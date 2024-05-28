import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from Quiz_questions import Quiz_questions
from PIL import ImageTk, Image
from tkinter import PhotoImage

root = tk.Tk()
root.title("Identifying time quiz")
root.geometry("600x600")
root.configure(bg="lightblue")

def second_page():
    global current_question
    global choice_buttons
    global question_label
    global feedback_label
    global score
    global score_label
    global next_button
    global skip_button

    root = tk.Tk()
    root.title("Identifying time quiz")
    root.geometry("600x600")
    root.configure(bg="lightblue")

    question_label = ttk.Label(root, anchor="center", padding=10)
    question_label.pack(pady=10)

    choice_buttons = ["choices"]
    for i in range(4):
        button = ttk.Button(root, command=lambda i=i: check_answer(i))
        button.pack(pady=5)
        choice_buttons.append(button)

    feedback_label = ttk.Label(root, anchor="center", padding=10)
    feedback_label.pack(pady=10)

    score = 0

    score_label = tk.Label(root, text="Score: 0/{}".format(len(Quiz_questions), bg = "lightblue"), anchor="center", font=("Comic Sans MS", 15)) 
    score_label.pack(pady=10)

    next_button = ttk.Button(root, text="Next", command=next_question, state="disabled")
    next_button.pack(pady=10)

    skip_button = ttk.Button(root, text="Skip", command=skip_question)
    skip_button.pack(pady=15)

    current_question = 0

    show_question()

font_family_1 = "Comic Sans MS"
    
label = tk.Label(root, text="Identifying time quiz", 
                font=(font_family_1, 17),
                fg="black",
                bg="white", 
                padx = 20,
                pady = 20,
                borderwidth = 2)
label.place(x = 160, y = 15)

image_frame = tk.Frame(root, bg="lightblue")
image_frame.place(x=180, y=140)

image_file = PhotoImage(file="Home.png")
image_file = image_file.subsample(2,2)
image = tk.Label(image_frame, image=image_file)
image.pack(anchor="center")

start_button = tk.Button(root, text="Start", 
                         command=second_page,
                         font=(font_family_1, 14),
                         width=12, 
                         height=1, 
                         bg = "sky blue", 
                         borderwidth = 1)
start_button.place(x = 220, y = 420)

quit_button = tk.Button(root, text="Quit", 
                        command=root.quit, 
                        font=(font_family_1, 14),
                        width=10, 
                        height=1, 
                        bg = "sky blue",
                        borderwidth = 1)
quit_button.place(x = 230, y = 490)

def next_question():
    global current_question
    current_question +=1

    if current_question < len(Quiz_questions):
        show_question()
        skip_button.config(state="normal") #allows the skip button to be normal on the next question
    else: 
        show_score_window() #if there are no questions left the quiz will end with displaying the users score

feedback_label = ttk.Label(root, anchor="center", padding=10)
feedback_label.pack(pady=10)

next_button = ttk.Button(root, text="Next", command=next_question, state="disabled")
next_button.pack(pady=10)

def show_question():
    global current_question
    global question_label
    global choice_buttons
    global next_button
    global skip_button

    question = Quiz_questions[current_question]
    question_label.config(text=question["question"])
    question_number = current_question + 1 #adds 1 to every question as it passes

    question_label.config(text=f"Question {question_number} \n{question['question']}", font=("Comic Sans MS", 16), justify = "center") #displays the question number and the question

    choices = question["choices"]
    for i in range(4): # 4 options
        choice_buttons[i].config(text="choices"[i], state="normal") #'normal' meaning the button is not disabled
    
    feedback_label.config(text="")
    next_button.config(state="disabled") # the user is unable to interact with the button

def check_answer(choice):
    global score
    global feedback_label
    global next_button
    global skip_button

    question = Quiz_questions[current_question]
    selected_choice = choice_buttons[choice].cget("text")

    score_label = tk.Label(root, text="Score: 0/{}".format(len(Quiz_questions), bg = "lightblue"), anchor="center", font=("Comic Sans MS", 15)) 
    score_label.pack(pady=10)

    skip_button = ttk.Button(root, text="Skip", command=skip_question)
    skip_button.pack(pady=15)

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/10".format(score, len(Quiz_questions))) # the format which scores are displayed in
        feedback_label.config(text="Correct! Well done.", foreground="green", font=("Comic Sans MS", 12))
    else:
        feedback_label.config(text="Incorrect! The answer is {}".format(question["answer"]), foreground="red", font=("Comic Sans MS", 12)) # tells the user the correct answer if they got it incorrect
    
    for button in choice_buttons:
        button.config(state="disabled")
        skip_button.config(state="disabled") #disables the skip button after the option is selected
    next_button.config(state="normal")

def skip_question():
    global current_question
    question = Quiz_questions[current_question]

    if current_question < len(Quiz_questions):
        feedback_label.config(text="The answer is {}".format(question["answer"]), foreground="blue", font=("Comic Sans MS", 12))
    next_button.config(state="normal")

font_family_1 = "Comic Sans MS"

def show_score_window():
    score_window = tk.Toplevel(root)
    score_window.title("Total score")
    score_window.geometry("600x600")
    score_window.config(bg="light blue")

    score_title = tk.Label(score_window, text="Quiz Completed!", font= ("font_family_1 17"))
    score_title.pack(anchor="center")

# the 'n' allows the text to go to the next line
    score_label = tk.Label(score_window, 
                           text="Final score: {}/{}".format(score, len(Quiz_questions)),
                           font=(font_family_1, 17))
    score_label.pack(pady=20, padx=40)

    quit_button = tk.Button(score_window, text="Quit", command=root.quit, width=10, height=2, bg="lightblue")
    quit_button.pack(pady=50, padx=90)

root.mainloop()