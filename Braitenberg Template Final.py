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

		self.targetSound = breve.createInstances( breve.Sound, 1 ).load( 'sounds/soundeffects/Arcade_S-wwwbeat-1886.wav' )
		self.victorySound = breve.createInstances( breve.Sound, 1 ).load( 'sounds/soundeffects/Victory Fanfare.wav' )

		self.firstLevel = 6
		self.lastLevel = len( os.listdir( os.getcwd()+"/levels" ) )

		self.setArkanoid( self.vehicle, self.ball, self.firstLevel, self.lastLevel, self.targetSound, self.victorySound )

		self.level( self.firstLevel )

		breve.myBraitenbergControl = myBraitenbergControl


#Create an instance of our controller object to initialize the simulation
myBraitenbergControl()
