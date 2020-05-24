class Behavior:
	def __init__(self, name, speed, isProtected, isPsycho):
		self.behaviorName = name
		self.speed = speed
		self.isProtected = isProtected
		self.isPsycho = isPsycho


behaviorTypes = []
behaviorTypes.append(Behavior("Cautious", 15, True, False))
behaviorTypes.append(Behavior("Uncareful", 20, False, False))