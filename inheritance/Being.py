class Being(object):
    def __init__(self, name, quarts):
        self.__name = name
        self.__quarts = quarts

    # get and set method for name
    def getName(self):
        return self.__name

    def setName(self,newName):
        self.__name = newName

    # get and set method for quarts
    def getQuarts(self):
        return self.__quarts

    def setQuarts(self,newQuarts):
        self.__quarts = newQuarts

    # increase and decrease quarts of blood by one
    def increaseQuarts(self):
        self.__quarts += 1

    def decreaseQuarts(self):
        self.__quarts -= 1















