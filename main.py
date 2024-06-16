from tkinter import *
from pygame import mixer


root = Tk()
root.title("Simple Piano")
root.geometry("500x500")
mixer.init()


def Do():
    mixer.music.load("sounds\do.mp3")
    mixer.music.play()
    indikator.config(text="Do")

def Re():
    mixer.music.load("sounds\Re.mp3")  
    mixer.music.play()
    indikator.config(text="Re")

def Mi(): 
    mixer.music.load("sounds\mi.mp3")  
    mixer.music.play()
    indikator.config(text="Mi")

def Fa(): 
    mixer.music.load("sounds\Fa.mp3")  
    mixer.music.play()
    indikator.config(text="Fa")

def Sol(): 
    mixer.music.load("sounds\sol.mp3")  
    mixer.music.play()
    indikator.config(text="Sol")

def La():
    mixer.music.load("sounds\lja.mp3")  
    mixer.music.play()
    indikator.config(text="La")

def Si(): 
    mixer.music.load("sounds\si.mp3")  
    mixer.music.play()
    indikator.config(text="Si")


Button(root, text="Do", width=25, height=100, bg="white", command=Do).pack(side="left")
Button(root, text="Re", width=25, height=100, bg="white",command=Re).pack(side="left")
Button(root, text="Mi", width=25, height=100, bg="white", command=Mi).pack(side="left")
Button(root, text="Fa", width=25, height=100, bg="white", command=Fa).pack(side="left")
Button(root, text="Sol", width=25, height=100, bg="white", command=Sol).pack(side="left")
Button(root, text="La", width=25, height=100, bg="white", command=La).pack(side="left")
Button(root, text="Si", width=25, height=100, bg="white", command=Si).pack(side="left")
Label(root, text="Simple Piano", font=("jokerman", 30)).pack(side="top")
Label(root, text="buttons clicked:", font=("Verdana", 10)).pack(side="top")
indikator = Label(root, text="~", font=("Bold", 50), bg="white", width=50, height=100)
indikator.pack(side="bottom")


root.mainloop()
