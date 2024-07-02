from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_loop = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    start_button['state'] = 'normal'
    global reps
    reps = 0
    window.after_cancel(timer_loop)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button['state'] = 'disabled'
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps%8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_secs) #THis will loop because of the window.mainloop function which is constantly checking the screen for changes every millisecond
    elif reps%2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_secs)
    elif reps%2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins = math.floor(count/60)
    secs = str(count%60)
    if len(secs) == 1:
        secs = "0" + secs
    canvas.itemconfig(timer, text=f"{mins}:{secs}")
    if count > 0:
        global timer_loop
        timer_loop = window.after(1000, count_down, count -1) #After a 1 second, it will call the function with the given arguments
    else:
        start_timer()
        global reps
        if reps%2 == 0:
            marks = ""
            work_sessions = reps//2
            for x in range(work_sessions):
                marks += "✓"
            check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img) 
#x and y values, 100 is half of the width, 112 is half of the height so the image will be centered.
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)




window.mainloop()
