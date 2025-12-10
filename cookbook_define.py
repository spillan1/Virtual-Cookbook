#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 19:45:19 2025

@author: shriya
"""
import json
from recipe_define import Recipe
from pantry_define import Pantry


class Cookbook:

    def __init__(self):
        self.recipes ={}     
        self.pantry = Pantry()

    def can_make(self):
        '''
        determines the recipes can be made with the ingredients availible in pantry

        Returns
        -------
        canmake : list
            list of recipes that can be made.

        '''
        canmake = []
        for name,recipe in self.recipes.items():
            if recipe.can_make(self.pantry):
                canmake.append(name)
        return canmake

    def add_recipe(self, recipe):
        '''
        adds a recipe to the cookbook

        Parameters
        ----------
        recipe : Recipe
            recipe entered by user.

        Returns
        -------
        None.

        '''
        self.recipes[recipe.name] = recipe
    
    def remove_recipe(self, name: str):
        """
        removes a recipe from the cookbook

        Parameters
        ----------
        name : str
            recipe name.

        Returns
        -------
        None.

        """
        if name in self.recipes:
            del self.recipes[name]
            
    def get_recipe(self, name: str):
        """
        returns a recipe

        Parameters
        ----------
        name : str
            name of the recipe to be returned.

        Returns
        -------
        Recipe
            DESCRIPTION.

        """
        return self.recipes.get(name)
    
    def missing_for_recipe(self, recipe_name: str):
        """
        returns the ingredients missing from the pantry to make the recips

        Parameters
        ----------
        recipe_name : str
            name of recipe.

        Returns
        -------
        dict
            Keys: ingredient names
            Values: (amount needed, unit)

        """
        recipe = self.recipes.get(recipe_name)
        if recipe is None:
            return None
        return recipe.missing_ingredients(self.pantry)

    def mark_cooked(self, name):
        """
        simulates a recipe being cooked by removing items from pantry

        Parameters
        ----------
        name : str
            name of recipe cooked.

        Raises
        ------
        ValueError
            DESCRIPTION.

        Returns
        -------
        None.

        """
        recipe = self.recipes.get(name)

        if recipe is None:
            raise ValueError("Recipe not found")

        if recipe.can_make(self.pantry) ==False:
            raise ValueError("Not enough ingredients")

        for ing,(amount, unit) in recipe.ingredients.items():
            self.pantry.remove_ingredient(ing, amount)

    def save(self, filename="cookbook_data.json"):
        """
        saves cookbook data in a JSON file 

        Parameters
        ----------
        filename : TYPE, optional
            DESCRIPTION. The default is "cookbook_data.json".

        Returns
        -------
        None.

        """
        data = {"recipes": [r.to_dict() for r in self.recipes.values()],"pantry": self.pantry.to_dict()}

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    def load(self,filename="cookbook_data.json"):
        """
        loads cookbook data from the JSON FILE

        Parameters
        ----------
        filename : TYPE, optional
            DESCRIPTION. The default is "cookbook_data.json".

        Returns
        -------
        None.

        """
        try:
            with open(filename) as f:
                data = json.load(f)
        except FileNotFoundError:
            return

        self.pantry = Pantry.from_dict(data["pantry"])
        self.recipes = {}
        for recipedata in data["recipes"]:
            r = Recipe.from_dict(recipedata)
            self.recipes[r.name] = r
