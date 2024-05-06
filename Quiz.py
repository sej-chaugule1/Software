import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def start_game():
    pass

root = tk.Tk()
root.title("Identifying time quiz")
root.geometry("600x600")
root.configure("lightblue")

image = Image.open("Icon.png") 
image = image.resize((200, 150))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack()

label = tk.Label(root, text="Identifying time quiz", 
                font=("Arial", 18), 
                fg="black",
                bg="lightblue", 
                padx = 20,
                pady = 10,
                borderwidth = 2)
label.pack()

start_button = tk.Button(root, text="Start Game", 
                         command=start_game, 
                         width=20, 
                         height=2, 
                         bg = "lightblue", 
                         borderwidth = 2)
start_button.place(x = 215, y = 200)

exit_button = tk.Button(root, text="Exit", 
                        command=root.quit, 
                        width=10, 
                        height=2, 
                        bg = "lightblue",
                        borderwidth = 2)
exit_button.place(x = 250, y = 300)

root.mainloop()












