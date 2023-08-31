from tkinter import *
#creating buttons
root = Tk() #creates a window
root.geometry('1000x1000')

lb1 = Label(root, text = "ARE YOU READY TO PLAY QUEST FOR TREASURE?",bg="red",fg="white",width='100',height='10')
lb1.pack()



def myClick():
     message = " let's begin the game"
     lb4 = Label(root, text = message,bg="purple",fg='white',width='50',height='10')
     lb4.pack()

bt1 = Button(root, text = "Start Game",width='20',height='10', command = myClick,bg = "blue",fg = "white")#callback
bt1.pack()


