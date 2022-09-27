import tkinter as tk
from tkinter import ttk
import random


# Defining the actual game.
def game_code():
    global result_random
    option_list = ["rock", "paper", "scissors"]
    result_random = random.choice(option_list)

def clicked_rock():
    game_code()
    if result_random == "rock":
        label_game_output.configure(text="Shit, it's a tie!")
    elif result_random == "paper":
        label_game_output.configure(text="Shit, you lose!")
    else:
        label_game_output.configure(text="You won! Yihaaa!")

def clicked_paper():
    game_code()
    if result_random == "paper":
        label_game_output.configure(text="Shit, it's a tie!")
    elif result_random == "scissors":
        label_game_output.configure(text="Shit, you lose!")
    else:
        label_game_output.configure(text="You won! Yihaaa!")

def clicked_chizzors():
    game_code()
    if result_random == "scissors":
        label_game_output.configure(text="Shit, it's a tie!")
    elif result_random == "rock":
        label_game_output.configure(text="Shit, you lose!")
    else:
        label_game_output.configure(text="You won! Yihaaa!")


# Setting up defaults, main core stuff. Also setting the icon.
root = tk.Tk()
root.title("KDR")
root.iconbitmap("favicon.ico")

root.option_add("*tearOff", False) # This is always a good idea
root.tk.call('source', 'forest-dark.tcl')
ttk.Style().theme_use('forest-dark')


# Top app text.
label_welcome_top = ttk.Label(root, text="Rock, paper and scissors game!")
label_welcome_top.pack(pady=15, padx=30)

# User input buttons.
btn_rock_input = ttk.Button(root, text="Rock", command=clicked_rock)
btn_rock_input.pack(pady=5, padx=30)

btn_paper_input = ttk.Button(root, text="Paper", command=clicked_paper)
btn_paper_input.pack(pady=5, padx=30)

btn_scissors_input = ttk.Button(root, text="Scissors", command=clicked_chizzors)
btn_scissors_input.pack(pady=5, padx=30)

# Output game area
label_game_output = ttk.Label(root, text="")
label_game_output.pack(pady=15, padx=30)


# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

root.mainloop()