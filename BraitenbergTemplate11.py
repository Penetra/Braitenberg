
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
		#self.light = breve.createInstances( breve.BraitenbergLight, 1 )
		#self.light.move( breve.vector( 10, 0, -2 ) )
		#self.light2 = breve.createInstances( breve.BraitenbergLight, 1 )
		#self.light2.move( breve.vector( 25, 0, 0 ) )
		self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
		self.watch( self.vehicle )
		
		
		front_left = self.vehicle.addWheel(breve.vector(-1,0,-1.5))
		front_right = self.vehicle.addWheel(breve.vector(-1,0,1.5))
		#s1 = self.vehicle.addSensor(breve.vector(2,0,-1),1,"light")
		#s2 = self.vehicle.addSensor(breve.vector(2,0,1),1,"light")
		
		#s1.link(front_left)
		#s1.link(back_left)
		
		#front_right.setNaturalVelocity(0.5)
		#front_left.setNaturalVelocity(0.5)
		
		leftSensor = self.vehicle.addSensor(breve.vector( 2.2, 0.1, -1.4 ),breve.vector( 0, 0, 1 ),1,"block")
		rightSensor = self.vehicle.addSensor(breve.vector( 2.2, 0.1, 1.4 ),breve.vector( 0, 0, 1 ),1,"block")
		
		leftSensor.link(front_left)
		rightSensor.link(front_right)
		
		#self.block = breve.createInstances( breve.BraitenbergBlock,1)
		#self.block.move( breve.vector(14*4,0,0))
		
		for i in range(11):
			self.block = breve.createInstances( breve.BraitenbergBlock,1)
			self.block.move( breve.vector(i*4,0,5))
			self.block = breve.createInstances( breve.BraitenbergBlock,1)
			self.block.move( breve.vector(i*4,0,-5))
			
		for i in range(11,14):	
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
			
		self.block = breve.createInstances( breve.BraitenbergBlock,1)
		self.block.move( breve.vector(11.5*4,0,-5-9*4))
			
breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
