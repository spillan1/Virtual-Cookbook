#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 15:05:20 2025

@author: shriya
"""
from pantry_define import Pantry

class Recipe:
    "defines a Recipe class"
    
    def __init__(self, name: str, ingredients: dict, instructions):
        self.name = name.strip()
        self.ingredients = ingredients  
        self.instructions = instructions
        
    def ingredients_required(self):
        """
        Return a dictionary of all required ingredients.

        Returns
        -------
        dict
            Keys: ingredient name
            Values: (quantity, unit)
        """
        return self.ingredients
    
    def missing_ingredients(self, pantry):
        """
        returns the ingredients missing from the pantry that are required to make this
        Parameters
        ----------
        pantry : Pantry
            The user's pantry.

        Returns
        -------
        dict
            Keys: ingredient names
            Values: (amount needed, unit)
        """
        missing = {}

        for name, (req_quantity, req_unit) in self.ingredients.items():
            if pantry.has_ingredient(name, req_quantity, req_unit) == False:
                # missing ingredient
                if name not in pantry.inventory:
                    missing[name] = (req_quantity, req_unit)
                else:
                    # not enough
                    available_quantity, _ = pantry.inventory[name]
                    missing_quantity = req_quantity - available_quantity
                    if missing_quantity > 0:
                        missing[name] = (missing_quantity, req_unit)

        return missing
    
    def can_make(self, pantry):
        """
        check if all required ingredients are available in the pantry

        Parameters
        ----------
        pantry : Pantry

        Returns
        -------
        bool
        """
        missing = len(self.missing_ingredients(pantry))
        if missing == 0:
            return True
        else:
            return False
    
    def to_dict(self):
        """
        returne recipe as a dictionary
        
        Returns
        -------
        dict
        """
        return {"name": self.name,"ingredients": self.ingredients,"instructions": self.instructions}
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        create a Recipe from a dictionary

        Returns
        -------
        Recipe
        """
        return cls(data["name"],data["ingredients"],data["instructions"])
    
if __name__ == "__main__":
    #testing

    p = Pantry()
    p.add_ingredient("flour", 200, "g")
    p.add_ingredient("eggs", 3, "count")

    pancake_recipe = Recipe("Pancakes",{"flour": (150, "g"),"eggs": (2, "count"),"milk": (1, "cups")},["Mix ingredients", "Cook on skillet until golden brown"])

    print(pancake_recipe.ingredients_required())
    print(pancake_recipe.missing_ingredients(p))
    print(pancake_recipe.can_make(p))

