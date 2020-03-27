from tkinter import *
import webbrowser, os, easygui, PIL


def input_img():
    global input_file
    input_file = easygui.fileopenbox(filetypes=["*.png"])

    win = Tk()
    win.geometry('710x5')
    win.resizable(width=False, height=False)
    win.title('Изображение выбрано, можно закрыть данное окно и конвертировать в другие форматы')

    win.mainloop()


def p_n_g():
    img = PIL.Image.open(input_file)
    img.save('PNG_ConPic.png')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - PNG_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def j_p_g():
    img = PIL.Image.open(input_file)
    img.save('JPG_ConPic.jpg')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - JPG_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def b_m_p():
    img = PIL.Image.open(input_file)
    img.save('BMP_ConPic.bmp')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - BMP_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def g_i_f():
    img = PIL.Image.open(input_file)
    img.save('GIF_ConPic.gif')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - GIF_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def p_d_f():
    img = PIL.Image.open(input_file)
    img.save('PDF_ConPic.pdf')

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображение сохранено в корневую папку приложения под названием - PDF_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


root = Tk()
root.config(bg='lavender')
root.geometry('500x400')
root.resizable(width=False, height=False)
root.title('ConPic')

inpF = Button(root, text='Выбрать изображение (.png, .jpg и д.р.)')
inpF.config(width=55, height=2, bg='white smoke', command=input_img)
inpF.pack()


png = Button(root, text='.PNG')
png.config(width=15, height=2, bg='white', command=p_n_g)
png.place(x=15, y=55)

jpg = Button(root, text='.JPG')
jpg.config(width=15, height=2, bg='white', command=j_p_g)
jpg.place(x=190, y=55)

bmp = Button(root, text='.BMP')
bmp.config(width=15, height=2, bg='white', command=b_m_p)
bmp.place(x=365, y=55)

gif = Button(root, text='.GIF')
gif.config(width=15, height=2, bg='white', command=g_i_f)
gif.place(x=15, y=105)

pdf = Button(root, text='.PDF')
pdf.config(width=15, height=2, bg='white', command=p_d_f)
pdf.place(x=190, y=105)

root.mainloop()