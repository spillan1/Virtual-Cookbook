#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 15:48:32 2025

@author: shriya
"""
import tkinter as tk
from tkinter import ttk, messagebox


class PantryWindow:
    def __init__(self, master, cookbook):
        self.cookbook = cookbook

        self.window = tk.Toplevel(master)
        self.window.title("Pantry")
        self.window.geometry("400x550")

        #pantry display
        self.tree = ttk.Treeview(self.window,columns=("quantity", "unit"), show="headings")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("unit", text="Unit")
        self.tree.pack(fill="both", expand=True, pady=10)

        self.load_pantry()

        #ingredients section
        tk.Label(self.window, text="Add Ingredient", font=("Helvetica", 12, "bold")).pack(pady=5)

        tk.Label(self.window, text="Ingredient Name:").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        tk.Label(self.window, text="Quantity:").pack()
        self.qty_entry = tk.Entry(self.window)
        self.qty_entry.pack()

        tk.Label(self.window, text="Unit:").pack()
        self.unit_entry = tk.Entry(self.window)
        self.unit_entry.pack()

        #submit button
        self.add_button = tk.Button(self.window, text="Add Ingredient", command=self.add_ingredient,bg="#FFFFFF", fg="black")
        self.add_button.pack(pady=15)
        
        # delete ingredient button
        self.delete_button = tk.Button(self.window,text="Delete Selected Ingredient",fg="black",bg="#FFFFFF",command=self.delete_ingredient)
        self.delete_button.pack(pady=10)


    #load pantry
    def load_pantry(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for name, (qty, unit) in self.cookbook.pantry.inventory.items():
            self.tree.insert("", "end", values=(f"{name}: {qty}", unit))

    
    def add_ingredient(self):
        name = self.name_entry.get().strip()
        qty_str = self.qty_entry.get().strip()
        unit = self.unit_entry.get().strip()

        if not name or not qty_str or not unit:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        try:
            qty = float(qty_str)
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number.")
            return

        self.cookbook.pantry.add_ingredient(name, qty, unit)
        self.cookbook.save()
        self.load_pantry()
        self.name_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.unit_entry.delete(0, tk.END)

    def delete_ingredient(self):
        selected_item = self.tree.focus()

        if not selected_item:
            messagebox.showerror("Error", "Please select an ingredient to delete.")
            return

        values = self.tree.item(selected_item, "values")
        name_qty_string = values[0]              
        name = name_qty_string.split(":")[0]     

        confirm = messagebox.askyesno("Delete Ingredient",f"Remove '{name}' from the pantry?")
        if not confirm:
            return

        if name in self.cookbook.pantry.inventory:
            del self.cookbook.pantry.inventory[name]

        self.cookbook.save()
        self.load_pantry()
