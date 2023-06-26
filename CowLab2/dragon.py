from cow import Cow
#Dragon class derived from cow
class Dragon(Cow):
#passes functions from cow class
    pass

    def __init__(self, name, image):
        self.name = name
        self.image = image

    def can_breathe_fire(self):
        return True
        