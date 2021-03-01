# python 3.7
from random import randint

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tries = 5

class liquid:
    def __init__(self, nameStr, colourStr, sparklyBool, healthyBool, lethalBool, ageRestrictionInt):
        self.name = nameStr
        self.colour = colourStr
        self.sparkly = sparklyBool
        self.healthy = healthyBool
        self.lethal = lethalBool
        self.ageRestriction = ageRestrictionInt


if __name__ == '__main__':
    drink1 = liquid('Zingo', 'Yellow', True, False, False, 0)
    drink2 = liquid('Coca Cola', 'Brown', True, False, False, 0)
    drink3 = liquid('Norrlands Guld', 'Yellow', True, False, False, 18)
    drink4 = liquid('Milk', 'White', False, True, False, 0)
    drink5 = liquid("O'boy", 'Brown', False, False, False, 0)
    drink6 = liquid('Coffee', 'Brown', False, False, False, 0)
    drink7 = liquid('Poison', 'Green', False, False, True, 18)

    print('Welcome to Sams text based adventure game!')
    print("What's your name?")
    inputName = input()
    print("How old are you?")
    inputAge = input()
    player = person(inputName, inputAge)
    print("Hello " + player.name + ". Let's begin.")

    inventory = []

    for i in range(0, 2):
        drinkNr = randint(1, 7)
        drink = 'drink'
        drink += str(drinkNr)
        inventory.append(eval(drink).name)

    print("As a little gift, you got two drinks in your inventory.")
    print("To check your inventory, try to use the inventory action.")

    while player.tries > 0:
        action = input('Use an action: ')
        if action == 'inventory':
            print('\n--INVENTORY--')
            for i in inventory:
                print(i)
            print('-------------')
        player.tries -= 1
