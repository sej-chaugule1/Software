import tkinter as tk
from tkinter import *

def start_game():
    pass

root = tk.Tk()
root.title("Identifying time quiz")
root.geometry("600x600")
root.configure(bg = "sky blue")

label = tk.Label(root, text="Identifying time quiz", 
                font=("Arial", 18), 
                fg="black",
                bg="white", 
                padx = 20,
                pady = 10,
                borderwidth = 2)
label.place(x = 170, y = 10)

start_button = tk.Button(root, text="Start Game", 
                         command=start_game, 
                         width=20, 
                         height=2, 
                         bg = "lightblue", 
                         borderwidth = 2)
start_button.place(x = 215, y = 380)

exit_button = tk.Button(root, text="Exit", 
                        command=root.quit, 
                        width=10, 
                        height=2, 
                        bg = "lightblue",
                        borderwidth = 2)
exit_button.place(x = 250, y = 450)

root.mainloop()