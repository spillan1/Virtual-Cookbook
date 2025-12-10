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
from PIL import Image, ImageTk
import os

if __name__ == "__main__":
    cookbook = Cookbook()
    cookbook.load()
    
    def open_pantry_window():
        '''
        opens a separate pantry window

        Returns
        -------
        None.

        '''
        PantryWindow(root, cookbook)

    def open_add_recipe_window():
        '''
        opens a separate add recipe window

        Returns
        -------
        None.

        '''
        AddRecipeWindow(root, cookbook)

    def open_recipe_list_window():
        '''
        opens a separate recipe list window

        Returns
        -------
        None.

        '''
        RecipeListWindow(root, cookbook)

    def open_can_make_window():
        '''
        opens a separate window of recipoes that can be made

        Returns
        -------
        None.

        '''
        recipes = cookbook.can_make()
        if recipes:
            messagebox.showinfo("Recipes You Can Make", "\n".join(recipes))
        else:
            messagebox.showinfo("Recipes You Can Make", "No recipes can be made right now.")

    root = tk.Tk()
    root.title("Virtual Cookbook")
    root.geometry("400x400")
    root.configure(bg="#F9D790")

    title_label = tk.Label(root, bg="#F1A90E", fg="black", text="Virtual Cookbook", font=("Georgia", 30)).pack(pady=50)
    
    btn1 = tk.Button(root, highlightbackground="#F1A90E", text="View Pantry", width=25, command=open_pantry_window).pack(pady=5)

    btn2 = tk.Button(root, highlightbackground="#F1A90E", text="Add Recipe", width=25, command=open_add_recipe_window).pack(pady=5)

    btn3 = tk.Button(root, highlightbackground="#F1A90E", text="View Recipes", width=25, command=open_recipe_list_window)
    btn3.pack(pady=5)

    btn4 = tk.Button(root, highlightbackground="#F1A90E", text="What Can I Make?", width=25, command=open_can_make_window)
    btn4.pack(pady=5)
    
    def on_close():
        cookbook.save()
        root.quit()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()





