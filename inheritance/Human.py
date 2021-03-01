from Being import Being

class Human(Being):
    def __init__(self, name, quarts, bloodType):
         super().__init__(name, quarts)
         self.__bloodType = bloodType

    # getter and setter for blood type
    def getBloodType(self):
        return self.__bloodType
    
    def setBloodType(self,newBloodType):
        self.__bloodType = newBloodType

    # check if human is alive. If number of quarts of blood is 0, the human is dead, so return false.
    # if human number of quarts of blood is greater than zero, human is alive, so return true.
    def isAlive(self):
        if self.getQuarts() > 0 :
            return True
        elif self.getQuarts() == 0:
            return False

    # strings together name, number of quarts of blood, and blood type of the human
    def __str__(self):
        msg = "Human " + self.getName() + " has " + str(self.getQuarts()) + \
              " quarts of type " + self.__bloodType + " blood."
        return msg

