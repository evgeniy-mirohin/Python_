import getpass
import ldap3
#from pprint import pprint
from tkinter import *
import sys
#from tkinter import messagebox
from threading import Thread
import csv
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


def Usercheck():
    if ismarried==0:
        EnUser.configure(state="normal")
    elif ismarried==1:
        EnUser.configure(state="readonly")

def Consolidate():
    attrs = GetAtrtr.get().split(',')
    if attrs[0] == "":
        attrs = ['name','telephoneNumber','description','department','mail','mailNickname','lastLogon','userAccountControl']
    search_filter = str(GetSearch.get())
    if    search_filter == "":
        search_filter = "(&(objectClass=person)(sAMAccountName=*)(sn=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))"
    result=get_users_win_data(server_win_uri,ad_name,search_filter,attrs,win_bind_name,GetPasswd.get())
    #thread1.join()
    len1=len(result)
    if len1 > 0:
        L4["text"] = "найдено записей: " + str(len1)
    else:
        L4["text"] = "не найдено записей"    
    i=0
    #k=0
    global letter2,UserFull
    UserFull=[]
    for k in range(len1-1):
        user = result[k]
        user=str(user)
        userPr = user.split('\r\n')
        LenUserPr = len(userPr)
        if userPr[LenUserPr-1] == '':
            userPr.pop()
        for i in range (1,LenUserPr-1):
            UserKey = userPr[i] 
            UsersKey = UserKey.split(': ')
            UsersKeyLen = len(UsersKey)
            for j in range (UsersKeyLen-1):
                if j == 0: 
                    UserKey1 = UsersKey[j]
                    UserKey1=UserKey1.replace(' ','')
                    UsersKey[j] =UserKey1
            if i == 1:
                User2 = dict.fromkeys([UsersKey[0]] ,UsersKey[1])
            else:
                User2[UsersKey[0]] = UsersKey[1] 
        UserFull.append(User2)
    letter2 = UserFull[0].keys()
    letter2= list(letter2)
    letter2 = UserFull[0].keys()
    letter2= list(letter2)
    print(UserFull)

   # WriteCSV(result,len1)


def WriteCSV(result,len1):
    #for i in range(len1):
    i=0
    #j=0
    k=0
    UserFull=[]
    for k in range(len1-1):
        user = result[k]
        user=str(user)
        userPr = user.split('\r\n')
        LenUserPr = len(userPr)
        if userPr[LenUserPr-1] == '':
            userPr.pop()
        #print("LenUserPr = " + str(LenUserPr))
        #print("userPr = " + str(userPr))
        for i in range (1,LenUserPr-1):
           # print("i= "+ str(i))
            UserKey = userPr[i] 
            #if i > 0: 
            #   UserKey = UserKey.replace(' ','')
            #   userPr[i]  = UserKey
            #print(userPr[i])
            #UserKey = UserKey[i]
            UsersKey = UserKey.split(': ')
            #print('UsersKey ' + str(UsersKey))
            UsersKeyLen = len(UsersKey)
            #print('UsersKeyLen= ' + str(UsersKeyLen))
            for j in range (UsersKeyLen-1):
              #  print('j= '+str(j))
                if j == 0: 
                # print(UsersKey)
                # print(UserKey[j])
                    UserKey1 = UsersKey[j]
                    UserKey1=UserKey1.replace(' ','')
                # print('UserKey1= '+ str(UserKey1))  
                    UsersKey[j] =UserKey1
            #a1=UsersKey[0]         
            #a2=UsersKey[1]
        # print(UsersKey)
            if i == 1:
                User2 = dict.fromkeys([UsersKey[0]] ,UsersKey[1])
            # print(User2)
            else:
                User2[UsersKey[0]] = UsersKey[1] 
       # print('User2 = ' + str(User2))
        UserFull.append(User2)
    #print(UserFull)
            #User2 = {UsersKey[0]=UsersKey[1]}
                #print(UsersKey)
            #    UsersKey[i][j] = UserKey[j]
            #    print (UsersKey[i][j])

                #print(UserKey)
       #print(thread1.is_alive)
       #letter1= UserFull[0]
   # letter2 = UserFull[0].keys()
  #  letter2= list(letter2)
    #print(UserFull[0])

    #with open("classmates.csv", "w", newline="") as file:

        
        #letter1= UserFull[0]
    letter2 = UserFull[0].keys()
    letter2= list(letter2)
        #print(UserFull[0])
    print(UserFull[len(UserFull)-1])

    with open("classmates.csv", "w", newline='') as csv_file:
        file_writer = csv.DictWriter(csv_file, delimiter = ";", lineterminator="\r", fieldnames=letter2)
        file_writer.writeheader()
        file_writer.writerows(UserFull)     
            
def WriteCSV1():
    with open("classmates.csv", "w", newline='') as csv_file:
        file_writer = csv.DictWriter(csv_file, delimiter = ";", lineterminator="\r", fieldnames=letter2)
        file_writer.writeheader()
        file_writer.writerows(UserFull)     

def WriteXML():
    for i in range(len1):
        str(result[i])      

def WriteTXT1():
    print("def WriteTXT() \t запущена")
    f1 = open("AD_Result.txt", 'w')
    len4=len(letter2)
    len1=len(UserFull)
    for i in range (len4-1):
        f1.write(str(letter2[i])+ "\t")
    for i in range(len1-1):
        f1.write(str(UserFull[i]) + "\r")
    f1.close() 

def WriteTXT():
    with open("classmates.txt", "w", newline='') as csv_file:
        file_writer = csv.DictWriter(csv_file, delimiter = "\t", lineterminator="\r", fieldnames=letter2)
        file_writer.writeheader()
        file_writer.writerows(UserFull)  

# # # # # # # # # #
thread1 = Thread(target = Consolidate)

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

btnGO = Button(text="GO",  command=lambda: WriteTXT())
btnGO.place(relx=.6, rely=.4)
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


filemenu2.add_command(label=".CSV", command=WriteCSV1)
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