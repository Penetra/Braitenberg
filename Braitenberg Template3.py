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
		self.vehicle.move(breve.vector(2,1,10))
		self.vehicle.rotate(breve.vector(0,1,0),3.14)
		self.watch( self.vehicle )

		self.block = breve.createInstances( breve.BraitenbergSound,1)
		self.block.move( breve.vector(2,1,15))
		self.block = breve.createInstances( breve.BraitenbergSound,1)
		self.block.move( breve.vector(-18,1,15))


		'''Adds wheels and sensors.'''
		lWheel = self.vehicle.addWheel (breve.vector( 0, 0, -1.5 ))
		rWheel = self.vehicle.addWheel (breve.vector( 0, 0, 1.5 ))

		#Correct values
		lFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, -1.4 ), breve.vector( 0.75, 0, 1 ),1, "Sounds")
		rFrontSensor = self.vehicle.addSensor (breve.vector( 2.2, 0.1, 1.4 ),breve.vector( -0.75, 0, 1 ),1, "Sounds")
		lFrontSensor.setActivationType("gauss")
		rFrontSensor.setActivationType("gauss")
		
		'''Links the sensors to the wheels.'''
		lFrontSensor.link(rWheel)
		rFrontSensor.link(lWheel)

		#Correct values
		lWheel.setNaturalVelocity(1.16)
		rWheel.setNaturalVelocity(1.16)

		#Correct values
		lFrontSensor.setBias(0.005)
		rFrontSensor.setBias(0.005)
	
		breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()