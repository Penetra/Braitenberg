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
		self.leftSmellSensor = None
		self.rightSmellSensor = None
		self.leftSoundSensor = None
		self.rightSoundSensor = None
		self.leftLightSensor = None
		self.rightLightSensor = None
		myBraitenbergControl.init( self )

	def init( self ):
		self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
		self.watch( self.vehicle )

		#Blocks	
		for i in range(10):
			self.block = breve.createInstances( breve.BraitenbergBlock,1)
			self.block.move( breve.vector(i*4,0,5))
			self.block = breve.createInstances( breve.BraitenbergBlock,1)
			self.block.move( breve.vector(i*4,0,-5))

		for i in range(10,14):	
			self.block = breve.createInstances( breve.BraitenbergBlock,1)
			self.block.move( breve.vector(i*4,0,5))

		self.block = breve.createInstances( breve.BraitenbergBlock,1)
		self.block.move( breve.vector(13*4,0,5))
		self.block = breve.createInstances( breve.BraitenbergBlock,1)
		self.block.move( breve.vector(13*4,0,0))

		for i in range(10):
			self.block = breve.createInstances( breve.BraitenbergBlock,1)
			self.block.move( breve.vector(13*4,0,-5-i*4))
			self.block = breve.createInstances( breve.BraitenbergBlock,1)
			self.block.move( breve.vector(10*4,0,-5-i*4))

		#self.block = breve.createInstances( breve.BraitenbergBlock,1)
		#self.block.move( breve.vector(11.5*4,0,-5-9*4))


		# Light
		for i in range(15):
			breve.createInstances( breve.BraitenbergLight, 1 ).move( breve.vector( 36 + ( 14 * breve.breveInternalFunctionFinder.sin( self, ( ( i * 6.280000 ) / 20 ) ) ), 0, -55-(  14 * breve.breveInternalFunctionFinder.cos( self, ( ( i * 6.280000 ) / 20 ) ) ) ) )

		for i in range(26):
			self.smell = breve.createInstances( breve.BraitenbergSmell, 1)
			self.smell.move( breve.vector( 30 + ( -60 * breve.breveInternalFunctionFinder.sin( self, ( ( i * 6.280000 ) / 60 ) ) ), 0, -33 -(  38 * breve.breveInternalFunctionFinder.cos( self, ( ( i * 6.280000 ) / 60 ) ) ) ) )
			self.smell.setIntensity(2)



		#Wheels and Sensors
		front_left = self.vehicle.addWheel(breve.vector(0,0,-1.5))
		front_right = self.vehicle.addWheel(breve.vector(0,0,1.5))

		leftSoundSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, -1.4),breve.vector( 0, 0, 1 ),1,"Sounds")
		leftSoundSensor.setActivationType("linear")
		rightSoundSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, 1.4),breve.vector( 0, 0, 1 ),1,"Sounds")
		rightSoundSensor.setActivationType("linear")		

		leftLightSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, -1.4),breve.vector( 0, 0, 1 ),1,"Lights")
		rightLightSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, 1.4),breve.vector( 0, 0, 1 ),1,"Lights")
		rightLightSensor.setActivationType("linear")
		leftLightSensor.setActivationType("linear")

		leftLightSensor.link(front_right)
		rightLightSensor.link(front_left)

		rightSmellSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, 1.4),breve.vector( 0, 0, 1 ),1,"Smells")
		leftSmellSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, -1.4),breve.vector( 0, 0, 1 ),1,"Smells")
		leftSmellSensor.setActivationType("linear")
		rightSmellSensor.setActivationType("linear")
		
		rightSmellSensor.link(front_left)
		leftSmellSensor.link(front_right)

		leftSensor = self.vehicle.addSensor(breve.vector( 2.2, 0.1, -1.4 ),breve.vector( 0, 0, 1 ),1,"Blocks")
		rightSensor = self.vehicle.addSensor(breve.vector( 2.2, 0.1, 1.4 ),breve.vector( 0, 0, 1 ),1,"Blocks")
		leftSensor.setActivationType("linear")
		rightSensor.setActivationType("linear")

		leftSensor.link(front_left)
		rightSensor.link(front_right)

		front_left.setNaturalVelocity(0.5)
		front_right.setNaturalVelocity(0.5)


		breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()