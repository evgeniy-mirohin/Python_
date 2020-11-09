from tkinter import *
#переменные
PosX=0
PosY=100
i=1
h1=80 #высота кнопки
w1=100 #ширина кнопки
#ab="1"
a2=0 #временные переменные для расчетов

def click_button(a):
  global a1,b1
  if a== "AC":
  	L1['text']= "0"
  	return
  elif a=="Del":
  #	d1=()
  	L1['text']=L1['text'][0:-1]
  	return
  elif a== "+":
  	b1=a
  	a1=float(L1['text'])
  	L1['text']="0"
  	return
  elif a== "-":
  	b1=a
  	a1=float(L1['text'])
  	L1['text']="0"
  	return
  elif a=="*":
  	b1=a
  	a1=float(L1['text'])
  	L1['text']="0"
  	return
  elif a== "/":
  	b1=a
  	a1=float(L1['text'])
  	L1['text']="0"
  	return
  elif a== "%":
  	if b1=="+":
  		L1['text'] = str(a1+int(L1['text'])*a1/100)
  	elif b1=="-":
  		L1['text'] = str(a1-int(L1['text'])*a1/100)
  	elif b1=="*":
  		L1['text'] = str(a1*(int(L1['text'])*a1/100))
  	elif b1=="/":
  		L1['text'] = str(a1/(int(L1['text'])*a1/100)) 	
  	return
  elif a== "=":
  	if b1=="+":
  		L1['text'] = '{0:.11f}'.format(a1+float(L1['text'])).rstrip('0').rstrip('.')
  	elif b1=="-":
  		L1['text'] = '{0:.11f}'.format(a1-float(L1['text'])).rstrip('0').rstrip('.')
  	elif b1=="*":
  		L1['text'] = '{0:.11f}'.format(a1*float(L1['text'])).rstrip('0').rstrip('.')
  	elif b1=="/":
  		L1['text'] = '{0:.11f}'.format(a1/float(L1['text'])).rstrip('0').rstrip('.')
      #  '{0:.2f}'.format(num).rstrip('0').rstrip('.')	
  	return	
  elif L1['text']=="0":
  	   L1['text']= a
  	   return
  if len(L1['text'])<15:
      #print (S.find(L1['text']))
      if a== "." and L1['text'].find(".") > 0:
         return
      L1['text']=L1['text']+a

root = Tk()
w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
root.title("Калькулятор")
root.geometry("400x600")
root.resizable(False, False) # запрещаем изменять размер окна
#Label
L1 = Label(text="0", fg="black",  bg="white", font="Arial 24", justify=LEFT)
#кнопки

btnPlus = Button(text="+",  command=lambda: click_button("+"))
btnMinus = Button(text="-",  command=lambda: click_button("-"))
btnAC = Button(text="AC",  command=lambda: click_button("AC"))
btnDel = Button(text="Del",  command=lambda: click_button("Del"))
btnDelen= Button(text="/",  command=lambda: click_button("/"))
btnUmn = Button(text="*",  command=lambda: click_button("*"))
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
btnProc= Button(text="%", command=lambda: click_button("%"))
btnToth= Button(text=".", command=lambda: click_button("."))



L1.place(height=100,width=400)
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

root.mainloop()