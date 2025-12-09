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
        self.recipes = {}
        self.pantry = Pantry()
        
    def recipes_you_can_make(self):
        """Return a list of recipes that can be made with current ingredients."""
        can_make = []
        
        for name, recipe in self.recipes.items():
            if recipe.can_make(self.pantry):
                can_make.append(name)
        
        return can_make


    def add_recipe(self, recipe: Recipe):
        """Add a new recipe to the cookbook."""
        self.recipes[recipe.name] = recipe

    def remove_recipe(self, name: str):
        """Remove a recipe by from the cookbook."""
        if name in self.recipes:
            del self.recipes[name]

    def get_recipe(self, name: str):
        """Return a Recipe from the cookbook."""
        return self.recipes.get(name)
    
    def missing_for_recipe(self, recipe_name: str):
        """
        Return missing ingredients for a  recipe.

        Returns
        -------
        dict or None
        """
        recipe = self.recipes.get(recipe_name)
        if recipe is None:
            return None
        return recipe.missing_ingredients(self.pantry)
    
    def mark_cooked(self, recipe_name: str):
        """
        Subtract required ingredients from the pantry. Simulates the user cooking the recipe

        Parameters
        ----------
        recipe_name : str

        Raises
        ------
        ValueError if recipe does not exist or cannot be made.
        """
        recipe = self.recipes.get(recipe_name)
        if recipe is None:
            raise ValueError("Recipe not found.")

        if recipe.can_make(self.pantry) == False:
            raise ValueError("Not enough ingredients to cook this recipe.")

        for name, (quantity, unit) in recipe.ingredients.items():
            self.pantry.remove_ingredient(name, quantity)
            
    def save(self, filename="cookbook_data.json"):
        """Save recipes and pantry to a JSON file."""
        data = {"recipes": [r.to_dict() for r in self.recipes.values()],
            "pantry": self.pantry.to_dict()}

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self, filename="cookbook_data.json"):
        """Load recipes and pantry from a JSON file."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return  

        self.pantry = Pantry.from_dict(data["pantry"])

        self.recipes = {}
        for rdata in data["recipes"]:
            recipe = Recipe.from_dict(rdata)
            self.recipes[recipe.name] = recipe

if __name__ == "__main__":
    from recipe_define import Recipe

    print("Testing Cookbook")

    # Create cookbook
    cb = Cookbook()

    # Add pantry ingredients
    cb.pantry.add_ingredient("flour", 300, "g")
    cb.pantry.add_ingredient("eggs", 4, "count")

    # Create recipes
    pancake = Recipe(
        "Pancakes",
        {"flour": (150, "g"), "eggs": (2, "count"), "milk": (1, "cups")},
        ["Mix", "Cook"]
    )

    omelette = Recipe(
        "Omelette",
        {"eggs": (3, "count"), "milk": (0.25, "cups")},
        ["Beat eggs", "Cook in pan"]
    )

    cb.add_recipe(pancake)
    cb.add_recipe(omelette)

    print("Recipes you can make now:", cb.recipes_you_can_make())
    print("Missing for Pancakes:", cb.missing_for_recipe("Pancakes"))

    # Try to cook omelette
    try:
        cb.mark_cooked("Omelette")
        print("Cooked omelette")
    except ValueError as e:
        print("Cannot cook omelette:", e)

    print("Pantry after attempting:", cb.pantry.inventory)

    cb.pantry.add_ingredient("milk", 1, "cups")
    
    try:
        cb.mark_cooked("Omelette")
        print("Cooked omelette")
    except ValueError as e:
        print("Cannot cook omelette:", e)
     
    print("Pantry after 2nd attempt:", cb.pantry.inventory)
        
    # Save + Reload demo
    cb.save("test_cookbook.json")
    print("Saved cookbook.")

    new_cb = Cookbook()
    new_cb.load("test_cookbook.json")
    print("Loaded recipes:", list(new_cb.recipes.keys()))

    
    
