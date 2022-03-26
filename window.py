import string
from tkinter import *
from tkinter import messagebox
import time
import pyautogui




win = Tk()

win.geometry("701x500")
win.configure(bg = "#ffffff")
win.title("Spammer")


spam_img = PhotoImage(file="spam.png")
win.iconphoto(False, spam_img)

canvas = Canvas(
    win,
    bg = "#ffffff",
    height = 500,
    width = 701,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    378.0, 147.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    362.0, 231.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#feecec",
    highlightthickness = 0)

entry0.place(
    x = 267.0, y = 201,
    width = 190.0,
    height = 58)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    362.0, 332.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#feecec",
    highlightthickness = 0)

entry1.place(
    x = 267.0, y = 302,
    width = 190.0,
    height = 58)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    362.0, 130.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#feecec",
    highlightthickness = 0)

entry2.place(
    x = 267.0, y = 100,
    width = 190.0,
    height = 58)


def label():
    response = messagebox.askokcancel(title="Spam!", message=f"The app will spam {entry2.get()} {entry0.get()} times after 5 seconds do you wish to proceed?")



    
    i=0
    if response == True:
        for i in range(int(entry0.get())):
            
            if str(entry1.get()) == "":
                messagebox.showerror(title="Error!",message="You have to write a number in the delay box if you don't want a delay you can write 0!")
                
            if type(entry1.get()) == string:
                messagebox.showerror(title="Error!",message="You have to write a number in the delay1!")
            else:
                time.sleep(5)
                pyautogui.write(f"{i}, {entry2.get()}")
                float(entry1.get())
                time.sleep(float(entry1.get()))
                

            pyautogui.press("enter")
            i+=1


    elif response == False:
        pass


img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = label,
    relief = "flat")

b0.place(
    x = 260, y = 403,
    width = 166,
    height = 45)

win.resizable(False, False)
win.mainloop()
