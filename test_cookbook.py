#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 22:11:18 2025

@author: shriya
"""
import pytest
from cookbook_define import Cookbook
from recipe_define import Recipe
from pantry_define import Pantry

def test_remove_recipe():
    """tests deleting a recipe from the cookbook"""
    c = Cookbook()
    r = Recipe("test", {"eggs": (12, "count")}, "test recipe")
    c.add_recipe(r)
    c.remove_recipe("test")
    assert c.recipes == {}

def test_can_make():
    """tests if the cookbook can generate a list of recipes that can be made with current ingredients"""
    c = Cookbook()
    r = Recipe("test", {"eggs": (12, "count")}, "test recipe")
    c.add_recipe(r)
    c.pantry.add_ingredient('eggs', 12, 'count')
    assert c.can_make() == ["test"]
    
def test_mark_cooked():
    """tests if the cookbook can simulate cooking a recipe"""
    c = Cookbook()
    r = Recipe("test", {"eggs": (12, "count")}, "test recipe")
    c.add_recipe(r)
    c.pantry.add_ingredient('eggs', 12, 'count')
    c.mark_cooked("test")
    assert c.pantry.inventory == {}

def test_missing_for_recipe():
    '''tests if the cookbook can determine which ingredients are missing for the recipe'''
    c = Cookbook()
    r = Recipe("test", {"eggs": (12, "count")}, "test recipe")
    c.add_recipe(r)
    missing = c.missing_for_recipe("test")
    assert missing == {"eggs": (12, "count")}