#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 15:48:32 2025

@author: shriya
"""
import tkinter as tk
from tkinter import ttk, messagebox


class PantryWindow:
    """defines a PantryWindow class"""
    def __init__(self, master, cookbook):
        self.cookbook = cookbook

        self.window = tk.Toplevel(master)
        self.window.title("Pantry")
        self.window.geometry("400x550")
        #self.window.configure(bg="#F9D790")

        #pantry display
        self.tree = ttk.Treeview(self.window,columns=("quantity", "unit"), show="headings")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("unit", text="Unit")
        self.tree.pack(fill="both", expand=True, pady=10)
        self.load_pantry()

        #ingredients section
        tk.Label(self.window, font=("Helvetica", 12, "bold"),text="Add Ingredient").pack(pady=5)
        tk.Label(self.window, text="Ingredient Name:").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()
        tk.Label(self.window, text="Quantity:").pack()
        self.amount_enter = tk.Entry(self.window)
        self.amount_enter.pack()
        tk.Label(self.window, text="Unit:").pack()
        self.unit_entry = tk.Entry(self.window)
        self.unit_entry.pack()

        #submit button
        self.add_button = tk.Button(self.window, text="Add Ingredient", command=self.add_ingredient,bg="#FFFFFF", fg="black")
        self.add_button.pack(pady=15)
        
        # delete ingredient button
        self.delete_button = tk.Button(self.window,text="Delete Selected Ingredient",fg="black",bg="#FFFFFF",command=self.delete_ingredient)
        self.delete_button.pack(pady=10)


    def load_pantry(self):
        '''
        loads the pantry

        Returns
        -------
        None.

        '''
        for row in self.tree.get_children():
            self.tree.delete(row)

        for name, (qty, unit) in self.cookbook.pantry.inventory.items():
            self.tree.insert("", "end", values=(f"{name}: {qty}", unit))

    
    def add_ingredient(self):
        '''
        adgs an ingredient to the pantry

        Returns
        -------
        None.

        '''
        name = self.name_entry.get()
        amountstring = self.amount_enter.get()
        unit = self.unit_entry.get()

        amount = float(amountstring)
        self.cookbook.pantry.add_ingredient(name, amount, unit)
        self.cookbook.save()
        self.load_pantry()
        self.name_entry.delete(0, tk.END)
        self.amount_enter.delete(0, tk.END)
        self.unit_entry.delete(0, tk.END)

    def delete_ingredient(self):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        selection = values[0]              
        name = selection.split(":")[0]     

        if name in self.cookbook.pantry.inventory:
            del self.cookbook.pantry.inventory[name]
        self.cookbook.save()
        self.load_pantry()
