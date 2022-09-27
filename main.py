from tkinter import ttk
from ttkthemes import ThemedTk
import random
from tkinter import *
import tkinter



# Defining the actual game.
def game_code():
    global result_random
    option_list = ["rock", "paper", "scissors"]
    result_random = random.choice(option_list)

def clicked_rock():
    game_code()
    if result_random == "rock":
        output_game.configure(text="Shit, it's a tie!")
    elif result_random == "paper":
        output_game.configure(text="Shit, you lose!")
    else:
        output_game.configure(text="You won! Yihaaa!")

def clicked_paper():
    game_code()
    if result_random == "paper":
        output_game.configure(text="Shit, it's a tie!")
    elif result_random == "scissors":
        output_game.configure(text="Shit, you lose!")
    else:
        output_game.configure(text="You won! Yihaaa!")

def clicked_chizzors():
    game_code()
    if result_random == "scissors":
        output_game.configure(text="Shit, it's a tie!")
    elif result_random == "rock":
        output_game.configure(text="Shit, you lose!")
    else:
        output_game.configure(text="You won! Yihaaa!")






# GUI code below me.
window = ThemedTk(theme='yaru')

# Setting up core value's.
window.title("Rock, paper, scissors!")
window.geometry("300x185")
window.iconbitmap(r"kdr.png")

# The different elements within the application (TXT, buttons etc).
greeting_txt = Label(window, text="Rock, paper, scissors game!!!", width=40)
greeting_txt.grid(column=6, row=0)

btn = ttk.Button(window, text="Rock", command=clicked_rock, width=10)
btn.grid(column=6, row=1, pady=5)

btn_two = ttk.Button(window, text="Paper", command=clicked_paper, width=10)
btn_two.grid(column=6, row=2, pady=5)

btn_three = ttk.Button(window, text="Scissors", command=clicked_chizzors, width=10)
btn_three.grid(column=6, row=3, pady=5)

output_game = Label(window, text="")
output_game.grid(column=6, row=4, sticky=tkinter.S, pady=5)

window.mainloop()
