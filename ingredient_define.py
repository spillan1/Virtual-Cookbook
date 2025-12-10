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
    
    def to_dict(self):
        return {"name": self.name,"unit": self.unit}
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Create an Ingredient object from a dictionary.
        
        Parameters
        ----------
        data : dict
           dictionary 

        Returns
        -------
        Ingredient
        """
        return cls(data["name"], data["unit"])

if __name__ == "__main__":
    #testing
    flour = Ingredient("  Flour", " g ")

    print(flour)                 
    print(flour.name)                  
    print(flour.unit)                  

    flour_dict = flour.to_dict()
    print(flour_dict)               

    flour_copy = Ingredient.from_dict(flour_dict)
    print(flour_copy)  

    print(flour_copy.name == flour.name)   
    print(flour_copy.unit == flour.unit)   



