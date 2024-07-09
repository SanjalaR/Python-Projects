from tkinter import *
from threading import Timer

BG_COLOR = '#45A29E'
TEXT_BG = '#AFDDE5'


class App():
    def __init__(self, window):
        if __name__ == '__main__':
            self.window = window
            window.title('Disappearing Text Writing App')
            window.geometry('900x600+0+0')
            window.state('zoomed')
            window.config(background=BG_COLOR)

            self.lbl1 = Label(text='Start Writing!', font=('Helvetica 20 bold'), foreground='white',
                              background=BG_COLOR)
            self.lbl1.pack(side=TOP, pady=20)

            self.lbl2 = Label(text='Beware! If you stop typing, your words will disppear 👻', font=('Helvetica 15 bold'),
                              foreground='white', background=BG_COLOR)
            self.lbl2.pack(pady=5)

            self.txtbox = Text(height=70, width=70, background=TEXT_BG, foreground='black')
            self.txtbox.pack(pady=20)
            self.txtbox.bind('<KeyPress>', self.key_press)

            self.timer_id = None

    def key_press(self, event):
        if self.timer_id is not None:
            self.window.after_cancel(self.timer_id)
        self.timer_id = self.window.after(5000, self.delete_text)

    def delete_text(self):
        self.txtbox.delete('1.0', END)


window = Tk()
app = App(window)
window.mainloop()
