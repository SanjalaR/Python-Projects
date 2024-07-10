
from tkinter import *
from tkinter import filedialog
from PIL import Image
from collections import Counter

BG_COLOR = '#2C2E3A'


def but1_click():
    filetypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=filetypes)

    if len(path):
        image = Image.open(path)
        image = image.resize((100,100))
        pixels = list(image.getdata())
        colors = Counter(pixels)
        most_comm = colors.most_common(5)
        colors = [f'RGB{color}' for color,_ in most_comm]
        colors = ', '.join(colors)
        lbl1.config(text=colors)



window = Tk()
window.title('Image Color Palette Generator')
window.geometry('900x600+0+0')
window.config(background=BG_COLOR)

btn1 = Button(text='Upload an Image', command=but1_click)
btn1.pack(pady=20)

lbl1 = Label(foreground='white', background=BG_COLOR)
lbl1.pack(pady=50)

window.mainloop()
