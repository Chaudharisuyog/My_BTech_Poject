from tkinter import *

window = Tk() 

PhotoImage = PhotoImage(file='C:\\Users\\HP\\Downloads\\coding.jpeg')
label = Label(window,
              text="Hello World",
              font=('Arial',40,'bold'),
              fg='green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image='PhotoImage')
label.pack()
window.mainloop()