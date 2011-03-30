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
		self.ball = None
		myBraitenbergControl.init( self )
	
	
	def init( self ):
		self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
		#self.vehicle.move(breve.vector(2,0,0))
		self.vehicle.rotate(breve.vector(0,2,0),3.14)
		#self.watch( self.vehicle )
		
		
		#Wheels
		front_left = self.vehicle.addWheel(breve.vector( 1.4, 0, -1.5 ))
		front_right = self.vehicle.addWheel(breve.vector(1.4,0,1.5))
		
		back_left = self.vehicle.addWheel(breve.vector( -1.4, 0, -1.5 ))
		back_right = self.vehicle.addWheel(breve.vector(-1.4,0,1.5))
		
		sensor = self.vehicle.addSensor(breve.vector(0, 0.1, 1.5),breve.vector( 1, 0, 0 ),-1,"Balls")
		
		sensor.link(front_left)
		sensor.link(front_right)
		sensor.link(back_left)
		sensor.link(back_right)
		
		self.ball = breve.createInstances(breve.BraitenbergBall,1)
		self.ball.move(breve.vector(0,0,-2))
		self.ball.enablePhysics()
		self.ball.setVelocity(breve.vector(-15,0,-15))
		self.ball.setE(0.5)
		
		self.southBlock = breve.createInstances(breve.BraitenbergTarget,1)
		self.southBlock.setShape( breve.createInstances(breve.Shape,1).initWithCube(breve.vector(40,3,3)))
		self.southBlock.move(breve.vector(0,2,4))
		self.northBlock = breve.createInstances(breve.BraitenbergTarget,1)
		self.northBlock.setShape( breve.createInstances(breve.Shape,1).initWithCube(breve.vector(40,3,3)))
		self.northBlock.move(breve.vector(0,2,-30))
		
		self.eastBlock = breve.createInstances(breve.BraitenbergTarget,1)
		self.eastBlock.setShape( breve.createInstances(breve.Shape,1).initWithCube(breve.vector(3,3,32)))
		self.eastBlock.move(breve.vector(20,2,-13))
		self.westBlock = breve.createInstances(breve.BraitenbergTarget,1)
		self.westBlock.setShape( breve.createInstances(breve.Shape,1).initWithCube(breve.vector(3,3,32)))
		self.westBlock.move(breve.vector(-20,2,-13))

		
		for i in range(12):
			breve.createInstances( breve.BraitenbergTarget,1).move(breve.vector(-16+(i*3),1,-20))
			breve.createInstances( breve.BraitenbergTarget,1).move(breve.vector(-16+(i*3),1,-17))
			breve.createInstances( breve.BraitenbergTarget,1).move(breve.vector(-16+(i*3),1,-14))
		
		breve.myBraitenbergControl = myBraitenbergControl
		

myBraitenbergControl()