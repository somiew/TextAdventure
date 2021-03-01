# python 3.7

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
    zingo = liquid('Zingo', 'Yellow', True, False, False, 0)
    coke = liquid('Coca Cola', 'Brown', True, False, False, 0)
    norrlands = liquid('Norrlands Guld', 'Yellow', True, False, False, 18)
    milk = liquid('Milk', 'White', False, True, False, 0)
    oboy = liquid("O'boy", 'Brown', False, False, False, 0)
    coffe = liquid('Coffee', 'Brown', False, False, False, 0)
    posion = liquid('Poison', 'Green', False, False, True, 18)

    print('Welcome to Sams text based adventure game!')
    print("What's your name?")
    inputName = input()
    print("How old are you?")
    inputAge = input()
    player = person(inputName, inputAge)
    print("Hello " + player.name + ". Let's begin.")

    # while player.tries > 0:
    #     action = input()
    #     print('Your action was: ' + action)
    #     player.tries -= 1
