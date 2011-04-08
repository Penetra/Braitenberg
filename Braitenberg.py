
# Note: this file was automatically converted to Python from the
# original steve-language source code.  Please see the original
# file for more detailed comments and documentation.


import breve, os
from math import log, pi, e, sqrt


class BraitenbergControl( breve.PhysicalControl ):
	'''This class is used for building simple Braitenberg vehicle  simulations.  To create a Braitenberg vehicle simulation, subclass BraitenbergControl and use the init method to  create OBJECT(BraitenbergLight) and  OBJECT(BraitenbergVehicle) objects.'''

	def __init__( self ):
		breve.PhysicalControl.__init__( self )
		self.cloudTexture = None
		self.floor = None
		BraitenbergControl.init( self )

	def init( self ):
		self.enableLighting()
		self.enableSmoothDrawing()
		self.floor = breve.createInstances( breve.Floor, 1 )
		self.pointCamera( breve.vector( 0, 0, 0 ), breve.vector( 3, 3, 24 ) )
		self.enableShadows()
		self.enableReflections()
		self.cloudTexture = breve.createInstances( breve.Image, 1 ).load( 'images/clouds.png' )
		self.setBackgroundColor( breve.vector( 0.400000, 0.600000, 0.900000 ) )
		self.setBackgroundTextureImage( self.cloudTexture )
breve.BraitenbergControl = BraitenbergControl


class BraitenbergVehicle( breve.MultiBody ):
	'''This object is used in conjunction with OBJECT(BraitenbergControl) to create simple Braitenberg vehicles.'''

	def __init__( self ):
		breve.MultiBody.__init__( self )
		self.bodyLink = None
		self.bodyShape = None
		self.sensorShape = None
		self.sensors = breve.objectList()
		self.wheelShape = None
		self.wheels = breve.objectList()
		self.wheelWidth = 0.100000
		
		BraitenbergVehicle.init( self )
		
	def init( self ):
		self.bodyShape = breve.createInstances( breve.Shape, 1 )
		self.bodyShape.initWithCube( breve.vector( 4.000000, 0.750000, 3.000000 ) )
		self.wheelShape = breve.createInstances( breve.Shape, 1 )
		self.wheelShape.initWithPolygonDisk( 40, self.getWheelWidth(), self.getWheelRadius() )
		self.sensorShape = breve.createInstances( breve.Shape, 1 )
		self.sensorShape.initWithPolygonCone( 10, 0.500000, 0.200000 )
		self.bodyShape.setDensity( self.getDensity() )
		self.bodyLink = breve.createInstances( breve.Link, 1 )
		self.bodyLink.setShape( self.bodyShape )
		self.bodyLink.setMu( -1.000000 )
		self.bodyLink.setET( 0.800000 )
		self.setRoot( self.bodyLink )
		self.move( breve.vector( 0, 0.900000, 0 ) )
		self.setTextureScale( 1.500000 )
		
		#self.setTextureImage( breve.createInstances( breve.Image, 1 ).load( 'images/jon.png' ) )
		#self.setTextureScale( 1.500000 )

	def addSensor( self, location, rotation, direction, type ):
		'''Adds a sensor at location on the vehicle.  This method returns the sensor which is created, a OBJECT(BraitenbergSensor).  You'll use the returned object to connect it to the vehicle's wheels.'''

		joint = None
		sensor = None
		
		if type=="Lights":
			sensor = breve.createInstances( breve.BraitenbergLightSensor, 1 )
			sensor.setColor( breve.vector( 1, 0, 0 ) )
			
		elif type=="Smells":
			sensor = breve.createInstances( breve.BraitenbergSmellSensor, 1 )
			sensor.setColor( breve.vector( 0, 1, 0 ) )
		
		elif type=="Sounds":
			sensor = breve.createInstances( breve.BraitenbergSoundSensor, 1 )
			sensor.setColor( breve.vector( 0, 0, 1 ) )
		
		elif type=="Blocks":
			sensor = breve.createInstances( breve.BraitenbergBlockSensor, 1 )
			sensor.setColor( breve.vector( 0, 0, 0 ) )
		elif type=="Balls":
			sensor = breve.createInstances( breve.BraitenbergBallSensor, 1 )
			sensor.setColor( breve.vector( 0.5, 0.3, 0.1 ) )
		
		sensor.setType(type)
		sensor.setShape( self.sensorShape )
		joint = breve.createInstances(breve.FixedJoint,1)
		if direction>0:
			joint.setRelativeRotation(rotation, 1.570000)
		else:
			joint.setRelativeRotation(rotation, -1.570000)
		joint.link( location, breve.vector( 0, 0, 0 ), sensor, self.bodyLink )
		joint.setDoubleSpring( 300, 0.010000, -0.010000 )
		self.addDependency( joint )
		self.addDependency( sensor )
		self.sensors.append( sensor )
		return sensor

	def addWheel( self, location ):
		'''Adds a wheel at location on the vehicle. This method returns the wheel which is created, a OBJECT(BraitenbergWheel).  You'll use the returned object to connect it to the vehicle's sensors.'''

		joint = None
		wheel = None

		wheel = breve.createInstances( breve.BraitenbergWheel, 1 )
		wheel.setShape( self.wheelShape )
		joint = breve.createInstances( breve.RevoluteJoint, 1 )
		joint.setRelativeRotation( breve.vector( 1, 0, 0 ), 1.570800 )
		joint.link( breve.vector( 0, 0, 1 ), location, breve.vector( 0, 0, 0 ), wheel, self.bodyLink )
		wheel.setET( 0.800000 )
		wheel.setJoint( joint )
		joint.setStrengthLimit( ( joint.getStrengthHardLimit() / 2 ) )
		wheel.setColor( breve.vector( 0.600000, 0.600000, 0.600000 ) )
		wheel.setMu( 100000 )
		self.addDependency( joint )
		self.addDependency( wheel )
		self.wheels.append( wheel )
		return wheel

	def destroy( self ):
		breve.deleteInstances( self.sensorShape )
		breve.deleteInstances( self.wheelShape )
		breve.deleteInstances( self.bodyShape )
		breve.MultiBody.destroy( self )

	def getDensity( self ):
		return 1.000000

	def getWheelRadius( self ):
		return 0.600000

	def getWheelWidth( self ):
		return self.wheelWidth
	
	def setWheelWidth(self, width):
		self.wheelWidth = width
		self.wheelShape.initWithPolygonDisk( 40, self.getWheelWidth(), self.getWheelRadius() )
	
