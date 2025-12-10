#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 15:40:24 2025

@author: shriya
"""

class Pantry:
    "defines a Pantry class"
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
                raise ValueError(f"Unit mismatch")
            
            self.inventory[name] = (existing_quantity + quantity, unit)
        else:
            self.inventory[name] = (quantity, unit)

    def remove_ingredient(self, name: str, num_to_remove: float):
        """
        Removes a quantity of an ingredient.

        Parameters
        ----------
        name : str
            Ingredient name.
        num_to_remove : float
            Amount to subtract.

        Raises
        ------
        ValueError
            ingredient does not exist or not enough.
        """

        if name not in self.inventory:
            raise ValueError(f"{name} is not in the pantry.")

        current_quantity, unit = self.inventory[name]

        if num_to_remove > current_quantity:
            raise ValueError(f"Not enough {name} in pantry")

        new_quantity = current_quantity - num_to_remove
        if new_quantity <= 0:
            del self.inventory[name]
        else:
            self.inventory[name] = (new_quantity, unit)



    def has_ingredient(self, name: str, num_needed: float, units: str):
        """
        Check if enough ingredient is availible.

        Parameters
        ----------
        name : str
            Ingredient name
        num_needed : float
            Amount needed
        units : str
            units 

        Returns
        -------
        bool
        """
        if name not in self.inventory:
            return False
        c_amount, pantry_unit = self.inventory[name]
        if pantry_unit != units:
            return False
        return c_amount >= num_needed

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
    pass
