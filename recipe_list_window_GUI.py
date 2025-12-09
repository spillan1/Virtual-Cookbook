#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 16:08:50 2025

@author: shriya
"""
import tkinter as tk
from tkinter import ttk, messagebox


class RecipeListWindow:
    def __init__(self, master, cookbook):
        self.cookbook = cookbook

        self.window = tk.Toplevel(master)
        self.window.title("Recipes")
        self.window.geometry("500x600")

        tk.Label(self.window, text="All Recipes", font=("Helvetica", 14, "bold")).pack(pady=10)

        self.recipe_listbox = tk.Listbox(self.window, width=40, height=15)
        self.recipe_listbox.pack(pady=10)

        self.load_recipe_names()

        tk.Button(self.window, text="View Recipe", command=self.view_recipe).pack(pady=5)

        tk.Button(self.window, text="Cook Recipe", command=self.cook_recipe, bg="#FFFFFF", fg="black").pack(pady=5)
        
        tk.Button(self.window,text="Delete Recipe",command=self.delete_recipe,bg="#FFFFFF",fg="black").pack(pady=5)

        self.details_frame = tk.Frame(self.window)
        self.details_frame.pack(pady=15)

        self.details_text = tk.Text(self.details_frame, width=55, height=15)
        self.details_text.pack()


    def load_recipe_names(self):
        self.recipe_listbox.delete(0, tk.END) 
        for name in self.cookbook.recipes:
            self.recipe_listbox.insert(tk.END, name)

    def view_recipe(self):
        selection = self.recipe_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a recipe.")
            return

        recipe_name = self.recipe_listbox.get(selection[0])
        recipe = self.cookbook.get_recipe(recipe_name)

        self.details_text.delete("1.0", tk.END)

        self.details_text.insert(tk.END, f"{recipe.name}\n\n")
        self.details_text.insert(tk.END, "Ingredients Required:\n")
        for ing, (qty, unit) in recipe.ingredients.items():
            self.details_text.insert(tk.END, f" - {ing}: {qty} {unit}\n")

        missing = recipe.missing_ingredients(self.cookbook.pantry)
        self.details_text.insert(tk.END, "\nMissing Ingredients:\n")
        if missing:
            for ing, (qty, unit) in missing.items():
                self.details_text.insert(tk.END, f" - {ing}: need {qty} {unit} more\n")
        else:
            self.details_text.insert(tk.END, "None\n")

        self.details_text.insert(tk.END, "\nInstructions:\n")
        if isinstance(recipe.instructions, list):
            for step in recipe.instructions:
                self.details_text.insert(tk.END, f" - {step}\n")
        else:
            self.details_text.insert(tk.END, recipe.instructions)


    def cook_recipe(self):
        selection = self.recipe_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a recipe.")
            return

        recipe_name = self.recipe_listbox.get(selection[0])
        recipe = self.cookbook.get_recipe(recipe_name)

        if not recipe.can_make(self.cookbook.pantry):
            missing = recipe.missing_ingredients(self.cookbook.pantry)
            msg = "You cannot make this recipe.\nMissing:\n"
            for ing, (qty, unit) in missing.items():
                msg += f" - {ing}: {qty} {unit} more\n"
            messagebox.showerror("Not enough ingredients", msg)
            return

        confirm = messagebox.askyesno("Cook Recipe", f"Are you sure you want to cook '{recipe_name}'?")
        if not confirm:
            return

        try:
            self.cookbook.mark_cooked(recipe_name)
            self.cookbook.save()
            messagebox.showinfo("Success", f"You cooked '{recipe_name}'")

            self.view_recipe()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            
    def delete_recipe(self):
        selection = self.recipe_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a recipe to delete.")
            return

        recipe_name = self.recipe_listbox.get(selection[0])

        confirm = messagebox.askyesno("Delete Recipe",
                                  f"Are you sure you want to delete '{recipe_name}'?")
        if not confirm:
            return

        if recipe_name in self.cookbook.recipes:
           del self.cookbook.recipes[recipe_name]

        self.cookbook.save()
        self.load_recipe_names()

        self.details_text.delete("1.0", tk.END)

        messagebox.showinfo("Deleted", f"Recipe '{recipe_name}' has been deleted.")