breve.BraitenbergVehicle = BraitenbergVehicle


class BraitenbergHeavyVehicle( breve.BraitenbergVehicle ):
	'''A heavy duty version of OBJECT(BraitenbergVehicle), this vehicle is heavier and harder to control, but more stable at higher  speeds.'''

	def __init__( self ):
		breve.BraitenbergVehicle.__init__( self )

	def getDensity( self ):
		return 20.000000

	def getWheelRadius( self ):
		return 0.800000

	def getWheelWidth( self ):
		return 0.400000
breve.BraitenbergHeavyVehicle = BraitenbergHeavyVehicle


class BraitenbergLight( breve.Mobile):
	'''A BraitenbergLight is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the lights--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Mobile.__init__( self )
		BraitenbergLight.init( self )

	def init( self):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithSphere( 0.300000 ) )
		self.setColor( breve.vector( 1, 0, 0 ) )
		self.intensity = 1.0
		
	def setIntensity(self, intensity):
		self.intensity = intensity
breve.BraitenbergLight = BraitenbergLight


class BraitenbergSmell( breve.Mobile ):
	'''A BraitenbergSmell is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergSmellSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the smells--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Mobile.__init__( self )
		BraitenbergSmell.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithSphere( 0.400000 ) )
		self.setColor( breve.vector( 0, 1, 0 ) )
		self.intensity = 1 #default
		
	def setIntensity(self, intensity):
		self.intensity = intensity
breve.BraitenbergSmell = BraitenbergSmell


