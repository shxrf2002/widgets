from tkinter import *

window = Tk()

window.geometry("500x500")

window.title("Widgets")

'''
5 WIDGETS 

1) LABEL --> to display a text
2) BUTTON --> to create a button
3) ENTRY --> to create a text box where one line can be written
4) TEXT --> a text box where multiple lines can be created
5) FRAME --> for holding the other widgets
'''

lab = Label(master=window,text="This is a label",fg="white",bg="green")
lab.pack()

btn=Button(master=window,text="hi",fg="blue",bg="yellow")
btn.pack()

en=Entry(master=window,fg="black",bg="white")
en.pack()
t=Text(master=window,bg="yellow")


#fg = foreground(colo of the text)
#bg = background(bakground color of the widget)

l1 = Label(master=window,text="Enter your name")
name = Entry(master=window)

def message():
    #to get the user input from the entry
    get_name = name.get()
    display = "Hello, "+get_name+" you have successfully created your first tkinter window"

    #to inser the message inside the textbox
    t.insert(END,display)
register = Button(master=window,text="Register",command=message)

l1.pack()
name.pack()
register.pack()
t.pack()
window.mainloop()