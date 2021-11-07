#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Help menu
"""   
import tkinter as tk


def printRules():
    """
    Load a text files 'rules_eng.txt' saved inside the same directory.
    Open a second window.

    Returns
    -------
    None.

    """
    ruleWindow=tk.Toplevel()
    ruleWindow.title("How to play")
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lab_Rule=tk.Label(ruleWindow,text=gameRules,fg="black", anchor="e", justify=tk.LEFT)
    lab_Rule.pack(side=tk.TOP)
    ruleWindow.mainloop()


def about():
    """
    Load the text document 'about.txt'.
    Open a secondary window.
    Write the content of the text document.

    Returns
    -------
    None.

    """
    aboutWindow=tk.Toplevel()
    aboutWindow.title("About") 
    with open('about.txt') as f:
        about=f.read()
    lbl_about=tk.Label(aboutWindow,text=about,fg="black", anchor="e", justify=tk.LEFT)
    lbl_about.pack(side=tk.TOP)
    aboutWindow.mainloop() 