class BraitenbergSound( breve.Mobile ):
	'''A BraitenbergSound is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergSoundSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the sounds--they're  basically just plain OBJECT(Mobile) objects.'''

	def __init__( self ):
		breve.Mobile.__init__( self )
		BraitenbergSound.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithSphere( 0.500000 ) )
		self.setColor( breve.vector( 0, 0, 1 ) )
		self.intensity = 1
		
	def setIntensity(self, intensity):
		self.intensity = intensity
breve.BraitenbergSound = BraitenbergSound


class BraitenbergBlock(breve.Mobile):
	'''A BraitenbergBlock is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergBlockSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the blocks--they're  basically just plain OBJECT(Mobile) objects.'''
	
	def __init__( self ):
		breve.Mobile.__init__( self )
		BraitenbergBlock.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube(breve.vector( 2, 2, 2 ) ) )
		self.setColor( breve.vector( 5, 5, 0 ) )
		self.reflection = 1
		
	def setReflection(self, intensity):
		self.reflection = reflection
breve.BraitenbergBlock = BraitenbergBlock


class BraitenbergTarget(breve.Stationary):
	'''A BraitenbergTarget is used in conjunction with OBJECT(BraitenbergControl) and OBJECT(BraitenbergVehicle).  It is what the OBJECT(BraitenbergTargetSensor) objects on the BraitenbergVehicle detect. <p> There are no special behaviors associated with the targets--they're  basically just plain OBJECT(Stationary) objects.'''
	def __init__( self ):
		breve.Stationary.__init__( self )
		BraitenbergTarget.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithCube(breve.vector( 4, 1, 2 ) ) )
		self.setE( 1 )
		self.handleCollisions( 'BraitenbergBall', 'kill' )
		self.control = None
		
	def setControl( self, control ):
		self.control = control
				
	def setCounter( self, counter ):
		'''Sets the number of hits necessary for the target to be destroyed and the target's starting color'''
		self.counter = counter
		self.setColor( breve.vector( 0, 1, self.counter * 0.2 ) )
		
	def kill( self ):
		'''Decreases the number of hits necessary for the target to be destroyed and changes the target's color. Called everytime a OBJECT(BraitenbergBall) hits the target.'''
		self.control.playTargetSound()
		self.counter -= 1
		self.setColor( breve.vector( 0, 1, self.counter * 0.2 ) )
		if self.counter==0:
			breve.deleteInstance(self)
			self.control.updateTargets()

breve.BraitenbergTarget = BraitenbergTarget


class BraitenbergBall( breve.Mobile ):		
	def __init__( self ):
		breve.Mobile.__init__( self )
		BraitenbergBall.init( self )

	def init( self ):
		self.setShape( breve.createInstances( breve.Shape, 1 ).initWithSphere( 0.400000 ) )
		self.setColor( breve.vector( 1, 0, 0 ) )
		self.enablePhysics()
		self.setE(1)
		self.handleCollisions('BraitenbergTarget', 'accelerate')
		self.handleCollisions('BraitenbergVehicle', 'accelerate')
		self.handleCollisions('BraitenbergWheel', 'accelerate')
		self.handleCollisions('BraitenbergBallSensor', 'accelerate')
		self.handleCollisions('Mobile', 'accelerate')
		self.handleCollisions('Stationary', 'accelerate')
		self.handleCollisions('Link', 'accelerate')
	
	def accelerate(self):
		'''Sets the ball's velocity to a higher or smaller velocity depending on the situation. Method called everytime the ball hits something.'''
		vel = self.getVelocity()
		mod = sqrt(vel[0]**2 + vel[2]**2)
		self.setVelocity(vel * (5/mod))
		
breve.BraitenbergBall = BraitenbergBall


