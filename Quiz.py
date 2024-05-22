import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from Quiz_data import Quiz_data

def start_game():
    pass

root = tk.Tk()
root.title("Identifying time quiz")
root.geometry("600x600")
root.configure(bg = "sky blue")

label = tk.Label(root, text="Identifying time quiz", 
                font=("Arial", 18), 
                fg="black",
                bg="lightblue", 
                bg="white", 
                padx = 20,
                pady = 10,
                borderwidth = 2)
label.place(x = 170, y = 10)

start_button = tk.Button(root, text="Start Quiz", 
                         command=start_game, 
                         width=20, 
                         height=2, 
                         bg = "lightblue", 
                         borderwidth = 2)
start_button.place(x = 215, y = 380)

exit_button = tk.Button(root, text="Quit", 
                        command=root.quit, 
                        width=10, 
                        height=2, 
                        bg = "lightblue",
                        borderwidth = 2)
exit_button.place(x = 250, y = 450)

def start_quiz(window):
    window.destroy()

def show_question():
    question = Quiz_data[current_question]
    qs_label.config(text=question["question"])

    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice):
    question = Quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(Quiz_data)))
        feedback_label.config(text="Correct! Well done.", foreground="green")
    else:
        feedback_label.config(text="Incorrect! The answer is", foreground="red")
    
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

def next_question():
    global current_question
    current_question +=1

    if current_question < len(Quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(Quiz_data)))
        root.destroy()

root = tk.Tk()
root.title("Identifying time quiz")
root.geometry("600x600")

qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

score = 0

score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(Quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

current_question = 0

show_question()

root.mainloop()