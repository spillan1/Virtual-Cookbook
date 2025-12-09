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
    def __init__(self, master, cookbook):
        self.cookbook = cookbook

        self.window = tk.Toplevel(master)
        self.window.title("Add Recipe")
        self.window.geometry("500x750")

        tk.Label(self.window, text="Recipe Name:", font=("Helvetica", 12, "bold")).pack(pady=5)
        self.name_entry = tk.Entry(self.window, width=40)
        self.name_entry.pack(pady=5)

        tk.Label(self.window, text="Ingredients:", font=("Helvetica", 12, "bold")).pack(pady=5)

        tk.Label(self.window, text="Ingredient Name:").pack()
        self.ing_name_entry = tk.Entry(self.window)
        self.ing_name_entry.pack()

        tk.Label(self.window, text="Quantity:").pack()
        self.ing_qty_entry = tk.Entry(self.window)
        self.ing_qty_entry.pack()

        tk.Label(self.window, text="Unit:").pack()
        self.ing_unit_entry = tk.Entry(self.window)
        self.ing_unit_entry.pack()

        tk.Button(self.window,text="Add Ingredient",command=self.add_ingredient,bg="#FFFFFF",fg="black",font=("Helvetica", 12, "bold")).pack(pady=10)

        self.ingredients = {}
        self.ing_listbox = tk.Listbox(self.window, width=50, height=8)
        self.ing_listbox.pack(pady=10)

        tk.Label(self.window, text="Instructions:", font=("Helvetica", 12, "bold")).pack(pady=5)
        self.instructions_text = tk.Text(self.window, width=50, height=10)
        self.instructions_text.pack()

        #save recipe button
        self.save_button = tk.Button(self.window,text="Save Recipe",command=self.save_recipe,bg="#FFFFFF",fg="black",font=("Helvetica", 12, "bold"))
        self.save_button.pack(pady=15)

    def add_ingredient(self):
        name = self.ing_name_entry.get().strip().lower()
        qty_str = self.ing_qty_entry.get().strip()
        unit = self.ing_unit_entry.get().strip().lower()

        if not name or not qty_str or not unit:
            messagebox.showerror("Error", "Please fill all ingredient fields.")
            return

        try:
            qty = float(qty_str)
        except ValueError:
            messagebox.showerror("Error", "Quantity must be numeric.")
            return

        self.ingredients[name] = (qty, unit)
        self.ing_listbox.insert(tk.END, f"{name} — {qty} {unit}")

        self.ing_name_entry.delete(0, tk.END)
        self.ing_qty_entry.delete(0, tk.END)
        self.ing_unit_entry.delete(0, tk.END)

    def save_recipe(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Recipe must have a name.")
            return

        if not self.ingredients:
            messagebox.showerror("Error", "Add at least one ingredient.")
            return

        instructions = self.instructions_text.get("1.0", tk.END).strip()
        if not instructions:
            messagebox.showerror("Error", "Add instructions.")
            return

        recipe = Recipe(name,self.ingredients.copy(),instructions.split("\n"))

        self.cookbook.add_recipe(recipe)
        self.cookbook.save()

        messagebox.showinfo("Success", f"Recipe '{name}' saved.")
        self.window.destroy()