class BraitenbergWheel( breve.Link  ):
	'''A BraitenbergWheel is used in conjunction with OBJECT(BraitenbergVehicle) to build Braitenberg vehicles.  This class is typically not instantiated manually, since OBJECT(BraitenbergVehicle) creates one for you when you add a wheel to the vehicle. <p> <b>NOTE: this class is included as part of the file "Braitenberg.tz".</b>'''

	def __init__( self ):
		breve.Link.__init__( self )
		self.joint = None
		self.naturalVelocity = 0
		self.newVelocity = 0
		self.oldVelocity = 0
		BraitenbergWheel.init( self )

	def activate( self, n ):
		self.newVelocity = ( self.newVelocity + n )

	def init( self ):
		self.naturalVelocity = 0
		self.newVelocity = 0

	def postIterate( self ):
		if ( self.newVelocity > 30 ):
			self.newVelocity = 30

		if ( self.newVelocity == 0 ):
			self.joint.setJointVelocity( self.oldVelocity )
			self.oldVelocity = ( self.oldVelocity * 0.950000 )

		else:
			self.joint.setJointVelocity( self.newVelocity )
			self.oldVelocity = self.newVelocity


		self.newVelocity = self.naturalVelocity

	def setJoint( self, j ):
		'''Used internally.'''

		self.joint = j

	def setNaturalVelocity( self, n ):
		'''Sets the "natural" velocity of this wheel.  The natural velocity is the speed at which the wheel turns in the absence of sensor input.  '''

		self.naturalVelocity = n
breve.BraitenbergWheel = BraitenbergWheel


class BraitenbergSensor( breve.Link ):
	'''A BraitenbergSensor is used in conjunction with OBJECT(BraitenbergVehicle) to build Braitenberg vehicles.  This class is typically not instantiated manually, since OBJECT(BraitenbergVehicle) creates one for you when you add a sensor to the vehicle. <p> <b>NOTE: this class is included as part of the file "Braitenberg.tz".</b>'''

	def __init__( self ):
		breve.Link.__init__( self )
		self.bias = 0
		self.direction = breve.vector()
		self.sensorAngle = 0
		self.wheels = breve.objectList()
		self.type = "BraitenbergLights" #default
		self.lowerBound = 0.0 #default
		self.upperBound = 9.0 #default
		self.activationType = "linear" #default
		self.average = 0.5 #default
		self.desvioPadrao = 0.13 #default
		self.lowerX = 0.0 #default
		self.upperX = () #default
		BraitenbergSensor.init( self )

	def init( self ):
		self.bias = 1.000000 
		self.direction = breve.vector( 0, 1, 0 )
		self.sensorAngle = 1.600000 
	
	def setType(self, type):
		self.type = "Braitenberg" + type
		
	def setLowerBound(self, lower):
		self.lowerBound = lower
	
	def setUpperBound(self, upper):
		self.upperBound = upper
		
	def setLowerX(self, lower):
		self.lowerX = lower
	
	def setUpperX(self, upper):
		self.upperX = upper
		
	def setActivationType(self, type):
		self.activationType = type
		
	def activationMethod(self, strength):
		if strength > self.upperX or strength < self.lowerX:
			return 0
		if(self.activationType == "linear"):
			return strength
		elif(self.activationType == "log"):
			if(strength < 1):
				return 0
			return log(strength,2)
			
		elif(self.activationType == "gauss"):
			return (1/ (self.desvioPadrao * sqrt(2*pi)) ) * (e**(-(((strength-self.average)**2)/(2*(self.desvioPadrao**2)))))
	
	def setGauss(self, mean, stdev):
		self.average = mean
		self.desvioPadrao = stdev
	
	def iterate( self ):
		i = None
		lights = 0
		angle = 0
		strength = 0
		total = 0
		transDir = breve.vector()
		toLight = breve.vector()

		transDir = ( self.getRotation() * self.direction )
		for i in breve.allInstances( self.type ):
			toLight = ( i.getLocation() - self.getLocation() )
			

			angle = breve.breveInternalFunctionFinder.angle( self, toLight, transDir )
			if ( angle < self.sensorAngle ):
				strength = breve.length( ( self.getLocation() - i.getLocation() ) ) 

				if self.activationType == "linear" and strength > 15:
					continue
				
				strength = ( 1.000000 / ( strength * strength ) ) * i.intensity
				#if ( self.activationMethod and self.activationObject ):
				#	strength = self.activationObject.callMethod( self.activationMethod, [ strength ] )
				#print "strength: %f " %(strength)
				strength = self.activationMethod(strength)
				#print strength

				if strength > self.upperBound:
					strength = self.upperBound
				elif strength < self.lowerBound:
					strength = self.lowerBound
				
					
				total = ( total + strength )
				lights = ( lights + 1 )


		if ( lights != 0 ):
			total = ( total / lights )
		
		total = ( ( 50 * total ) * self.bias )
		self.wheels.activate( total )

	def link( self, w ):
		'''Associates this sensor with wheel w.'''

		self.wheels.append( w )

	def setActivationMethod( self, m, o ):
		'''This method specifies an activation method for the sensor.  An activation method is a method which takes as input the strength read by the sensor, and as output returns the strength of the  signal which will travel on to the motor. <p> Your activation function should be defined as: <pre> + to <i>activation-function-name</i> with-sensor-strength s (float): </pre> <p> The default activation method is linear, but more complex vehicles may require non-linear activation functions. '''

		self.activationMethod = m
		self.activationObject = o

	def setBias( self, d ):
		'''Sets the "bias" of this sensor.  The default bias is 1, meaning that the sensor has a positive influence on associated wheels with strength 1.  You can change this to any magnitude, positive or negative.'''

		self.bias = d

	def setSensorAngle( self, n ):
		'''Sets the angle in which this sensor can detect light.  The default value of 1.5 means that the sensor can see most of everything in front of it.  Setting the value to be any higher leads to general wackiness, so I don't suggest it.'''

		self.sensorAngle = n
