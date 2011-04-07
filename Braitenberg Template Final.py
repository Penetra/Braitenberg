import breve
import os, sys

class myBraitenbergControl( breve.BraitenbergControl ):
    def __init__( self ):
        breve.PhysicalControl.__init__( self )
        myBraitenbergControl.init( self )
    
    def init( self ):
	
		#Set the camera's position and direction
		self.pointCamera( breve.vector( 0, 0, -12 ), breve.vector( 0, 60, 1 ) )
		#self.watch( self.vehicle )

		#Set various settings
		self.enableSmoothDrawing()
		self.disableLighting()
		self.floor = breve.createInstances( breve.Floor, 1 )
		self.floor.setColor( breve.vector( 0, 0, 0 ) )

		#Create vehicle
		self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
		self.vehicle.setWheelWidth( 0.50000 )

		#Create vehicle wheels
		front_left = self.vehicle.addWheel( breve.vector( 1.4, 0, 0 ) )
		back_left = self.vehicle.addWheel( breve.vector( -1.4, 0, 0 ) )

		#Create vehicle sensors        
		sensor = self.vehicle.addSensor( breve.vector( 0, 0.6, -1), breve.vector( -1, 0, 0 ), -1, "Balls" )
		sensor2 = self.vehicle.addSensor( breve.vector( 0, 0.6, -1), breve.vector( -1, 0, 0 ), -1, "Balls" )

		#Set the sensors' max strength
		sensor.setUpperX( 20 )
		sensor.setUpperX( 20 )

		#Link each sensor to each wheel
		sensor.link(front_left)
		sensor2.link(back_left)

		#Create ball        
		self.ball = breve.createInstances( breve.BraitenbergBall, 1 )
		self.ball.move( breve.vector( 0, 0, -2 ) )
		self.ball.setVelocity( breve.vector(-5, 0, -6 ) )

		#Create some sounds
		self.targetSound = breve.createInstances( breve.Sound, 1 ).load( 'sounds/soundeffects/Arcade_S-wwwbeat-1886.wav' )
		self.victorySound = breve.createInstances( breve.Sound, 1 ).load( 'sounds/soundeffects/Victory Fanfare.wav' )

		#Define some level settings
		self.firstLevel = 1
		self.lastLevel = 1#len( os.listdir( os.getcwd()+"/levels" ) )
		self.currentLevel = 0
		self.southWall = None
		self.northWall = None
		self.eastWall = None
		self.westWall = None
		self.otherWalls = []

		#Let the game begin!
		self.level( self.firstLevel )
		
		breve.myBraitenbergControl = myBraitenbergControl
		
    def level( self, level ):
		'''Method responsible for the creation of each level'''

		'''
		dist1 - distance from the southWall to the spaceship
		dist2 - distance from the spaceship to the first line of blocks
		dist3 - distance from the last line of blocks to the northWall
		dist4 - distance from a side block to the wall on the same side. Min = 0, Max = 2
		'''
		
		blockColor = breve.vector( 0, 0, 0.2 )
		
		breve.deleteInstances( self.southWall )
		breve.deleteInstances( self.northWall )
		breve.deleteInstances( self.eastWall )
		breve.deleteInstances( self.westWall )
		for i in self.otherWalls:
			breve.deleteInstances( i )

		self.vehicle.move( breve.vector( 0, 0, 0 ) )
		self.ball.move( breve.vector( 0, 0, -2 ) )
		self.ball.setVelocity( breve.vector( -5, 0, -6 ) )

		if level == 0:
			self.currentLevel += 1
		else:
			self.currentLevel = level
		if os.name == 'posix':
			filename = "levels/level"+str(self.currentLevel)+".txt"
		else:
			filename = "levels\level"+str(self.currentLevel)+".txt"
			
		self.nTargets = 0

		try:
			f = open(filename, "r")
			
			dists = f.readline().split(" ")
			dist1 = int(dists[0])
			dist2 = int(dists[1])
			dist3 = int(dists[2])
			dist4 = int(dists[3])
			
			limits = f.readline().split(" ")
			lines = int(limits[0])
			columns = int(limits[1])
			
			startX = -1 * 4 * columns/2 + 2
			startY = -1 * 2 * lines
			
			for i in range(lines):
				line = f.readline()
				for j in range(len(line)):
					if (line[j] != " " and line[j] != "\n"):
						c = int(line[j])
						if c > 0:
							block = breve.createInstances( breve.BraitenbergTarget, 1 )
							block.setCounter(c)
							block.setControl(self)
							self.nTargets += 1
						else:
							block = breve.createInstances( breve.Stationary, 1 )
							block.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector( 4, 1, 2 ) ) )
							block.setColor( blockColor )
							self.otherWalls.append( block )
						block.move( breve.vector( startX + (j*4), 1, startY + (i*2) - dist2 ) )
						
			f.close()
				
		except IOError:
			print "Error: File named "+filename+" could not found in directory "+os.getcwd()+"\levels"
			#default values
			dist1 = 6
			dist2 = 0
			dist3 = 6
			dist4 = 2
			lines = 6
			columns = 6
			startX = -10
			startY = -12

		self.southWall = breve.createInstances( breve.Stationary, 1 )
		self.southWall.setColor ( blockColor )
		self.southWall.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector( (columns+1 ) * 4, 2, 2 ) ) )
		self.southWall.move( breve.vector( 0, 1, dist1 ) )
		self.northWall = breve.createInstances( breve.Stationary, 1 )
		self.northWall.setColor ( blockColor )
		self.northWall.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector( (columns+1 ) * 4, 2, 2 ) ) )
		self.northWall.move( breve.vector( 0, 1, startY - dist2 - dist3 + 0.5 ) )
		self.eastWall = breve.createInstances( breve.Stationary, 1 )
		self.eastWall.setColor ( blockColor )
		self.eastWall.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector( 2, 2, (lines+1) * 2 + dist1 + dist2 + dist3 - 4 ) ) )
		self.eastWall.move( breve.vector( -startX + 3 + dist4, 1, dist1 - lines - (dist1 + dist2 + dist3)/2 ) )
		self.westWall = breve.createInstances( breve.Stationary, 1 )
		self.westWall.setColor ( blockColor )
		self.westWall.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector( 2, 2, (lines+1) * 2 + dist1 + dist2 + dist3 - 4 ) ) )
		self.westWall.move( breve.vector( startX - 3 - dist4, 1, dist1 - lines - (dist1 + dist2 + dist3)/2 ) )
	
    def playTargetSound ( self ):
		self.targetSound.play( 1.0 )
		
    def playVictorySound ( self ):
		self.victorySound.play( 1.0 )		
	
    def updateTargets ( self ):
		'''Decreases the number of targets present in the game and returns the current number of targets. Method called everytime a OBJECT(BraitenbergTarget) is destroyed.'''
		self.nTargets -= 1
	
		if self.nTargets == 0:
			if self.currentLevel == self.lastLevel:
				self.playVictorySound()
				if os.name == 'posix':
					self.endSimulation()
				else:
					self.pause()
			else:
				self.level( 0 )


#Create an instance of our controller object to initialize the simulation
myBraitenbergControl()
