import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from Quiz_data import Quiz_data
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Identifying time quiz")
root.geometry("600x600")

def start_game():
    pass
    
label = tk.Label(root, text="Identifying time quiz", 
                font=("Arial", 18), 
                fg="black",
                bg="lightblue", 
                padx = 20,
                pady = 10,
                borderwidth = 2)
label.place(x = 170, y = 10)

start_button = tk.Button(root, text="Start", 
                         command=start_game, 
                         width=20, 
                         height=2, 
                         bg = "lightblue", 
                         borderwidth = 2)
start_button.place(x = 215, y = 380)

quit_button = tk.Button(root, text="Quit", 
                        command=root.quit, 
                        width=10, 
                        height=2, 
                        bg = "lightblue",
                        borderwidth = 2)
quit_button.place(x = 250, y = 450)


def skip_question():
    global current_question
    question = Quiz_data[current_question]

    if current_question < len(Quiz_data):
        feedback_label.config(text="The answer is {}".format(question["answer"]), foreground="blue")
    next_button.config(state="normal")

def show_question():
    question = Quiz_data[current_question]
    question_label.config(text=question["question"])
    question_number = current_question + 1  # adds 1 to every question as it passes

    question_label.config(text=f"Question {question_number} \n{question['question']}", font=("Arial", 16), justify = "center")  # displays the question number and the question

    choices = question["choices"]
    for i in range(4): # 4 options
        choice_buttons[i].config(text=choices[i], state="normal") # 'normal' meaning the button is not disabled
    
    feedback_label.config(text="")
    next_button.config(state="disabled") # the user is unable to interact with the button

def check_answer(choice):
    question = Quiz_data[current_question]
    selected_choice = choice_buttons[choice].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/10".format(score, len(Quiz_data))) # the format which scores are displayed in

        feedback_label.config(text="Correct! Well done.", foreground="green")
    else:
        feedback_label.config(text="Incorrect! The answer is {}".format(question["answer"]), foreground="red") # tells the user the correct answer if they got it incorrect
    
    for button in choice_buttons:
        button.config(state="disabled")
    next_button.config(state="normal")

def next_question():
    global current_question
    current_question +=1

    if current_question < len(Quiz_data):
        show_question()
    else: 
        show_score_window() # if there are no questions left the quiz will end with displaying the users score

def show_score_window():
    score_window = tk.Toplevel(root)
    score_window.title("Total score")
    score_window.geometry("600x600")

# the 'n' allows the text to go to the next line
    score_label = tk.Label(score_window, text="Congratulations!\nFinal score: {}/{}".format(score, len(Quiz_data)), font=("Arial", 16), bg = "lightblue")
    score_label.pack(pady=20, padx=40)

    quit_button = tk.Button(score_window, text="Quit", command=root.quit, width=10, height=2, bg="lightblue")
    quit_button.pack(pady=50, padx=90)

root = tk.Tk()
root.title("Identifying time quiz")
root.geometry("600x600")

question_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
question_label.pack(pady=10)

choice_buttons = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_buttons.append(button)

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

next_button = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_button.pack(pady=10)

skip_button = ttk.Button(
    root, 
    text="Skip", 
    command=skip_question
)
skip_button.pack (pady=15)

current_question = 0

show_question()