breve.BraitenbergSensor = BraitenbergSensor

class BraitenbergLightSensor( BraitenbergSensor ):
	def __init__( self ):
		breve.Link.__init__( self )
		self.bias = 0
		self.direction = breve.vector()
		self.sensorAngle = 0
		self.wheels = breve.objectList()
		self.lowerBound = 0.0 #default
		self.upperBound = 10.0 #default
		self.activationType = "linear" #default
		self.average = 0.5 #default
		self.desvioPadrao = 0.15 #default
		self.lowerX = 0.0 #default
		self.upperX = () #default
		BraitenbergLightSensor.init( self )
	def init( self ):
		self.bias = 1.000000
		self.direction = breve.vector( 0, 1, 0 )
		self.sensorAngle = 1.600000
breve.BraitenbergLightSensor = BraitenbergLightSensor


class BraitenbergSmellSensor( BraitenbergSensor ):
	def __init__( self ):
		breve.Link.__init__( self )
		self.bias = 0
		self.direction = breve.vector()
		self.sensorAngle = 0
		self.wheels = breve.objectList()
		self.lowerBound = 0.0 #default
		self.upperBound = 10.0 #default
		self.activationType = "linear" #default
		self.average = 0.5 #default
		self.desvioPadrao = 0.15 #default
		self.lowerX = 0.0 #default
		self.upperX = () #default
		BraitenbergSmellSensor.init( self )
	def init( self ):
		self.bias = 1.000000
		self.direction = breve.vector( 0, 1, 0 )
		self.sensorAngle = 1.600000
breve.BraitenbergSmellSensor = BraitenbergSmellSensor


class BraitenbergSoundSensor( BraitenbergSensor ):
	def __init__( self ):
		breve.Link.__init__( self )
		self.bias = 0
		self.direction = breve.vector()
		self.sensorAngle = 0
		self.wheels = breve.objectList()
		self.lowerBound = 0.0 #default
		self.upperBound = 10.0 #default
		self.activationType = "linear" #default
		self.average = 0.5 #default
		self.desvioPadrao = 0.15 #default
		self.lowerX = 0.0 #default
		self.upperX = () #default
		BraitenbergSoundSensor.init( self )
	def init( self ):
		self.bias = 1.000000
		self.direction = breve.vector( 0, 1, 0 )
		self.sensorAngle = 1.600000
breve.BraitenbergSoundSensor = BraitenbergSoundSensor


