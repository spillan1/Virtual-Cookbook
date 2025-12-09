#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 15:01:50 2025

@author: shriya
"""

import tkinter as tk
from tkinter import messagebox
from cookbook_define import Cookbook
from pantry_window_GUI import PantryWindow
from add_recipe_window_GUI import AddRecipeWindow
from recipe_list_window_GUI import RecipeListWindow

def main():
    cookbook = Cookbook()
    cookbook.load()
    
    def open_pantry_window():
        PantryWindow(root, cookbook)

    def open_add_recipe_window():
        AddRecipeWindow(root, cookbook)

    def open_recipe_list_window():
        RecipeListWindow(root, cookbook)

    def open_can_make_window():
        recipes = cookbook.recipes_you_can_make()
        if recipes:
            messagebox.showinfo("Recipes You Can Make", "\n".join(recipes))
        else:
            messagebox.showinfo("Recipes You Can Make", "No recipes can be made right now.")

    root = tk.Tk()
    root.title("Virtual Cookbook")
    root.geometry("400x400")

    title_label = tk.Label(root, text="Virtual Cookbook", font=("Helvetica", 18))
    title_label.pack(pady=20)

    btn1 = tk.Button(root, text="View Pantry", width=25, command=open_pantry_window)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Add Recipe", width=25, command=open_add_recipe_window)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="View Recipes", width=25, command=open_recipe_list_window)
    btn3.pack(pady=5)

    btn4 = tk.Button(root, text="What Can I Make?", width=25, command=open_can_make_window)
    btn4.pack(pady=5)
    
    def on_close():
        cookbook.save()
        root.quit()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    root.mainloop()


if __name__ == "__main__":
    main()

