from tkinter import *


GUI = Tk()
frame= Frame(GUI,width=200,height=200)
buttom1= Button(frame,text="Thank you")
buttom2= Button(frame,text="Thank you")
buttom3= Button(frame,text="Thank you")
# buttom4= Button(frame,text="Thank you")

buttom1.pack(side=LEFT)
buttom2.pack(side=LEFT)
buttom3.pack(side=LEFT)
# buttom4.pack(side=LEFT)
frame.pack()
# middleframe=Frame(GUI)
# middleframe.pack(side=)
bottomframe = Frame(GUI)
buttom =Button(bottomframe,text="swich off")
buttom.pack()

bottomframe.pack(side=BOTTOM)
GUI.mainloop()


