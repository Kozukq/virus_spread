class Behavior:
	def __init__(self, name, speed, isProtected, isPsycho):
		self.behaviorName = name
		self.speed = speed
		self.protected = isProtected
		self.isPsycho = isPsycho


behaviorTypes = {
	"Cautious": Behavior("Cautious", 15, True, False),
	"Uncareful": Behavior("Uncareful", 20, False, False)
}