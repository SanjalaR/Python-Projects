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
        count = 0
        input_words = input.split()
        qs_words = qs.split()
        for i in range(len(input_words)):
            if input_words[i]!=qs_words[i]:
                print(input_words[i], qs_words[i])
                count+=1
        txtbox2.pack_forget()
        acc = (len(input)-count)*100/len(input)
        lbl1.config(text=f"Your typing speed is \n{len(input)} characters per minute\n{len(input_words)} words per minute\nAccuracy is {acc:.2f}%", foreground='red')

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

# global qs
qs = random.choice(paras)
txtbox1 = Text(height=15)
txtbox1.insert(END, qs)
txtbox1.pack(pady=5)

btn1 = Button(text='Start!', command=speed)
btn1.pack(pady=20)

window.mainloop()
