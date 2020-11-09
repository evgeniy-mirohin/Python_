from tkinter import *

class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Цвета")
        self.pack(fill=BOTH, expand=1)
 
        canvas = Canvas(self)
        canvas.create_rectangle(
            30, 10, 120, 80,
            outline="#fb0", fill="#fb0"
        )
 
        canvas.create_rectangle(
            150, 10, 240, 80,
            outline="#f50", fill="#f50"
        )
 
        canvas.create_rectangle(
            270, 10, 370, 80,
            outline="#05f", fill="#05f"
        )
 
        canvas.pack(fill=BOTH, expand=1)
 
 
def main():
 #   root = Tk()
    ex = Example()
    root.geometry("400x100+300+300")
    root.mainloop()
 root = Tk()

 btn1 = Button(text="кнопка 1",  command=lambda: main())
 btn1.place(x=300,y=300)
#if __name__ == '__main__':
#    main()