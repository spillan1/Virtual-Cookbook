#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 15:40:24 2025

@author: shriya
"""

class Pantry:

    def __init__(self):
        self.inventory = {}

    def add_ingredient(self, name: str, quantity: float, unit: str):
        """
        Add an ingredient to the pantry or updates its amount.

        Parameters
        ----------
        name : str
            Ingredient name.
        quantity : float
            Amount to add.
        unit : str
            Unit for the ingredient (must match if ingredient already exists).
        """
        name = name.lower().strip()
        unit = unit.lower().strip()

        if name in self.inventory:
            existing_quantity, existing_unit = self.inventory[name]
            
            if existing_unit != unit:
                raise ValueError(f"Unit mismatch for {name}: '{existing_unit}' vs '{unit}'")
            
            self.inventory[name] = (existing_quantity + quantity, unit)
        else:
            self.inventory[name] = (quantity, unit)

    def remove_ingredient(self, name: str, quantity: float):
        """
        Removes a quantity of an ingredient.

        Parameters
        ----------
        name : str
            Ingredient name.
        quantity : float
            Amount to subtract.

        Raises
        ------
        ValueError
            If the ingredient does not exist or the quantity is insufficient.
        """
        name = name.lower().strip()

        if name not in self.inventory:
            raise ValueError(f"{name} is not in the pantry.")

        current_quantity, unit = self.inventory[name]

        if quantity > current_quantity:
            raise ValueError(f"Not enough {name} in pantry. Have {current_quantity}, need {quantity}.")

        new_quantity = current_quantity - quantity
        if new_quantity <= 0:
            del self.inventory[name]
        else:
            self.inventory[name] = (new_quantity, unit)

    def has_ingredient(self, name: str, req_quantity: float, req_unit: str):
        """
        Check if enough ingredient is availible.

        Parameters
        ----------
        name : str
            Ingredient name.
        req_quantity : float
            Amount needed.
        req_unit : str
            Unit required (must match pantry unit)

        Returns
        -------
        bool
        """
        name = name.lower().strip()
        req_unit = req_unit.lower().strip()

        if name not in self.inventory:
            return False

        pantry_quantity, pantry_unit = self.inventory[name]


        if pantry_unit != req_unit:
            return False

        return pantry_quantity >= req_quantity

    def to_dict(self):
        """Return inventory as a dictionary."""
        return self.inventory.copy()

    @classmethod
    def from_dict(cls, data: dict):
        """Load a pantry from a dictionary."""
        p = cls()
        p.inventory = data
        return p
    
    
if __name__ == "__main__":
    print("Testing Pantry")

    p = Pantry()
    p.add_ingredient("Flour", 500, "g")
    p.add_ingredient("eggs", 6, "count")
    p.add_ingredient("milk", 2, "cups")

    print("Pantry:", p.inventory)

    print("Has flour 100 g:", p.has_ingredient("flour", 100, "g"))
    print("Has milk 3 cups:", p.has_ingredient("milk", 3, "cups"))

    p.remove_ingredient("eggs", 2)
    print("After using 2 eggs:", p.inventory)

