
# Note: this file was automatically converted to Python from the
# original steve-language source code.  Please see the original
# file for more detailed comments and documentation.


import breve

class myBraitenbergControl( breve.BraitenbergControl ):
    def __init__( self ):
        breve.BraitenbergControl.__init__( self )
        self.leftSensor = None
        self.leftWheel = None
        self.light = None
        self.rightSensor = None
        self.rightWheel = None
        self.vehicle = None
        myBraitenbergControl.init( self )

    def init( self ):
        self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
        self.watch( self.vehicle )
        self.vehicle.move(breve.vector(2,1,10))
        self.vehicle.rotate(breve.vector(0,1,0),3.14)
        self.block = breve.createInstances( breve.BraitenbergSound,1)
        self.block.move( breve.vector(2,1,15))
        self.block = breve.createInstances( breve.BraitenbergSound,1)
        self.block.move( breve.vector(-20,1,15))
        


        #Wheels and Sensors
        front_left = self.vehicle.addWheel(breve.vector(0,0,-1.5))
        front_right = self.vehicle.addWheel(breve.vector(0,0,1.5))
        
        leftSoundSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, -1.4),breve.vector( 0.75, 0, 1 ), 1, "Sounds")
        rightSoundSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, 1.4),breve.vector( -0.75, 0, 1 ), 1, "Sounds")
        leftSoundSensor.setActivationType("gauss")
        rightSoundSensor.setActivationType("gauss")
        leftSoundSensor.setGauss(0.8, 0.5)
        rightSoundSensor.setGauss(0.8, 0.5)
        leftSoundSensor.link(front_right)
        rightSoundSensor.link(front_left)
        
        front_left.setNaturalVelocity(1.2)
        front_right.setNaturalVelocity(1.2)
        
        leftSoundSensor.setBias(0.12)
        rightSoundSensor.setBias(0.12)
        
            
        breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
