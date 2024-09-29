import re
import tkinter as tk
import tkinter.messagebox as messagebox
def funct(slovo):
    result = re.match(r'm[a-zA-Zа-яА-ЯёЁ]{2}e$', slovo)
    if result is not None:
        print("Match")
    else:
        messagebox.showerror("No match","No match")
        
#funct("mate")
funct("maaae")