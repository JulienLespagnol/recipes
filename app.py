import csv
from inspect import currentframe

from numpy import rec

class Ingredient:
        def __init__(self, name:str, quantite:float, unite:str) :
            self._name = name
            self._quantite = quantite
            self._unite = unite

        def __str__(self):
            s = self._name + " : " + str(self._quantite) + " " + self._unite
            return s

class Recipe:
    def __init__(self, name:str):
        self._name = name
        self.ingredients = []
    
    def AddIngredient(self, ingredient:str, quantite:float, unite:str):
        self.ingredients.append(Ingredient(ingredient, quantite, unite))

    def __str__(self) :
        s = self._name + ":\n"
        for ingredient in self.ingredients:
            s += "\t" + str(ingredient) + "\n"

        return s


print("Hello World !")
file = open('recipes.csv', mode='r')

rcsv = csv.DictReader(file)
recipes = []

line_count = 0
lastPlat = ""
currRecipe = None
for row in rcsv:
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1

    if row['Plats'] != lastPlat:
        if lastPlat != "":
            recipes.append(currRecipe)
        
        currRecipe = Recipe(row['Plats'])
        currRecipe.AddIngredient(row["Ingredient"], float(row["Quantite"]), row["Unite"])
        lastPlat = row['Plats']
    else:
        currRecipe.AddIngredient(row["Ingredient"], float(row["Quantite"]), row["Unite"])

recipes.append(currRecipe)

for recipe in recipes:
    print(str(recipe))

