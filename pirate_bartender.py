"""Pirate bartender creates a cocktail based on the answers to some simple
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

def obtain_preferences():
    """Gather customer responses to the questions and save them in the
    preferences dictionary."""
    
    preferences = {}
    
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
    
    drink = []
    
    for flavor in preferences:
        if preferences[flavor] == True:
            drink.append(random.choice(ingredients[flavor]))
    
    return drink

def main(preferences, drink):
    """This function calls the obtain_preferences function and imports the
    preferences dictionary. Then it calls the pour function and imports 
    the drink list. Finally it prints the drink."""
    
    obtain_preferences()
    pour(preferences)
    
    print(drink)

if __name__=="__main__":
    main(obtain_preferences, pour)
