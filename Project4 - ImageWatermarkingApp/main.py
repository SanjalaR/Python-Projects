import tkinter
import tkinter.filedialog
from tkinter import *
from PIL import Image, ImageTk


class App:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.lbl1 = Label(self.frame, text='Upload an image')
        self.lbl1.pack(pady=10)

        self.lbl2 = Label(self.frame)
        self.lbl2.pack(pady=10)

        self.uploadbtn = Button(self.frame, text='Upload', command=self.imageUploader)
        self.uploadbtn.pack(side=tkinter.BOTTOM, pady=20)

        self.logo_btn = Button(self.frame, text='Upload Logo')
        self.logo_btn.pack_forget()

        self.dl_btn = Button(self.frame, text='Download')
        self.dl_btn.pack_forget()

        self.imw = 0
        self.imh = 0


    def download(self, img):
        # edge = Image.fromarray(img)
        #img = img.resize((self.imw,self.imh))
        filename = tkinter.filedialog.asksaveasfile(mode='w', defaultextension='.jpg')
        if not filename:
            return
        img.save(filename)
        self.lbl1.config(text='Saved successfully!')

    def logoUploader(self, img):
        filetypes = [('Image files', '*.png;*.jpg;*.jpeg')]
        path_logo = tkinter.filedialog.askopenfilename(filetypes=filetypes)

        if len(path_logo):
            img_logo = Image.open(path_logo)
            img_logo = img_logo.resize((30,30))

            img.paste(img_logo, (170,170))
            new_img = ImageTk.PhotoImage(img)
            self.lbl2.config(image=new_img)
            self.lbl2.image = new_img

            self.dl_btn.config(command=lambda:(self.download(img)))
            self.dl_btn.pack(side=tkinter.BOTTOM, pady=5)


        else:
            print('No file is chosen! Please choose a file')

    def imageUploader(self):
        filetypes = [('Image files', '*.png;*.jpg;*.jpeg')]
        path = tkinter.filedialog.askopenfilename(filetypes=filetypes)

        if len(path):
            img = Image.open(path)
            self.imw = img.width
            self.imh = img.height
            print(self.imw, self.imh)
            img = img.resize((200,200))
            pic = ImageTk.PhotoImage(img)

            self.lbl2.config(image=pic)
            self.lbl2.image = pic

            self.logo_btn.config(command=lambda: (self.logoUploader(img)))
            self.logo_btn.pack(side=tkinter.BOTTOM, pady=20)

        else:
            print('No file is chosen! Please choose a file')


window = Tk()

window.title('Image Watermarker App')
window.geometry('900x450')

app = App(window)

window.mainloop()
