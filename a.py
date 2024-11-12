from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()

root.title("Welcome")
root.configure(bg= "light blue")
#root.geometry("650X400")

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

l1 = Label(root, image = image)
l1.place(x=180, y=20)

l2 = Label(root, text = "Hey user welcome to denomination application counter", bg= "light blue" )
l2.place(relx= 0.5, y= 340, anchor=CENTER)

def msg():
    msgbox = messagebox.showinfo("Alert","Do you want to calculate the denomination count?")
    if msgbox == "ok":
        topwin()

b1 = Button(root, text= "Lets get started", command = msg, bg="brown", fg= "white")
b1.place(x = 260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination counter")
    top.configure(bg = "lightgrey")
    #top.geometry("600X350+50+50+50")

    L1 = Label(root, text = "Enter total amount", bg="lightgrey")
    entry = Entry(top)
    L2 = Label(root, text = "Here are the num of notes for each denomination", bg="lightgrey")

    L3 = Label(top, text="2000", bg="lightgrey")
    L4 = Label(top, text="500", bg="lightgrey")
    L5 = Label(top, text="100", bg="lightgrey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculate():
        try:
            global amount
            amount = int(entry.get())

            n1 = amount//2000
            amount%=2000

            n2 = amount//500
            amount%=500

            n3 = amount//100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(n1))
            t2.insert(END,str(n2))
            t3.insert(END,str(n3))

        except ValueError:
            messagebox.showerror("ERROR", "Please enter a valid number.")
        
    
    b2 = Button(top, text= "Calculate", command= calculate, bg="brown", fg="white")

    L1.place(x = 230, y=50)
    L2.place(x= 140, y=170)
    L3.place(x = 180, y=200)
    L4.place(x = 180, y=230)
    L5.place(x = 180, y=260)

    entry.place(x = 200, y= 80)
    b2.place(x=240, y=120)

    t1.place(x = 270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()


root.mainloop()