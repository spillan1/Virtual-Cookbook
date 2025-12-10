#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 16:08:50 2025

@author: shriya
"""
import tkinter as tk
from tkinter import ttk, messagebox


class RecipeListWindow:
    """defines a RecipeListWindow class"""
    def __init__(self, master, cookbook):
        self.cookbook = cookbook
        self.window = tk.Toplevel(master)
        self.window.title("Recipes")
        self.window.geometry("500x600")
        self.recipelist = tk.Listbox(self.window, width=40, height=15)
        self.recipelist.pack(pady=10)
        self.load_recipe_names()

        #3 buttons in this window
        tk.Button(self.window, text="View Recipe", command=self.view_recipe).pack(pady=5)
        tk.Button(self.window, text="Cook Recipe", command=self.cook_recipe, bg="#FFFFFF", fg="black").pack(pady=5)
        tk.Button(self.window,text="Delete Recipe",command=self.delete_recipe,bg="#FFFFFF",fg="black").pack(pady=5)

        self.frame = tk.Frame(self.window)
        self.frame.pack(pady=15)
        self.rtext = tk.Text(self.frame, width=55, height=15)
        self.rtext.pack()


    def load_recipe_names(self):
        '''
        loads recipes stored in cookbook. recipes are displayed in top box

        Returns
        -------
        None.

        '''
        self.recipelist.delete(0, tk.END) 
        for name in self.cookbook.recipes:
            self.recipelist.insert(tk.END, name)

    def view_recipe(self):
        """
        shows selected recipe info in bottom box (ingredients, instructions, and missing ingredients)

        Returns
        -------
        None.

        """
        #selection from top box
        selection = self.recipelist.curselection()
        recipe_name = self.recipelist.get(selection[0])
        recipe = self.cookbook.get_recipe(recipe_name)

        self.rtext.delete("1.0", tk.END)

        #recipe details output in lower box
        self.rtext.insert(tk.END, f"{recipe.name}\n\n")
        self.rtext.insert(tk.END, "Ingredients Required:\n")
        for ing, (qty, unit) in recipe.ingredients.items():
            self.rtext.insert(tk.END, f" - {ing}: {qty} {unit}\n")
        #if any missing ingredients
        missing = recipe.missing_ingredients(self.cookbook.pantry)
        self.rtext.insert(tk.END, "\nMissing Ingredients:\n")
        if missing:
            for ing, (qty, unit) in missing.items():
                self.rtext.insert(tk.END, f" - {ing}: need {qty} {unit} more\n")
        else:
            self.rtext.insert(tk.END, "None\n")

        self.rtext.insert(tk.END, "\nInstructions:\n")
        if isinstance(recipe.instructions, list):
            for step in recipe.instructions:
                self.rtext.insert(tk.END, f" - {step}\n")
        else:
            self.rtext.insert(tk.END, recipe.instructions)


    def cook_recipe(self):
        '''
        deletes required ingredientsa from the pantry to simulate cooking the recipe

        Returns
        -------
        None.

        '''
        selection = self.recipelist.curselection()
        recipe_name = self.recipelist.get(selection[0])
        recipe = self.cookbook.get_recipe(recipe_name)

        if not recipe.can_make(self.cookbook.pantry):
            missing = recipe.missing_ingredients(self.cookbook.pantry)
            msg = "You cannot make this recipe.\nMissing:\n"
            for ing, (qty, unit) in missing.items():
                msg += f" - {ing}: {qty} {unit} more\n"
            messagebox.showerror("Not enough ingredients", msg)
            return


        try:
            self.cookbook.mark_cooked(recipe_name)
            self.cookbook.save()
            self.view_recipe()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            
    def delete_recipe(self):
        '''
        removes a recipe from the cookbook

        Returns
        -------
        None.

        '''
        selection = self.recipelist.curselection()
        recipe_name = self.recipelist.get(selection[0])

        if recipe_name in self.cookbook.recipes:
           del self.cookbook.recipes[recipe_name]
           
        self.cookbook.save()
        self.load_recipe_names()
        self.rtext.delete("1.0", tk.END)



