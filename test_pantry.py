#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 21:36:29 2025

@author: shriya
"""
import pytest
from pantry_define import Pantry
from ingredient_define import Ingredient
from recipe_define import Recipe

'''unit tests for Pantry class'''

def test_add_ingredient():
    """testn adding a new ingredient to the pantry"""
    p = Pantry()
    p.add_ingredient("eggs", 12, "count")
    assert "eggs" in p.inventory
    assert p.inventory["eggs"][0] == 12


def test_add_ingredient_already_in_pantry():
    """testing that the amount of an ingredient updates if it is already in the pantry."""
    p = Pantry()
    p.add_ingredient("eggs", 12, "count")
    p.add_ingredient("eggs", 1, 'count')
    assert p.inventory["eggs"][0] == 13
    
def test_remove_ingredient():
    """testn removing a new ingredient to the pantry"""
    p = Pantry()
    p.add_ingredient("eggs", 12, "count")
    p.remove_ingredient("eggs", 1)
    assert p.inventory["eggs"][0] == 11


def test_has_ingredient():
    """testing if an ingredient is in the pantry or not"""
    p = Pantry()
    p.add_ingredient("eggs", 12, "count")
    
    #testing if the ingredient is in the pantry
    assert p.has_ingredient('eggs', 2, 'count') == True
    
    #testing if the ingredient is not in pantry'
    assert p.has_ingredient('milk', 2, 'cups') == False
