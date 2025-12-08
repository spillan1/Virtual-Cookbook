#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 15:05:20 2025

@author: shriya
"""
from pantry_define import Pantry

class Recipe:
    
    def __init__(self, name: str, ingredients: dict, instructions, tags=None):
        self.name = name.strip()
        self.ingredients = ingredients  
        self.instructions = instructions
        self.tags = tags or []
        
    def ingredients_required(self):
        """
        Return a dictionary of all required ingredients.

        Returns
        -------
        dict
            Keys: ingredient names
            Values: (quantity, unit)
        """
        return self.ingredients
    
    def missing_ingredients(self, pantry):
        """
        Compare this recipe's required ingredients with what is available 
        in the given Pantry an return a dictionary of missing ingredients.

        Parameters
        ----------
        pantry : Pantry
            The user's pantry.

        Returns
        -------
        dict
            Keys: ingredient names
            Values: (quantity_needed, unit)
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
        Check if all required ingredients are available in the pantry.

        Parameters
        ----------
        pantry : Pantry

        Returns
        -------
        bool
        """
        return len(self.missing_ingredients(pantry)) == 0
    
    def to_dict(self):
        """
        returne recipe as a dictionary
        
        Returns
        -------
        dict
        """
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "tags": self.tags
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a Recipe from a dictionary.

        Returns
        -------
        Recipe
        """
        return cls(
            data["name"],
            data["ingredients"],
            data["instructions"],
            data.get("tags", [])
        )
    
if __name__ == "__main__":
    print("Testing Recipe Class")

    p = Pantry()
    p.add_ingredient("flour", 200, "g")
    p.add_ingredient("eggs", 3, "count")

    pancake_recipe = Recipe("Pancakes",
        {"flour": (150, "g"),"eggs": (2, "count"),"milk": (1, "cups")},
        ["Mix ingredients", "Cook on skillet until golden brown"])

    print("Ingredients required:", pancake_recipe.ingredients_required())
    print("Missing ingredients:", pancake_recipe.missing_ingredients(p))
    print("Can make:", pancake_recipe.can_make(p))

