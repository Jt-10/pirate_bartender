"""Pirate bartender creates a cocktail based on the answers to some
questions."""

import random

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? ",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

preferences = {}

adjectives = ["Arrogant","Bubbly","Comfortable","Dilicious","Earthy","Diabolical"]

nouns = ["Aardvark","Pomeranian","Chinchilla","Swimmer","Herb","Beach"]

drink = []

def obtain_preferences():
    """Gather customer responses to the questions and save them in the
    preferences dictionary."""
    
    for flavor in questions:
        preferences[flavor] = str(input(questions[flavor])).lower()
        if preferences[flavor] == "yes":
            preferences[flavor] = True
        elif preferences[flavor] == "y":
            preferences[flavor] = True
        else:
            preferences[flavor] = False
    
    return preferences
    
def pour(preferences):
    """Use the preferences and ingredients dictionaries to randomly select
    ingredients that correspond to flavors the customer enjoys."""
    
    for flavor in preferences:
        if preferences[flavor] == True:
            drink.append(random.choice(ingredients[flavor]))
    
    return drink

def main():
    """This function calls the obtain_preferences function and imports the
    preferences dictionary. Then it calls the pour function and imports 
    the drink list. Finally it prints the drink."""
    
    customer = "sober"
    
    while customer == "sober":
        obtain_preferences()
        pour(preferences)
    
        name = str(random.choice(adjectives)) + " " + str(random.choice(nouns))
        
        print(name)
        print(drink)
        
        sobriety = input("Would you like another beverage? ").lower()
        if sobriety == "no":
            customer = "drunk"
        elif sobriety == "n":
            customer = "drunk"
        else:
            pass
        
    
if __name__ == "__main__":
    main()
