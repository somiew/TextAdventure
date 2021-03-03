# python 3.8.7
import objects
from random import randint

def game_over():
    print('-------------')
    print('--GAME OVER--')
    print('-------------')
    exit()


def valid_age():
    while True:
        try:
            inputAge = int(input('Age: '))
            if 0 < inputAge < 999:
                return inputAge
            elif inputAge > 999:
                print('Okay, I get it, you want to role play a certain age, but not even most Drow elves become older than 1000 years old')
            else:
                print('A VALID age that is... No commas, no negative numbers etc.')
        except:
            print('Invalid age, try writing it with numbers')


drink1 = objects.liquid('Zingo', 'Yellow', True, False, False, 0)
drink2 = objects.liquid('Coca Cola', 'Brown', True, False, False, 0)
drink3 = objects.liquid('Norrlands Guld', 'Yellow', True, False, False, 18)
drink4 = objects.liquid('Milk', 'White', False, True, False, 0)
drink5 = objects.liquid("O'boy", 'Brown', False, False, False, 0)
drink6 = objects.liquid('Coffee', 'Brown', False, False, False, 0)
drink7 = objects.liquid('Poison', 'Green', False, False, True, 18)

print('Welcome to Sams text based adventure game!')
print("What's your name?")
inputName = input('Name: ')
print("How old are you?")
inputAge = valid_age()
player = objects.person(inputName, inputAge)
print("Hello " + player.name + ". Let's begin.")

inventory = []

for i in range(0, 2):
    drinkNr = randint(1, 7)
    drink = 'drink'
    drink += str(drinkNr)
    inventory.append(drink)

print("As a little gift, you got two drinks in your inventory.")
print("To check your inventory, try to use the inventory action.")

while player.tries > 0:
    action = input('\nUse an action: ')
    if action == 'inventory':
        print('\n--INVENTORY--')
        for i in inventory:
            print(eval(i).name)
        print('-------------')

    for each in inventory:
        if action.lower() == 'drink ' + str(eval(each).name).lower():
            # check age restriction
            if eval(each).ageRestriction > player.age:
                print('You tried to drink ' + str(eval(each).name) + '...')
                print('But then you remembered the age restriction of ' + str(eval(each).ageRestriction) + 'years, and decided to skip it...')
                break
            
            print('You drank '+ str(eval(each).name))
            inventory.remove(each)
            
            # check if lethal
            if eval(each).lethal:
                print('AND DIED!')
                game_over()
            
            break

        if action.lower() == 'look at ' + str(eval(each).name).lower():
            print('You look at the '+ str(eval(each).name))
            if eval(each).sparkly:
                print('It is ' + eval(each).colour.lower() + ' and sparkly!')
            else:
                print('It is plain ' + eval(each).colour.lower())
            break

    player.tries -= 1
