from  tkinter import *
import pandas as pd
import random as rd
import time
import json
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"
card_front='card_front.png'
card_back='card_back.png'
front=True
FLIP_TIME=3 #sec
LANGUAGE='French'
WORD='First Word'
try:
    with open('./data/unknown_words.json', 'r') as json_file:
        VOCAB = json.load(json_file)
except FileNotFoundError:
    VOCAB= pd.read_csv('./data/french_words.csv').set_index(keys='French')['English'].to_dict()
flip_timer = None

#------------------------------------------------Logic-----------------------------------------------------#
def crete_new_card():
    global VOCAB
    global WORD
    global flip_timer
    fill_color='black'
    if flip_timer:
        window.after_cancel(flip_timer)
    WORD=rd.choice(list(VOCAB.keys()))
    canvas.itemconfig(card_image, {'image': IMG_CARD_FRONT})
    canvas.itemconfig(text_word, {'text': WORD, 'fill': fill_color})
    canvas.itemconfig(text_title, {'text': 'French', 'fill': fill_color})
    flip_timer=window.after(3000, create_rare_card)
    return WORD

def create_rare_card():
    global VOCAB
    global WORD
    fill_color='white'
    canvas.itemconfig(card_image, {'image': IMG_CARD_BACK})
    canvas.itemconfig(text_word, {'text': VOCAB[WORD], 'fill': fill_color})
    canvas.itemconfig(text_title, {'text': 'English', 'fill': fill_color})
    return WORD


def incorrect_clicked():
    crete_new_card()

 
def correct_clicked():
    if not VOCAB:
        messagebox.showinfo('You WIN',"I guess we ran out of words, for you to learn")
        return


    VOCAB.pop(WORD)

    try:
        with open('./data/unknown_words.json', 'w') as json_file:
            json.dump(VOCAB, json_file)
    except IOError as e:
        print(f"An error occurred: {e}")    
    crete_new_card()   


# ------------------------------------------------ UI------------------------------------------------------#
#set up window
window = Tk()
window.title("French Cards")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

# add canvas and image
canvas = Canvas(width=800, height=526,bg = BACKGROUND_COLOR, highlightthickness=0)
# front_canvas.itemconfig()
# canvas.create_line(10, 10, 200, 50, fill='red', width=3)
#creating image for lock
IMG_CARD_FRONT = PhotoImage(file='./images/'+card_front)
IMG_CARD_BACK = PhotoImage(file='./images/'+card_back)

card_image=canvas.create_image(400, 270, image=IMG_CARD_FRONT)
text_title= canvas.create_text(400, 150, text=LANGUAGE, font=('Times New Roman', 40, 'italic'))
text_word=canvas.create_text(400, 263, text=WORD, font=('Times New Roman', 60, 'bold'))
canvas.grid(row=0,column=0, padx=30, pady=30, columnspan=2)


#addubg buttons
img_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, command=incorrect_clicked)
button_wrong.grid(row=1, column=0)

img_right = PhotoImage(file="./images/right.png")
button_right = Button(image=img_right, highlightthickness=0, command=correct_clicked)
button_right.grid(row=1, column=1)

crete_new_card()



window.mainloop()