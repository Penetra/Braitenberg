import breve
import os, sys

class myBraitenbergControl( breve.BraitenbergControl ):
    def __init__( self ):
        breve.BraitenbergControl.__init__( self )
        myBraitenbergControl.init( self )
    
    
    def init( self ):
    
        #Create vehicle
        self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
        
        #Create vehicle wheels
        front_left = self.vehicle.addWheel(breve.vector( 1.4, 0, 0 ))
        #front_right = self.vehicle.addWheel(breve.vector( 1.4,0,1.2))
        
        back_left = self.vehicle.addWheel(breve.vector( -1.4, 0, 0 ))
        #back_right = self.vehicle.addWheel(breve.vector(-1.4,0,1.2))
        
        #Create vehicle sensors        
        sensor = self.vehicle.addSensor(breve.vector(0, 0.6, -1),breve.vector( -1, 0, 0 ),-1,"Balls")
        sensor2 = self.vehicle.addSensor(breve.vector(0, 0.6, -1),breve.vector( -1, 0, 0 ),-1,"Balls")

        sensor.setUpperX(20)
        sensor.setUpperX(20)

        sensor.link(front_left)
        sensor2.link(back_left)
        #sensor.link(front_right)
        #sensor2.link(back_right)
        
        #Create ball        
        self.ball = breve.createInstances(breve.BraitenbergBall,1)
        self.ball.move(breve.vector(0, 0, -2))
        self.ball.setVelocity(breve.vector(-5, 0, -6))
        
        #Create level
        
        '''
        dist1 - distance from the southWall to the spaceship
        dist2 - distance from the spaceship to the first line of blocks
        dist3 - distance from the last line of blocks to the northWall
        dist4 - distance from a side block to the wall on the same side. Min = 0, Max = 2
        '''
        
        blockColor = breve.vector( 0, 0, 0.2 )
        nTargets = 0
        
        filename = "level5.txt"
        
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
                            nTargets += 1
                        else:
                            block = breve.createInstances( breve.Stationary, 1 )
                            block.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector( 4, 1, 2 ) ) )
                            block.setColor ( blockColor )
                        block.move( breve.vector( startX + (j*4), 1, startY + (i*2) - dist2 ) )
                        
            f.close()
                
        except IOError:
            print "Error: File named "+filename+" could not found in directory "+os.getcwd()
            dist1 = 6
            dist2 = 0
            dist3 = 6
            dist4 = 2
            lines = 6
            columns = 6
            startX = -10
            startY = -12
            
        myBraitenbergControl.setTargets(self, nTargets)
        
        self.southWall = breve.createInstances( breve.Stationary, 1 )
        self.southWall.setColor ( blockColor )
        self.southWall.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector( (columns+1) * 4, 2, 2 ) ) )
        self.southWall.move( breve.vector( 0, 1, dist1 ) )
        self.northWall = breve.createInstances( breve.Stationary, 1 )
        self.northWall.setColor ( blockColor )
        self.northWall.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector( (columns+1) * 4, 2, 2 ) ) )
        self.northWall.move( breve.vector( 0, 1, startY - dist2 - dist3 ) )
        self.eastWall = breve.createInstances( breve.Stationary, 1 )
        self.eastWall.setColor ( blockColor )
        self.eastWall.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector( 2, 2, (lines+1) * 2 + dist1 + dist2 + dist3 - 4 ) ) )
        self.eastWall.move( breve.vector( -startX + 3 + dist4, 1, dist1 - lines - (dist1 + dist2 + dist3)/2 ) )
        self.westWall = breve.createInstances( breve.Stationary, 1 )
        self.westWall.setColor ( blockColor )
        self.westWall.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube( breve.vector( 2, 2, (lines+1) * 2 + dist1 + dist2 + dist3 - 4 ) ) )
        self.westWall.move( breve.vector( startX - 3 - dist4, 1, dist1 - lines - (dist1 + dist2 + dist3)/2 ) )
        
		
        #Set the camera's position
        #self.watch( self.vehicle )
        self.disableLighting()
        self.pointCamera( breve.vector( 0, 0, -12 ), breve.vector( 0, 60, 1 ) )    
		
        breve.myBraitenbergControl = myBraitenbergControl


#Create an instance of our controller object to initialize the simulation
myBraitenbergControl()
