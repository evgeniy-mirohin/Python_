import getpass
import ldap3
from pprint import pprint
from tkinter import *
import sys
from tkinter import messagebox
from threading import Thread
    #############Переменные##
ad_name='OU=Users,OU=spb,OU=KATREN,DC=katren,DC=net'
server_win_uri = 'katren.net'
#search_filter = "(&(objectClass=person)(sAMAccountName=mirohinev)(sn=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))"
win_bind_name = "katren\\"+getpass.getuser()
#print ("Введите пароль: ")
#win_bind_passwd = getpass.getpass("Введите пароль(ввод не отображается): ")
win_bind_passwd =""
#attrs = ['*']
#attrs = ['name','telephoneNumber','description','department','mail','mailNickname','lastLogon','userAccountControl']


root = Tk()
w = root.winfo_screenwidth() # получаем ширину экрана
h = root.winfo_screenheight() # получаем высоту экрана
root.title("Запросы из AD")
root.geometry("400x600")        # задаем размеры окна
root.resizable(False, False) # запрещаем изменять размер окна

message = StringVar()   # чтобы заработал (.get)
GetPasswd = StringVar()   # чтобы заработал (.get)
ismarried = IntVar()
GetAtrtr = StringVar()
GetSearch = StringVar()
# # # # # # # # # # # # # # # # #

#######Классы#############
class windows:
    def __init__(self):
        top=self.top=Toplevel()
        top.title("введите пароль")
        top.geometry("200x100")
        l=Label(top,text="введите пароль")
        l.pack()
        e=Entry(top,show='*',textvariable=message)
        e.pack()
        b=Button(top,text='Ok',command = lambda:self.cleanup())
        b.pack()

    def cleanup(self):
    #message=e.get()
        #print("rtyuui")
        self.top.destroy()
        #top.destroy() 
    #top.destroy() 
       # print (message.get())

# # # # # # # # # #  # # # #  # # 



    ### Функции ######
def get_users_win_data(ip,search_base,search_filter,attrs,win_bind_name,win_bind_passwd):
    try:
        server = ldap3.Server('ldap://{}'.format(ip))
        with ldap3.Connection(server,user=win_bind_name,password=win_bind_passwd) as conn:
            conn.search(search_base, search_filter, attributes=attrs)
            return(conn.entries)
    except:
        print("Что-то пошло не так")

def write1():
    attrs = GetAtrtr.get().split(',')
    if attrs[0] == "":
        attrs = ['name','telephoneNumber','description','department','mail','mailNickname','lastLogon','userAccountControl']
    search_filter = str(GetSearch.get())
    if    search_filter == "":
        search_filter = "(&(objectClass=person)(sAMAccountName=*)(sn=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))"
    result=get_users_win_data(server_win_uri,ad_name,search_filter,attrs,win_bind_name,GetPasswd.get())
    len1=len(result)
    #En1.insert(0,len1)
    if len1 > 0:
        L4["text"] = "найдено записей: " + str(len1)
    else:
        L4["text"] = "не найдено записей"    
    #En1["text"] = "reter"
    f1 = open("AD_Result.txt", 'w')
    # f1.write(str(result[1]))
    for i in range(len1):
        f1.write(str(result[i]))
    f1.close()
    #thread1.join()

def Usercheck():
    if ismarried==0:
        EnUser.configure(state="normal")
    elif ismarried==1:
        EnUser.configure(state="readonly")

def WriteCSV():
    for i in range(len1):
        str(result[i])
    

def WriteXML():
    for i in range(len1):
        str(result[i])      



# # # # # # # # # #
thread1 = Thread(target=write1)

######## Элементы формы #########
L1 = Label(text="Укажите attrs")
L1.place(relx=.07, rely=.13)
L2 = Label(text="логин:")
L2.place(relx=.2, rely=.23)
L3 = Label(text="пароль:")
L3.place(relx=.2, rely=.28)
L4 = Label(text="")
L4.place(relx=.2, rely=.7)
L5 = Label(text="search_base")
L5.place(relx=.07, rely=.08)
Lsearch = Label(text="search_filter")
Lsearch.place(relx=.07, rely=.03)

En1 = Entry(justify=RIGHT)
En1.place(relx=.5, rely=.1, anchor="c")
#En1.insert(0,"ntcn")
EnUser = Entry(justify=LEFT,state="normal")
EnUser.place(relx=.5, rely=.25, anchor="c")
EnUser.insert(0,getpass.getuser())
EnUser.configure(state="normal")
EnPaswd = Entry(justify=RIGHT,show='*',textvariable=GetPasswd)
EnPaswd.place(relx=.5, rely=.3, anchor="c")
EnOtdel = Entry(justify=RIGHT,textvariable=GetAtrtr)
EnOtdel.place(relx=.5, rely=.15, anchor="c")
EnSearch = Entry(justify=RIGHT,textvariable=GetSearch)
EnSearch.place(relx=.5, rely=.05, anchor="c")

#btnGO = Button(text="GO",  command=lambda: windows())
#btnGO.place(relx=.6, rely=.4)
#btnPrint = Button(text="Print",  command = lambda:print(get_users_win_data(server_win_uri,ad_name,search_filter,attrs,win_bind_name,message.get())))
btnPrint = Button(text="Запрос",  command = lambda:thread1.start())
btnPrint.place(relx=.45, rely=.4)

Usercheckbutton = Checkbutton(text="запрос от текущего пользователя Windows", variable=ismarried,onvalue=0, offvalue=1,commmand=Usercheck())
#Usercheckbutton.place(relx=.1, rely=.22)

mainmenu = Menu(root) 
root.config(menu=mainmenu) 
 
filemenu = Menu(mainmenu, tearoff=0)
filemenu2 = Menu(filemenu, tearoff=0)
filemenu.add_command(label="настройка")
filemenu.add_cascade(label="Экспорт в...",menu=filemenu2)
filemenu.add_command(label="Импорт настроек")
filemenu.add_command(label="Выход")


filemenu2.add_command(label=".CSV")
filemenu2.add_command(label=".txt")
filemenu2.add_command(label=".xml")
filemenu2.add_command(label=".html")
filemenu2.add_command(label=".xls")
filemenu2.add_command(label="на дисплей")
 
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")
 
mainmenu.add_cascade(label="Файл",menu=filemenu)
mainmenu.add_cascade(label="Справка",menu=helpmenu)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
root.mainloop()


 
  
#data2=get_users_win_data(server_win_uri,ad_name,search_filter,attrs,win_bind_name,message.get())
#pprint(data2)