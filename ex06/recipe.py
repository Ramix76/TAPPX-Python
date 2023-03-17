from multiprocessing.sharedctypes import Value
from pickle import TRUE
from secrets import choice
from socket import setdefaulttimeout
from typing import ItemsView, KeysView, ValuesView
from unicodedata import name


cookbook = {
    'Bocadillo': {
        'ingredients': ['jamon','queso','tomate'],
        'meal': 'almuerzo',
        'prep_time': 10
    },
    'Tarta': {
        'ingredients': ['harina','azucar','huevos'],
        'meal': 'postre',
        'prep_time': 60
    },
    'Ensalada': {
        'ingredients': ['aguacate','rucula','tomates','espinacas'],
        'meal': 'almuerzo',
        'prep_time': 15
    }
}

def menu():
    print("\nWelcome to the Python Cookbook !")
    print("List of available optopns: ")
    while TRUE:
        choice = input ("""
        1: Add a recipe
        2: Delete a recipe
        3: Print a recipe
        4: Print the cookbook
        5; Quit

        Please select an option: """)
    
        if choice == "1":
            enter_recipe()
        elif choice == "2":
            delete_recipe()
        elif choice == "3":
            print_details()
        elif choice == "4":
            print_recipe()
        elif choice == "5":
            quit()
        else:
            print("\nYou must select an option between 1-5")
            print("Please try again")

def print_recipe():
    print()
    [print(keys) for keys in cookbook]
      
def print_details():
    key = input("\nPlease enter a recie name to get its details:\n")
    print(f"\nRecipe for {key}:")
    print(f"  Ingredients list: {cookbook[key]['ingredients']}")
    print(f"  To be eaten for {cookbook[key]['meal']}")
    print(f"  Takes {cookbook[key]['prep_time']} minutes of cooking")

def delete_recipe():
    del_key = input("\nEnter recipe to delete:")
    cookbook.pop(del_key)

def enter_recipe():
    name = input("\nEnter recipe name: ")
    ing = input("Enter the ingredients: ").split(",")
    meal = input("Enter type of meal: ")
    time = input("Enter preparation time: ")
    cookbook[name] = {
        'ingredients': [],
        'meal': '',
        'prep_time': 0
    }
    cookbook[name]['ingredients'].append(ing)
    cookbook[name]['meal'] = meal
    cookbook[name]['prep_time'] = time

def quit():
    print('\nThanks for playins with us\n')
    exit()
      
__name__ == '__main__'
menu()
