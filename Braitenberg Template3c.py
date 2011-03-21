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
		
		#Wheels
		front_left = self.vehicle.addWheel(breve.vector(0,0,-1.5))
		front_right = self.vehicle.addWheel(breve.vector(0,0,1.5))
		
		#Sensors
		leftSoundSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, -1.4),breve.vector( 0, 0, 1 ),1,"Sounds")
		leftSoundSensor.setActivationType("linear")
		leftSoundSensor.link(front_left)
		rightSoundSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, 1.4),breve.vector( 0, 0, 1 ),1,"Sounds")
		rightSoundSensor.setActivationType("linear")
		rightSoundSensor.link(front_right)
		
		leftSmellSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, -1.4),breve.vector( 0, 0, 1 ),1,"Smells")
		leftSmellSensor.setActivationType("linear")
		leftSmellSensor.link(front_right)
		rightSmellSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, 1.4),breve.vector( 0, 0, 1 ),1,"Smells")
		rightSmellSensor.setActivationType("linear")
		rightSmellSensor.link(front_left)
		
		leftBlockSensor = self.vehicle.addSensor(breve.vector(2.2,0.1,-1.4),breve.vector(0,0,1),1,"Blocks")
		leftBlockSensor.setActivationType("linear")
		leftBlockSensor.link(front_right)
		leftBlockSensor.setBias(-0.2)
		rightBlockSensor = self.vehicle.addSensor(breve.vector(2.2,0.1,1.4),breve.vector(0,0,1),1,"Blocks")
		rightBlockSensor.setActivationType("linear")
		rightBlockSensor.link(front_left)
		rightBlockSensor.setBias(-0.2)
		

		leftLightSensor = self.vehicle.addSensor(breve.vector(2.2,0.1,-1.4),breve.vector(0,0,1),1,"Lights")
		leftLightSensor.setActivationType("linear")
		leftLightSensor.link(front_right)
		leftLightSensor.setBias(-0.4)
		rightLightSensor = self.vehicle.addSensor(breve.vector(2.2,0.1,1.4),breve.vector(0,0,1),1,"Lights")
		rightLightSensor.setActivationType("linear")
		rightLightSensor.link(front_left)
		rightLightSensor.setBias(-0.5)
		#Sound 
		for i in range(-5,0):
			self.light = breve.createInstances( breve.BraitenbergLight,1)
			self.light.move( breve.vector(1+i*3,0,6))
			self.light = breve.createInstances( breve.BraitenbergLight,1)
			self.light.move( breve.vector(-14,0,-9-i*3))
		for i in range(10):
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(i*4,0,5))
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(i*4,0,-5))
		for i in range(10,14):	
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(i*4,0,5))

		self.block = breve.createInstances( breve.BraitenbergSound,1)
		self.block.move( breve.vector(13*4,0,5))
		self.block = breve.createInstances( breve.BraitenbergSound,1)
		self.block.move( breve.vector(13*4,0,0))

		for i in range(10):
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(13*4,0,-5-i*4))
			self.block.setIntensity(1.2)
			self.block = breve.createInstances( breve.BraitenbergSound,1)
			self.block.move( breve.vector(10*4,0,-5-i*4))	
			self.block.setIntensity(1.2)
			
		#Smell
		for i in range(15):
			self.smell = breve.createInstances( breve.BraitenbergSmell, 1 )
			self.smell.move( breve.vector( 36 + ( 14 * breve.breveInternalFunctionFinder.sin( self, ( ( i * 6.280000 ) / 30 ) ) ), 0, -55-(  14 * breve.breveInternalFunctionFinder.cos( self, ( ( i * 6.280000 ) / 30 ) ) ) ) )
			self.smell.setIntensity(1.2)
		
		for i in range(5):
			breve.createInstances( breve.BraitenbergBlock,1).move(breve.vector(25,0,-63-i*4))
			breve.createInstances( breve.BraitenbergBlock,1).move(breve.vector(25+i*4,0,-80))
			breve.createInstances( breve.BraitenbergBlock,1).move(breve.vector(25+i*4,0,-60))
			
		for i in range(12):
			breve.createInstances(breve.BraitenbergSmell,1).move(breve.vector(35-(i*4),0,-38+(i*3)))
		
		front_left.setNaturalVelocity(0.7)
		front_right.setNaturalVelocity(0.7)
		
		breve.myBraitenbergControl = myBraitenbergControl

myBraitenbergControl()