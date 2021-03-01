from Being import Being

class Vampire(Being):
    def __init__(self, name, quarts, animalForm):
        super().__init__(name, quarts)
        self.__maxBlood = 5
        self.__hungerLevels = ["starving","hangry","hungry","content","full","stuffed"]
        self.__animalForm = animalForm

    # get and set method for animal form
    def getAnimalForm(self):
        return self.__animalForm

    def setAnimalForm(self, newForm):
        self.__animalForm = newForm

    # use the vampire's current quart of blood as an index for the hungerlevels list to determine hunger level
    def getHunger(self):
        hunger = self.__hungerLevels # list of the hunger levels
        level = self.getQuarts() # this acts as the index
        return hunger[level]

    # gets the quarts of blood the vampire to determine his hunger levels
    def isStuffed(self):
        # if vampire's quarts of blood is equal to the max blood (5), then return True.
        # It is true that vampire is stuffed
        if self.getQuarts() == self.__maxBlood:
            return True
        # return false if the vampire's quarts of blood is not equal to the max.
        else:
            return False
    # simulates blood sucking. Increase vampire's quarts of blood by one and decrease human's quarts of blood by one.
    def suckBlood(self, human):
        human.decreaseQuarts()
        self.increaseQuarts()

    def __str__(self):
        msg = self.getName() + " is " + self.getHunger() + "."
        return msg

