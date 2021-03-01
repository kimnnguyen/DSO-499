from Human import Human
from Vampire import Vampire

def printHumans(humanList):
    print("----------------------------------------------")
    listLength = len(humanList) #contains a LIST of all the indices of the humans.
    for num in range(listLength):
        print(num, ")", humanList[num]) #humanList[num] is the human with the correspinding index
    print("----------------------------------------------")


def performdFeeding(humanList, vamp):
    humanIndex = int(input("Please select a human from the list: "))
    listLength = len(humanList)
    # used for error checking
    possibleValues = list(range(listLength)) # list of INTEGERS(the indices for how many humans are in the List)

    # error checking
    while humanIndex not in possibleValues:
        print("Invalid input. Please try again. ")
        humanIndex = input("Please select a human from the list: ")
    human = humanList[humanIndex]
    # determine if the vampire is able to suck blood from human
    # human cannot have less than 0 quarts of blood and vampire can't have more than 5 quarts of blood
    if human.isAlive() == False:
        print(human)
        print(human.getName(), "is dead! Cannot suck blood.")
    if vamp.isStuffed() == True:
        print(vamp, vamp.getName(), "can not suck any more blood.") # printing out vamp prints out the status of the vamp.
    elif human.getQuarts() > 0 and vamp.isStuffed() == False:
        vamp.suckBlood(human)
        print(human)
        print(vamp)



def main():

    # display menu
    print("Menu: ")
    print("1) Print all humans")
    print("2) Suck Blood")
    print("-1) quit")

    option = input("Please select an option from the menu: ")
    # error checking
    possibleSelections = ["1","2","-1"]
    while option not in possibleSelections:
        print("Invalid input. Please try again.")
        option = input("Please select an option from the menu: ")
    # Option1: print all humans
    if option == "1":
        printHumans(humanList)
    # Option 2: Vampire sucks blood.
    elif option == "2":
        printHumans(humanList)
        performdFeeding(humanList,vamp)
    # Option 3: vampire turns back into animal and program ends
    elif option == "-1":
        print(vamp.getName(), "turned back into a", vamp.getAnimalForm())
        quit()

# creating 4 humans and putting them into a list
Alice = Human("Alice",10,"A+")
Jerry = Human("Jerry", 3,"B+")
Tom = Human("Tom", 5, "O")
Mary = Human("Mary", 8, "A-")
humanList = [Alice, Jerry, Tom, Mary]
# ask user for vampire name and animal form
vampName = input("Enter the name of the vampire: ").title()
animal = input("Enter an animal: ")
#create vampire
vamp = Vampire(vampName, 0, animal)
while True:
    main()
