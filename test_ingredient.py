#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 21:25:03 2025

@author: shriya
"""
import pytest
from ingredient_define import Ingredient

def test_create_ingredient():
    sugar = Ingredient(name="Sugar", unit="cups")
    assert sugar.name == "sugar"
    assert sugar.unit == "cups"


