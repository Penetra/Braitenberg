
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
        
        #Wheels and Sensors
        front_left = self.vehicle.addWheel(breve.vector(0,0,-1.5))
        front_right = self.vehicle.addWheel(breve.vector(0,0,1.5))
        
        leftLightSensor = self.vehicle.addSensor(breve.vector(1.82, 0.1, -1.8),breve.vector( 1, 0, 0 ),1,"Lights")
        rightLightSensor = self.vehicle.addSensor(breve.vector(1.82, 0.1, 1.8),breve.vector( -1, 0, 0 ),1,"Lights")
        
        leftLightSensor.link(front_right)
        rightLightSensor.link(front_left)
        leftLightSensor.setUpperBound(0.028)
        rightLightSensor.setUpperBound(0.028)
        leftLightSensor.setUpperX(0.07811)
        rightLightSensor.setUpperX(0.07811)
        
        light = breve.createInstances( breve.BraitenbergLight, 1 )
        light.move( breve.vector (0, 1, 7.5))
        light.setIntensity(1.5)
        light = breve.createInstances( breve.BraitenbergLight, 1 )
        light.move( breve.vector (0, 1, -9))
        light.setIntensity(1.5)
        
        front_left.setNaturalVelocity(0.950)
        front_right.setNaturalVelocity(0.950)
        
            
        breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
