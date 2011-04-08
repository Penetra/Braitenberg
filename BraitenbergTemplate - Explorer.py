
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
		
		leftSoundSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, -1.4),breve.vector( 0, 0, 1 ),1,"Sounds")
		rightSoundSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, 1.4),breve.vector( 0, 0, 1 ),1,"Sounds")
		leftSoundSensor.link(front_right)
		rightSoundSensor.link(front_left)
		leftSoundSensor.setLeftSensor(1)
		leftSoundSensor.setBias(-0.5)
		rightSoundSensor.setBias(-0.5)

		leftLightSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, -1.4),breve.vector( 0, 0, 1 ),1,"Lights")
		rightLightSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, 1.4),breve.vector( 0, 0, 1 ),1,"Lights")
		leftLightSensor.link(front_right)
		rightLightSensor.link(front_left)
		
		rightSmellSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, 1.4),breve.vector( 0, 0, 1 ),1,"Smells")
		leftSmellSensor = self.vehicle.addSensor(breve.vector(2.2, 0.1, -1.4),breve.vector( 0, 0, 1 ),1,"Smells")
		rightSmellSensor.link(front_left)
		leftSmellSensor.link(front_right)
		
		leftSensor = self.vehicle.addSensor(breve.vector( 2.2, 0.1, -1.4 ),breve.vector( 0, 0, 1 ),1,"Blocks")
		rightSensor = self.vehicle.addSensor(breve.vector( 2.2, 0.1, 1.4 ),breve.vector( 0, 0, 1 ),1,"Blocks")
		leftSensor.link(front_right)
		rightSensor.link(front_left)
		leftSensor.setLeftSensor(1)
		leftSensor.setBias(-0.2)
		rightSensor.setBias(-0.2)
		
		front_left.setNaturalVelocity(2.0)
		front_right.setNaturalVelocity(2.0)
		
		
		
		#Surrounding blocks
		
		for i in range(20):
			#WEST
			breve.createInstances( breve.BraitenbergSound,1).move(breve.vector(-10+i*3,0,-30))
			#NORTH
			breve.createInstances( breve.BraitenbergSound,1).move(breve.vector(10,0,-30+i*3))
			#EAST
			breve.createInstances( breve.BraitenbergSound,1).move(breve.vector(-10+i*3,0,28))
			#SOUTH
			breve.createInstances( breve.BraitenbergSound,1).move(breve.vector(-10,0,-30+i*3))

		
		
		breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
