from tkinter import *
import webbrowser, os, easygui, PIL


def input_img():
    global input_file
    input_file = easygui.fileopenbox(filetypes=["*.png"], multiple=True)

    win = Tk()
    win.geometry('710x5')
    win.resizable(width=False, height=False)
    win.title('Изображения выбраны, можно закрыть данное окно и конвертировать в другие форматы')

    win.mainloop()


def p_n_g():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.save(str(num) + 'PNG_ConPic.png')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - PNG_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def j_p_g():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.save(str(num) + 'JPG_ConPic.jpg')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - JPG_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def b_m_p():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.save(str(num) + 'BMP_ConPic.bmp')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - BMP_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def g_i_f():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.save(str(num) + 'GIF_ConPic.gif')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - GIF_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def p_d_f():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.save(str(num) + 'PDF_ConPic.pdf')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - PDF_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def we_bp():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.save(str(num) + 'WebP_ConPic.webp')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - WebP_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def ult_ra():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.thumbnail((3840, 2160))
        img.save(str(num) + '_ULTRA_ConPic.png')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - ULTRA_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def fu_ll():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.thumbnail((1920, 1080))
        img.save(str(num) + '_FULL_ConPic.png')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - FULL_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def h_d():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.thumbnail((1280, 720))
        img.save(str(num) + '_HD_ConPic.png')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - HD_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def p_480():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.thumbnail((854, 480))
        img.save(str(num) + '_480p_ConPic.png')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - 480p_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def p_360():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.thumbnail((480, 360))
        img.save(str(num) + '_360p_ConPic.png')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - 360p_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def p_240():
    num = 1
    for i in input_file:
        img = PIL.Image.open(i)
        img.thumbnail((320, 240))
        img.save(str(num) + '_240p_ConPic.png')
        num += 1

    win = Tk()
    win.geometry('650x5')
    win.resizable(width=False, height=False)
    win.title('Изображения сохранены в корневую папку приложения под названием - 240p_ConPic')

    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir)

    win.mainloop()


def u_r_l():
    webbrowser.open('https://vk.com/serv_studio')


root = Tk()
root.config(bg='lavender')
root.geometry('500x350')
root.resizable(width=False, height=False)
root.title('ConPic')
root.iconbitmap('data\\icon.ico')

inpF = Button(root, text='Выбрать изображения (.png, .jpg и д.р.)')
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

webp = Button(root, text='.WebP')
webp.config(width=15, height=2, bg='white', command=we_bp)
webp.place(x=365, y=105)

ultra = Button(root, text='''Сжать до
Ultra HD''')
ultra.config(width=15, height=2, bg='white', command=ult_ra)
ultra.place(x=15, y=155)

full = Button(root, text='''Сжать до
Full HD''')
full.config(width=15, height=2, bg='white', command=fu_ll)
full.place(x=190, y=155)

hd = Button(root, text='''Сжать до
HD''')
hd.config(width=15, height=2, bg='white', command=h_d)
hd.place(x=365, y=155)

p480 = Button(root, text='''Сжать до
480p''')
p480.config(width=15, height=2, bg='white', command=p_480)
p480.place(x=15, y=205)

p360 = Button(root, text='''Сжать до
360p''')
p360.config(width=15, height=2, bg='white', command=p_360)
p360.place(x=190, y=205)

p240 = Button(root, text='''Сжать до
240p''')
p240.config(width=15, height=2, bg='white', command=p_240)
p240.place(x=365, y=205)

textt = Label(root, text='''Запрещено сжимать до разрешений,
которые больше разрешения изображения''', bg='lavender', fg='gray')
textt.config(font=('Times', 14))
textt.place(x=80, y=250)

info = Label(root, text='Создано: Матвей Воронцов | Service Studio', fg='gray', bg='lavender')
info.config(font=('Arial', 9))
info.place(x=250, y=330)

url = Button(root, text='Страница разработчика')
url.config(width=20, height=1, bg='white', command=u_r_l)
url.place(x=1, y=325)

root.mainloop()