from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE= "#26577C"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_TICK='✔'
REPS = 0
IS_FOCUS=1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    #timer_text= 00:00
    canvas.itemconfig(timer_text, text='00:00')

    # removes check_labels
    check_label.config(text='')
    #title_label= "Pomodoro"
    timer_label.config(text='Pomodoro', fg=GREEN)
    global REPS
    REPS=0


    return 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    global IS_FOCUS
    if IS_FOCUS:
        count_down(WORK_MIN*60)
    elif REPS%3==0:
        count_down(LONG_BREAK_MIN*60)
    else:
        count_down(SHORT_BREAK_MIN*60)

    



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS
    global IS_FOCUS
    global timer
    
    count_min= math.floor(count/60)
    count_sec= count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}' 
    
    if count_min < 10:
        count_min = f'0{count_min}' 

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count==0 and IS_FOCUS:
        IS_FOCUS=0
        if REPS%3==0:
            fg=RED
        else:
            fg=PINK
        timer_label.config(text='Break', fg=fg)
        REPS+=1
        check_label.config(text=CHECK_TICK*REPS)
        return
    elif count==0:
        IS_FOCUS=1
        timer_label.config(text='Focus', fg=GREEN)
        return
    timer=window.after(1000, count_down, count- 1)

        


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=BLUE)


#create canvas
canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
# create tomato image
tomato_image=PhotoImage(file='static/tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 132, text='00:00', fill='white', font= (FONT_NAME, 35, 'bold'))
canvas.grid(row=1,column=1)




#label
timer_label = Label(text="Focus", bg=BLUE, font=('Calabri', 35, "bold"), fg=GREEN)
# label.config(text="This is new text")
timer_label.grid(row=0, column=1)


#start button
start_button = Button(text="Start", command=start)
start_button.grid(row=2, column=0)


#reset button
reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=2, column=2)


#check counts
check_label = Label(text= '', bg=BLUE, font=('Calabri', 15, "bold"), fg=GREEN)

# label.config(text="This is new text")
check_label.grid(row=3, column=1)
window.mainloop()