import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import PhotoImage

Quiz_questions = [
    {
    "question": "When the big hand is on 12 and the small hand is on 7,\nwhat is the time?",
    "choices": ["A. 5:30", "B. 7:00", "C. 12:15", "D. 8:45"],
    "answer": "B. 7:00"
},
    
{ 
    "question": "At 9:20 PM, what time is displayed on\na digital clock?",
    "choices": ["A. 18:45", "B. 04:50", "C. 00:00", "D. 21:20"],
    "answer": "D. 21:20"
},
    
{
    "question": "When both hands are pointing at 12,\nwhat is the time?",
    "choices": ["A. 7:30", "B. 11:55", "C. 12:00", "D. 1:25"],
    "answer": "C. 12:00"
},
    
{
    "question": "If it is midnight. What time is displayed \non a digital clock?",
    "choices": ["A. 00:00", "B. 22:25", "C. 05:05", "D. 13:35"],
    "answer": "A. 00:00"
},

{
    "question": "What time does the analogue clock show when the \nbig hand is on 9 and the small hand is almost on 1?",
    "choices": ["A. 8:15", "B. 12:45", "C. 9:10", "D. 4:00"],
    "answer": "B. 12:45"
},

{
    "question": "If a digital clock displays 01:25, \nwhat time is it?",
    "choices": ["A. 7:30", "B. 11:55", "C. 2:10", "D. 1:25"],
    "answer": "D. 1:25"
},

{
    "question": "When the small hand is point directly left and \nthe big hand is pointing directly right, \nwhat time is on the analogue clock?",
    "choices": ["A. 5:30", "B. 7:00", "C. 9:15", "D. 8:45"],
    "answer": "C. 9:15"
},

{
    "question": "If the time is 11:20 at night, \nhow would a digital clock display this time",
    "choices": ["A. 07:00", "B. 23:20", "C. 14:10", "D. 13:20"],
    "answer": "B. 23:20"
},

{
    "question": "What time is it when both hands \nare on 6 on an analogue clock?",
    "choices": ["A. 6:30", "B. 4:00", "C. 10:45", "D. 12:20"],
    "answer": "A. 6:30"
},

{
    "question": "If a digital clock shows 19:35, \nwhat time is it",
    "choices": ["A. 4:50", "B. 10:25", "C. 5:40", "D. 7:35"],
    "answer": "D. 7:35"
}
]

root = tk.Tk()
root.title("Identifying time quiz")
root.geometry("600x600")
root.configure(bg="lightblue", borderwidth=2, relief="ridge")

font_family_1 = "Comic Sans MS"

def second_page():
    global current_question
    global choice_buttons
    global question_label
    global feedback_label
    global score
    global score_label
    global next_button
    global skip_button

    root.destroy

    question_window = tk.Toplevel(root)
    question_window.title("Quiz")
    question_window.geometry("600x600")
    question_window.configure(bg="lightblue")

    question_label = tk.Label(question_window, text="", bg="white")
    question_label.pack(pady=10)

    choice_buttons = []
    for i in range(4):
        button = ttk.Button(question_window, command=lambda i=i: check_answer(i))
        button.pack(pady=7)
        choice_buttons.append(button)

    feedback_label = tk.Label(question_window, text="", bg="lightblue")
    feedback_label.pack(pady=10)

    score = 0
    score_label = tk.Label(question_window, text="Score: 0/10".format(len(Quiz_questions)), font=("Comic Sans MS", 15), bg="lightblue")
    score_label.pack(pady=10)

    next_button = ttk.Button(question_window, text="Next", command=next_question, state="disabled")
    next_button.pack(pady=10)

    skip_button = ttk.Button(question_window, text="Skip", command=skip_question)
    skip_button.pack(pady=15)

    image_frame2 = tk.Frame(root, bg="lightblue")
    image_frame2.place(x=180, y=140)

    current_question = 0
    show_question()

def show_question():
    global current_question
    global question_label
    global choice_buttons
    global next_button
    global skip_button

    question = Quiz_questions[current_question]
    question_label.config(text=question["question"], bg="white")
    question_number = current_question + 1
    question_label.config(text=f"Question {question_number}:\n {question['question']}", font=("Comic Sans MS", 15), justify = "center", bg="white")

    choices = question["choices"]
    for i in range(4):
        choice_buttons[i].config(text=choices[i], state="normal")

    feedback_label.config(text="", bg="lightblue")
    next_button.config(state="disabled")

def check_answer(choice):
    global score
    global feedback_label
    global next_button
    global skip_button

    question = Quiz_questions[current_question]
    selected_choice = choice_buttons[choice].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/10".format(score, len(Quiz_questions)))
        feedback_label.config(text="Correct! Well done.", foreground="green", font=("Comic Sans MS", 12), bg="lightblue")
    else:
        feedback_label.config(text="Incorrect! The answer is {}".format(question["answer"]), foreground="red", font=("Comic Sans MS", 12), bg="lightblue")

    for button in choice_buttons:
        button.config(state="disabled")
        skip_button.config(state="disabled")
    next_button.config(state="normal")

def skip_question():
    global current_question
    global feedback_label
    global next_button
    global Quiz_questions

    question = Quiz_questions[current_question]

    if current_question < len(Quiz_questions):
        feedback_label.config(text="The answer is {}".format(question["answer"]), foreground="blue", font=("Comic Sans MS", 12))
    next_button.config(state="normal")

def next_question():
    global current_question

    current_question += 1
    if current_question < len(Quiz_questions):
        show_question()
        skip_button.config(state="normal") #allows the skip button to be normal on the next question
    else: 
        show_score_window() #if there are no questions left the quiz will end with displaying the users score

font_family_1 = "Comic Sans MS"

def show_score_window():
    score_window = tk.Toplevel(root)
    score_window.title("Total score")
    score_window.geometry("600x600")
    score_window.config(bg="light blue")

    score_title = tk.Label(score_window, text="Quiz Completed!", font= ("Comic Sans MS", 17), bg = "white", borderwidth = 2)
    score_title.pack(pady = 10, anchor="center")

    image_frame = tk.Frame(score_window)
    image_frame.pack(pady=20)

    image_path = "Congratulations.png" 
    image = Image.open(image_path)
    image = image.resize((300, 200)) 

    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(image_frame, image=photo, bg="lightblue")
    image_label.pack()

    score_label = tk.Label(score_window, 
                           text="Your score: {}/{}".format(score, len(Quiz_questions)),
                           font=(font_family_1, 20), bg="lightblue")
    score_label.pack(pady=20, padx=40)

    quit_button = tk.Button(score_window, text="Quit", command=root.quit, width=10, height=2, bg="skyblue")
    quit_button.pack(pady=50, padx=90)

label = tk.Label(root, text="Identifying time quiz", 
                font=(font_family_1, 19),
                fg="black",
                bg="white", 
                padx = 20,
                pady = 20,
                borderwidth = 2)
label.place(x = 160, y = 15)

image_frame = tk.Frame(root, bg="lightblue")
image_frame.place(x=100, y=110)

image_file = PhotoImage(file="Home.png")
image_file = image_file.subsample(1,1)
image = tk.Label(image_frame, image=image_file, bg="lightblue")
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

root.mainloop()
