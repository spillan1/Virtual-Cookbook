#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 21:56:57 2025

@author: shriya
"""

import pytest
from recipe_define import Recipe
from pantry_define import Pantry

'''tests the functions in the Recipe class'''

def test_ingredients_required():
    '''tests ingredients_required function'''
    r = Recipe("test", {"eggs": (12, "count")}, "test recipe")
    required = r.ingredients_required()
    assert required == {"eggs": (12, "count")}
    
def test_missing_ingredients():
    '''tests missing_ingredients function'''
    r = Recipe("test", {"eggs": (12, "count")}, "test recipe")
    p = Pantry()
    missing = r.missing_ingredients(p)
    assert missing == {"eggs": (12, "count")}

def test_can_make():
    '''tests that a recipe can determine if it can be mnade with pantry ingredients'''
    r = Recipe("test", {"eggs": (12, "count")}, "test recipe")
    p = Pantry()
    p.add_ingredient('eggs', 12, 'count')
    can = r.can_make(p)
    assert can == True
    
    
    