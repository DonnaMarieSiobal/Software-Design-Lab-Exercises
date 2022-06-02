from tkinter import*
from tkinter import messagebox

count = 3
def login():
    username = entry1.get()
    pin = entry2.get()
    global count

    if (username== "" and pin==""):
        messagebox.showinfo("", "Blank Not Allowed")
    elif(username== "Donna" and pin=="2002"):
        messagebox.showinfo("", "login success")
    else:
        messagebox.showerror("Error", "Incorrect Username/Pin" + "\n   Attempts left: " + str(count - 1))
        count -= 1
    if count == 0:
        messagebox.showerror("Error", "   Incorrect Username/Pin" + "\nYou have too many attempts!! I'll call a police!")


root = Tk()
root.title("ATM Login")
root.geometry("500x300")

global entry1
global entry2

Label(root, text="Username:").place(x=110, y=63)
Label(root, text="Pin:").place(x=110, y=105)

entry1=Entry(root, bd=6)
entry1.place(x=200, y=60 )

entry2=Entry(root, bd=6)
entry2.place(x=200, y=100)

Button(root, text="Login", command=login, height=1, width=10, bd=6). place(x=200, y=150)

root.mainloop()