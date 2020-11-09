from tkinter import *
#переменные
PosX=0
PosY=100
i=1
h1=80 #высота кнопки
w1=100 #ширина кнопки
global ab
#ab="1"
a2=0 #временные переменные для расчетов

def click_button(a):
  # i+=1
   if a=="AC":
      L1['text']="0"
      return
   elif a=="Del":
      L1['text']= L1['text'][0:-1]
      return  
   elif len(L1['text']) > 20:
      return
   elif L1['text']=="0" or "":
      L1['text']= a
      return
   elif a=="+":
      ab=L1['text']
      L1['text']="0"
      print(type(ab))
      print(ab)
      return
        
   elif a =="=":
      print(ab)
      #L1['text']=str(int(L1['text'])+a1)
      #L1['text'] = eval(L1['text']+ab)
      return
   else:
      L1['text']= L1['text']+a

root = Tk()
w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
root.title("Калькулятор")
root.geometry("400x600")
root.resizable(False, False) # запрещаем изменять размер окна
#Label
L1 = Label(text="0", fg="black",  bg="white", font="Arial 24", justify=LEFT)
#кнопки

#btn = Button(text="Click Me",padx="55", pady="60", command=click_button)
btnPlus = Button(text="+",  command=lambda: click_button("+"))
btnMinus = Button(text="-",  command=lambda: click_button("-"))
btnAC = Button(text="AC",  command=lambda: click_button("AC"))
btnDel = Button(text="Del",  command=lambda: click_button("Del"))
btnDelen= Button(text="/",  command=click_button)
btnUmn = Button(text="*",  command=click_button)
btn0= Button(text="0", command=lambda: click_button("0"))
btn1= Button(text="1", command=lambda: click_button("1"))
btn2= Button(text="2", command=lambda: click_button("2"))
btn3= Button(text="3", command=lambda: click_button("3"))
btn4= Button(text="4", command=lambda: click_button("4"))
btn5= Button(text="5", command=lambda: click_button("5"))
btn6= Button(text="6", command=lambda: click_button("6"))
btn7= Button(text="7", command=lambda: click_button("7"))
btn8= Button(text="8", command=lambda: click_button("8"))
btn9= Button(text="9", command=lambda: click_button("9"))
btnRavno= Button(text="=", command=lambda: click_button("="))
btnProc= Button(text="%", command=click_button)
btnToth= Button(text=".", command=lambda: click_button("."))






#btn.place(x=100,y=200)
#btn.place(relx=.5, rely=.5, anchor="c", height=100, width=200, bordermode=OUTSIDE)
L1.place(height=100,width=400)
#L1.grid(row=2, column=2,sticky=E, ipadx=10, ipady=6)
btnDel.place(x=PosX+w1,y=PosY,height=h1, width=w1)
btnAC.place(x=PosX,y=PosY,height=h1, width=w1)
btnDelen.place(x=PosX+2*w1,y=PosY,height=h1, width=w1)
btnUmn.place(x=PosX+3*w1,y=PosY,height=h1, width=w1)
btn7.place(x=PosX+0,y=PosY+h1,height=h1, width=w1)
btn8.place(x=PosX+w1,y=PosY+h1,height=h1, width=w1)
btn9.place(x=PosX+2*w1,y=PosY+h1,height=h1, width=w1)
btnMinus.place(x=PosX+3*w1,y=PosY+h1,height=h1, width=w1)
btn4.place(x=PosX+0,y=PosY+2*h1,height=h1, width=w1)
btn5.place(x=PosX+w1,y=PosY+2*h1,height=h1, width=w1)
btn6.place(x=PosX+2*w1,y=PosY+2*h1,height=h1, width=w1)
btnPlus.place(x=PosX+3*w1,y=PosY+2*h1,height=h1, width=w1)
btn1.place(x=PosX+0,y=PosY+3*h1,height=h1, width=w1)
btn2.place(x=PosX+w1,y=PosY+3*h1,height=h1, width=w1)
btn3.place(x=PosX+2*w1,y=PosY+3*h1,height=h1, width=w1)
btnRavno.place(x=PosX+3*w1,y=PosY+3*h1,height=2*h1, width=w1)
btnProc.place(x=PosX,y=PosY+4*h1,height=h1, width=w1)
btn0.place(x=PosX+w1,y=PosY+4*h1,height=h1, width=w1)
btnToth.place(x=PosX+2*w1,y=PosY+4*h1,height=h1, width=w1)
#btnPlus.pack()

root.mainloop()