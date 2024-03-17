from tkinter import *
root = Tk()

color1 = Label(root,text="one",bg="yellow")
color2 = Label(root,text="one",bg="royalblue")
color3 = Label(root,text="one",bg="red")
color1.pack()
color2.pack(fill=X)
color3.pack(side=LEFT,fill=Y)
root.mainloop()