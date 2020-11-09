from tkinter import *
import os

window = Tk()
window.title('Работа с canvas')
x1,y1,x2,y2=100,100,200,200
class snake:
	
#	def UseSnake(self,x1,y1):	
	def __init__(self,x1,y1):	
	#	x1=100
	#	y1=50
		x2=x1+100
		y2=y1+100
		color="white"
		colorline="blue"
		canvas.create_rectangle(x1,y1,x2,y2,fill=color,outline= colorline)
		canvas.pack()
def control():
#	if btn =="up":
	canvas.move(150,150,400,400,fill="white",outline="blue")
#	elif btn =="down":
	canvas.move(200,150,300,300,fill="white",outline="blue")
	tk.update()
	canvas.pack()

	
La1 = Label(text="0", fg="black",  bg="white", font="Arial 24", justify=RIGHT)
#L1.place(height=400,width=1100)
canvas = Canvas(window,width=700,height=700,bg="gray",cursor="pencil")
btnUp = Button(text="up",  command=lambda: control())
btnDown= Button(text="down",  command=lambda: control("down"))


#canvas.create_line(0,0,600,600,width=5,fill="yellow")
#canvas.create_line(0,600,600,0,width=5,fill="yellow")
btnUp.place(x=350,y=800,height=150, width=200)
btnDown.place(x=350,y=1100,height=150, width=200)
snk=canvas.create_rectangle(x1,y1,
x2,y2,fill="white",outline="blue")
canvas.pack()
#os.system('clear')
window.mainloop()

tk.update()