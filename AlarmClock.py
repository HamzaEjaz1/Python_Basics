from tkinter import *
root = Tk()

root.title("Alarm Clock")
root.geometry("530x330")
head = Label(root , text="Alaram CLock" , font=('comic sans ', 20))
head.grid(row=0 , columnspan=3)

clockimage = PhotoImage(file="a1.png")
img = Label(root, image=clockimage)
img.grid(rowspan=4 , column=0)
inputt = Label(root , text="input Time" , font=("comic snas " , 15))
inputt.grid(row=1, column=1)
altime =Entry(root, font=("comic snas " , 15) , width=50)
altime.grid(row=1, column=2)




root.mainloop()