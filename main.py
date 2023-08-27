from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width =500, height=300)
window.config(padx=20,pady=50)

#Label
my_label = Label(text="I am a label", font=("Times", 24, "bold"))
my_label.grid(column=0,row=0)




#Button

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command =button_clicked)
button.grid(column=1,row=1)

button_2 =Button(text="New button")
button_2.grid(column=2,row=0)

#Entry
input = Entry(width=10)
input.grid(column=4,row=3)




window.mainloop()