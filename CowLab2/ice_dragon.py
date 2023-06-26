from dragon import Dragon
#Ice dragon class derived from dragon class
class IceDragon(Dragon):
    #passing function from dragon(cow) class
    pass

    def __init__(self, name, image):
        self.name = name
        self.image = image
        
    def can_breathe_fire(self):
        return False
        