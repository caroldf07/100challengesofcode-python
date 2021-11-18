import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
laps = 0
clock = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global laps
    laps = 0
    canvas.itemconfig(timer_text, text="00:00")
    """Sem o window.after_cancel() a função segue para o start_timer e fica num looping para sempre"""
    window.after_cancel(clock)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global laps
    laps += 1

    if laps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_time_label.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)
    elif laps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_time_label.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)
    else:
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Aqui ele vai pegar a variável timer_text e setar o texto de acordo com a variável count.
    Quando se usa o Canvas, fica dessa forma diferentemente de quando se usa o Label"""
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds <= 9:
        seconds = f"0{seconds}"
    else:
        pass

    if minutes <= 9:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global clock
        clock = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=100, height=100)
window.config(padx=50, pady=50, bg=YELLOW)

timer_time_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_time_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
"""Aqui colocamos o canvas dentro de uma variável para poder modificar o tempo"""
timer_text = canvas.create_text(103, 112, fill=RED, font=(FONT_NAME, 35, "bold"))
canvas.itemconfig(timer_text, text="00:00")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=FONT_NAME, fg="black", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", font=FONT_NAME, fg="black", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
