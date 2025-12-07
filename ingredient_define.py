#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 15:12:17 2025

@author: shriya
"""

class Ingredient:
    def __init__(self, name: str, unit: str):
        self.name = name.lower().strip()
        self.unit = unit.lower().strip()

    def __str__(self):
        return f"{self.name} ({self.unit})"
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "unit": self.unit
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Create an Ingredient instance from a dictionary.
        
        Parameters
        ----------
        data : dict
            A dictionary containing 'name' and 'unit' keys.

        Returns
        -------
        Ingredient
        """
        return cls(data["name"], data["unit"])

if __name__ == "__main__":
    # Test the Ingredient class functionality

    print("Testing Ingredient Class")

    flour = Ingredient("  Flour  ", " g ")

    print("Ingredient:", flour)                 
    print("Name:", flour.name)                  
    print("Unit:", flour.unit)                  

    flour_dict = flour.to_dict()
    print("As dict:", flour_dict)               

    flour_copy = Ingredient.from_dict(flour_dict)
    print("Recreated Ingredient:", flour_copy)  

    print("Name matches:", flour_copy.name == flour.name)   
    print("Unit matches:", flour_copy.unit == flour.unit)   



