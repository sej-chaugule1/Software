from tkinter import *

questions = ("What time is displayed?",
             "What time is displayed?",
             "What time is displayed?",
             "What time is displayed?",
             "What time is displayed?",
             "What time is displayed?",
             "What time is displayed?",
             "What time is displayed?",
             "What time is displayed?",
             "What time is displayed?",)


options = (("A. 5:30", "B. 7:00", "C. 12:15", "D. 8:45"),
            ("A. 6:45", "B. 4:50", "C. 9:00", "D. 12:20"),
            ("A. 7:30", "B. 11:55", "C. 2:10", "D. 1:25"),
            ("A. 3:00", "B. 10:25", "C. 5:05", "D. 7:35"),
            ("A. 8:15", "B. 12:45", "C. 9:10", "D. 4:00"),
            ("A. 7:30", "B. 11:55", "C. 2:10", "D. 1:25"),
            ("A. 5:30", "B. 7:00", "C. 12:15", "D. 8:45"),
            ("A. 7:00", "B. 11:20", "C. 2:10", "D. 1:25"),
            ("A. 6:45", "B. 4:00", "C. 10:30", "D. 12:20"),
            ("A. 4:50", "B. 10:25", "C. 5:40", "D. 7:35"))


answers = ("B. 7:00", "D. 12:20", "C. 2:10", "A. 3:00", "B. 12:45", "D. 1:25", "C. 12:15", "B. 11:20", "A. 6:45", "D. 7:35")

Score = 0
Total_Questions = 10
Question_no = 1

def start_again():
    global Score,Question_no

    Score = 0
    Question_no = 1
    val1.set(0)
    val2.set(0)
    val3.set(0)
    question.config(text=questions[Question_no-1])
    option1.config(text=options[Question_no-1][0])
    option2.config(text=options[Question_no-1][1])
    option3.config(text=options[Question_no-1][2])
    next_b.config(text="next")
    play_again.place_forget()
    score.place_forget()
    root.pack()

def next():
    global Score, Question_no
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if answers[Question_no-1] == selected_option :
        Score += 1

    Question_no += 1

    if Question_no > Total_Questions:
        root.pack_forget()
        score.place(relx=.5, rely=.5,anchor=CENTER)
        play_again.place(relx=.45, rely=.1)

        score.config(text="Score:"+str(Score), font=("Arial", 15))

    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=questions[Question_no-1])
        option1.config(text=options[Question_no-1][0])
        option2.config(text=options[Question_no-1][1])
        option3.config(text=options[Question_no-1][2])


def check(option):
    if option == 1:
        val2.set(0)
        val3.set(0)
    elif option == 2:
        val1.set(0)
        val3.set(0)
    else:
        val2.set(0)
        val1.set(0)


def start_game():
    user_screen.place_forget()
    root.pack()


Win = Tk()
Win.geometry("600x600")
Win.title("Identifying Time Quiz")
Win.configure(bg = "sky blue")

user_screen = Frame()
user_screen.place(relx=0.5, rely=0.5, anchor=CENTER)
intro_message = Label(user_screen, width=60, font=("Arial", 15), text="Identifying Time Quiz", bg = "sky blue")
intro_message.pack()
play_b = Button(user_screen, text="Start", command=start_game, 
                        width=20, 
                         height=2, 
                         bg = "lightblue", 
                         borderwidth = 2)
play_b.place(x = 80, y = 80)
exit_b = Button(user_screen, text="Quit", command=Win.quit,
                width=10, 
                height=2, 
                bg = "lightblue",
                borderwidth = 2)
exit_b.place(x = 100, y = 100)


root = Frame(Win)
root.pack_forget()

question = Label(root, width=60, font=("Arial", 15), text=questions[0])
question.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root, variable=val1, text=options[0][0], command=lambda: check(1))
option1.pack()

option2 = Checkbutton(root, variable=val2, text=options[0][1], command=lambda: check(2))
option2.pack()

option3 = Checkbutton(root, variable=val3, text=options[0][2], command=lambda: check(3))
option3.pack()

next_b = Button(root, text="next", command=next)
next_b.pack()

score = Label(Win)
score.place_forget()

play_again = Button(Win,text= "Play Again",command=start_again)
play_again.place_forget()

Win.mainloop()