class BraitenbergBlockSensor(BraitenbergSensor):
	'''A BraitenbergBlockSensor is used in conjunction with OBJECT(BraitenbergVehicle) to build Braitenberg vehicles.  This class is typically not instantiated manually, since OBJECT(BraitenbergVehicle) creates one for you when you add a sensor to the vehicle. <p>'''

	def __init__( self ):
		breve.Link.__init__( self )
		self.bias = 0
		self.direction = breve.vector()
		self.sensorAngle = 0
		self.wheels = breve.objectList()
		self.lowerBound = 0.0 #default
		self.upperBound = 10.0 #default
		self.activationType = "linear" #default
		self.average = 1.0 #default
		self.desvioPadrao = 0.2 #default
		self.lowerX = 0.0 #default
		self.upperX = () #default
		self.counter = 0 #default
		BraitenbergBlockSensor.init( self )

	def init( self ):
		self.bias = 1.000000
		self.direction = breve.vector( 0, 1, 0 )
		self.sensorAngle = 1.200000
			
	def iterate( self ):
		i = None
		lights = 0
		angle = 0
		strength = 0
		total = 0
		transDir = breve.vector()
		toBlock = breve.vector()
		transDir = ( self.getRotation() * self.direction )
		
		least = ()
		item = None
		flag = False
		
		for i in breve.allInstances( "BraitenbergBlocks" ):
			toBlock = ( i.getLocation() - self.getLocation() )
			angle = breve.breveInternalFunctionFinder.angle( self, toBlock, transDir )
			if ( angle < self.sensorAngle ):
				strength = breve.length( ( self.getLocation() - i.getLocation() ) ) 
				if(strength < least):
					flag = True
					least = strength
					item = i
				#lights = ( lights + 1 )
				
		if flag:
			strength = (1.000000/(least * least) ) * 1/item.reflection
			#if ( self.activationMethod and self.activationObject ):
			#	strength = self.activationObject.callMethod( self.activationMethod, [ strength ] )
			self.counter=self.counter+1
			
			strength = self.activationMethod(strength)
			
			if ( strength > self.upperBound ):
				strength = self.upperBound
			elif strength < self.lowerBound:
				strength = self.lowerBound
			#total = ( total + least )


		#if ( lights != 0 ):
			#total = ( total / lights )
		total = strength
		total = ( ( 50 * total ) * self.bias )
		self.wheels.activate( total )
breve.BraitenbergBlockSensor = BraitenbergBlockSensor


class BraitenbergBallSensor( BraitenbergSensor ):
	'''A BraitenbergBallSensor is used in conjunction with OBJECT(BraitenbergVehicle) to build Braitenberg vehicles.  This class is typically not instantiated manually, since OBJECT(BraitenbergVehicle) creates one for you when you add a sensor to the vehicle. <p>'''
	def __init__( self ):
		breve.Link.__init__( self )
		self.bias = 0
		self.direction = breve.vector()
		self.sensorAngle = 0
		self.wheels = breve.objectList()
		self.lowerBound = 0.0 #default
		self.upperBound = 10.0 #default
		self.upperX = () #default
		BraitenbergBallSensor.init( self )
		
	def init( self ):
		self.bias = 1.000000
		self.direction = breve.vector( 0, 1, 0 )
		self.sensorAngle = 1.600000
		
	def iterate( self ):
		i = None
		strength = 0
		transDir = breve.vector()
		toBall = breve.vector()

		transDir = ( self.getRotation() * self.direction )
		for i in breve.allInstances( "BraitenbergBalls" ):
			toBall = ( i.getLocation() - self.getLocation() )
			angle = breve.breveInternalFunctionFinder.angle( self, toBall, transDir )
			if ( angle < self.sensorAngle ):
				strengthX = -1 * toBall[0]
				strengthY = toBall[2]
				strength = 12 * strengthX / strengthY
			else:
				strength = 0
		self.wheels.activate(strength)
breve.BraitenbergBallSensor = BraitenbergBallSensor


breve.BraitenbergVehicles = BraitenbergVehicle
breve.BraitenbergHeavyVehicles = BraitenbergHeavyVehicle
breve.BraitenbergLights = BraitenbergLight
breve.BraitenbergWheels = BraitenbergWheel
breve.BraitenbergSensors = BraitenbergSensor
breve.BraitenbergBlocks = BraitenbergBlock
breve.BraitenbergSmells = BraitenbergSmell
breve.BraitenbergSounds = BraitenbergSound
breve.BraitenbergTargets = BraitenbergTarget
breve.BraitenbergBalls = BraitenbergBall
