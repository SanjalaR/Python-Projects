from para import paras
import random
from tkinter import *

def countdown(secs):
    if secs>0:
        lbl1.config(text=f'Time left: {secs}', foreground='red')
        window.after(1000, countdown, secs-1)
    else:
        lbl1.config(text='Time up!', foreground='red')
        input = txtbox2.get(1.0, END)
        txtbox2.pack_forget()
        lbl1.config(text=f"Your typing speed is {len(input)} characters per minute!", foreground='red')

def speed():
    btn1.pack_forget()

    global txtbox2
    txtbox2 = Text(height=15)
    txtbox2.pack(pady=5)
    txtbox2.focus()

    countdown(60)


window = Tk()
window.title('Typing Test')
window.geometry('900x600+0+0')
window.config(background='black')

lbl1 = Label(text='Test your typing speed!', background='black', foreground='white', font=('Helvetica 15 bold'))
lbl1.pack(side=TOP, pady=20)

txtbox1 = Text(height=15)
txtbox1.insert(END, random.choice(paras))
txtbox1.pack(pady=5)

btn1 = Button(text='Start!', command=speed)
btn1.pack(pady=20)

window.mainloop()