"""
Sandwich Maker
Write a program that asks users for their sandwich preferences.
The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their
selection.
"""


import pyinputplus as pyip


def make_sandwich():
    menu = {
        'breads': {'wheat': 7, 'white': 6, 'sourdough': 8},
        'proteins': {'chicken': 5, 'turkey': 6, 'ham': 7, 'tofu': 6.50},
        'cheeses': {'cheddar': 2, 'Swiss': 3, 'mozzarella': 2.50},
        'toppings': {'mayo': 1, 'mustard': 1, 'lettuce': 2, 'tomato': 2}
    }

    bread = pyip.inputMenu(list(menu['breads'].keys()), lettered=True, limit=2)
    protein = pyip.inputMenu(list(menu['proteins'].keys()), lettered=True, limit=2)
    with_cheese = pyip.inputYesNo('Cheese? > ', limit=2)
    cheese = None
    if with_cheese == 'yes':
        cheese = pyip.inputMenu(list(menu['cheeses'].keys()), lettered=True, limit=2)
    mayo = pyip.inputYesNo('Mayo? > ', limit=2)
    mustard = pyip.inputYesNo('Mustard? > ', limit=2)
    lettuce = pyip.inputYesNo('Lettuce? > ', limit=2)
    tomato = pyip.inputYesNo('Tomato? > ', limit=2)

    price = (menu['breads'][bread] +
             menu['proteins'][protein] +
             (menu['cheeses'][cheese] if cheese else 0) +
             (menu['toppings']['mayo'] if mayo else 0) +
             (menu['toppings']['mustard'] if mustard else 0) +
             (menu['toppings']['lettuce'] if lettuce else 0) +
             (menu['toppings']['tomato'] if tomato else 0))

    return f'Your total will be ${price}'


print(make_sandwich())
