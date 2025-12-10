#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 16:07:18 2025

@author: shriya
"""
import tkinter as tk
from tkinter import ttk, messagebox
from recipe_define import Recipe


class AddRecipeWindow:
    '''defines a RecipeWindow class'''
    def __init__(self, master, cookbook):
        self.cookbook = cookbook

        self.window = tk.Toplevel(master)
        self.window.title("Add Recipe")
        self.window.geometry("500x750")

        tk.Label(self.window, text="Recipe Name:", font=("Helvetica", 12, "bold")).pack(pady=5)
        self.recipe_entry = tk.Entry(self.window)
        self.recipe_entry.pack(pady=5)

        tk.Label(self.window, text="Ingredients:", font=("Helvetica", 12, "bold")).pack(pady=5)

        tk.Label(self.window, text="Ingredient Name:").pack()
        self.ingredient_enter = tk.Entry(self.window)
        self.ingredient_enter.pack()
        tk.Label(self.window, text='Quantity:').pack()
        self.amount_entry = tk.Entry(self.window)
        self.amount_entry.pack()

        tk.Label(self.window, text="Unit:").pack()
        self.unit_entry = tk.Entry(self.window)
        self.unit_entry.pack()

        tk.Button(self.window,text="Add Ingredient",bg="#FFFFFF",fg="black",command=self.add_ingredient,font=("Helvetica", 12, "bold")).pack(pady=10)

        #creats textboox that stores entered ingredients
        self.ingredients = {}
        self.ingredient_textbox = tk.Listbox(self.window, width=50, height=8)
        self.ingredient_textbox.pack(pady=10)

        #creates textbox to enter instructions
        tk.Label(self.window, text="Instructions:", font=("Helvetica", 12, "bold")).pack(pady=5)
        self.instructions_text = tk.Text(self.window, width=50, height=10)
        self.instructions_text.pack()

        #save recipe button
        self.save_button = tk.Button(self.window,text="Save Recipe",command=self.save_recipe,bg="#FFFFFF",fg="black",font=("Helvetica", 12, "bold"))
        self.save_button.pack(pady=15)

    def add_ingredient(self):
        '''
        add an ingredient needed for the recipe to recipe info

        Returns
        -------
        None.

        '''
        name = self.ingredient_enter.get().strip().lower()
        qty_str = self.amount_entry.get().strip()
        unit = self.unit_entry.get().strip().lower()

        if not name or not qty_str or not unit:
            messagebox.showerror("Error", "fill all ingredient fields.")
            return

        try:
            qty = float(qty_str)
        except ValueError:
            messagebox.showerror("Error", "enter a number.")
            return

        self.ingredients[name] = (qty, unit)
        self.ingredient_textbox.insert(tk.END, f"{name} — {qty} {unit}")
        self.ingredient_enter.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.unit_entry.delete(0, tk.END)

    def save_recipe(self):
        """
        saves the recipe to the cookbook

        Returns
        -------
        None.

        """
        name = self.recipe_entry.get()
        if not name:
            messagebox.showerror("Error", "enter recipe name.")
            return

        if not self.ingredients:
            messagebox.showerror("Error", "Add ingredient(s).")
            return

        instructions = self.instructions_text.get("1.0", tk.END).strip()
        if not instructions:
            messagebox.showerror("Error", "Add instructions.")
            return

        recipe = Recipe(name,self.ingredients.copy(),instructions.split("\n"))

        self.cookbook.add_recipe(recipe)
        self.cookbook.save()
        self.window.destroy()
