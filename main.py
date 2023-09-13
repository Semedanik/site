from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from ttkbootstrap.constants import *
import ttkbootstrap as tb
#все эти библиотеки надо скачать

root = tb.Window(themename="superhero")
#root = Tk() - для меня(забейте)
root.title("Our Project")


root.iconbitmap("c:/images/favicon.ico")

root.geometry("400x500+700+500")
root.resizable(width=False, height=False)


my_label = tb.Label(text="Главная", font=("Helvetica",28), bootstyle="default")
my_label.pack(pady=50)

#здесь папочка откуда он достает фото
def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='/images', title="Выберите файл",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Выберите изображение",width=25,height=5,bg="blue",fg="yellow", command=open).pack()





root.mainloop()