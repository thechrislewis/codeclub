# class for moving object
# includes basic physics but not using vectors yet

class movingObj:

    def __init__(self):
        self.x = 10
        self.y = 20
        self.speedx = 0.0
        self.speedy = 0.0
        self.accelx = 0.0
        self.accely = 0.0

    def update(self):
	# acceleration changes velocity and velocity changes position
		
	# add acceleration
	self.speedx += self.accelx
        self.speedy += self.accely
	
	# update speed / velocity 
        self.x += self.speedx
        self.y += self.speedy
	
	# reset accel for next cycle
        self.accelx = self.accely = 0.0
		
    def applyForce(self, force) # force is tuple
        self.accelx += force[0]
        self.accely += force[1]
		
    def show(self):
	    pass
	
