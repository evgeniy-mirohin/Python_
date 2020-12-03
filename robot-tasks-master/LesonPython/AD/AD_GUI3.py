import getpass
import ldap3
from pprint import pprint
from tkinter import *
import sys
from tkinter import messagebox
    #############Переменные##
ad_name='OU=Users,OU=spb,OU=KATREN,DC=katren,DC=net'
server_win_uri = 'katren.net'
search_filter = "(&(objectClass=person)(sAMAccountName=*)(sn=*))"
win_bind_name = 'katren\mirohinev'
#print ("Введите пароль: ")
#win_bind_passwd = getpass.getpass("Введите пароль(ввод не отображается): ")
win_bind_passwd =""
#attrs = ['*']
attrs = ['name','telephoneNumber','description','department','mail','mailNickname']


root = Tk()
w = root.winfo_screenwidth() # получаем ширину экрана
h = root.winfo_screenheight() # получаем высоту экрана
root.title("Запросы из AD")
root.geometry("400x600")        # задаем размеры окна
#root.resizable(False, False) # запрещаем изменять размер окна

message = StringVar()   # чтобы заработал (.get)
# # # # # # # # # # # # # # # # #

#######Классы#############
class windows:
    def __init__(self):
        top=self.top=Toplevel()
        top.title("введите пароль")
        top.geometry("200x100")
        l=Label(top,text="введите пароль")
        l.pack()
        e=Entry(top, textvariable=message)
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
    server = ldap3.Server('ldap://{}'.format(ip))
    with ldap3.Connection(server,user=win_bind_name,password=win_bind_passwd) as conn:
        conn.search(search_base, search_filter, attributes=attrs)
        return(conn.entries)

def write1():
    #print (message.get())
    result=get_users_win_data(server_win_uri,ad_name,search_filter,attrs,win_bind_name,message.get())
   # messagebox.showinfo("GUI Python", len(result))
    En1.insert(0,len(result))
    #En1["text"] = "reter"
    f1 = open("AD_Result.txt", 'w')
    f1.write()
    f1.close()


      
# # # # # # # # # #


    ######## Элементы формы #########
L1 = Label(text="укажите параметры которые отображать * = все")
L1.place(relx=.1, rely=.0)
L2 = Label(text="введите пароль")
L2.place(relx=.2, rely=.15)
En1 = Entry(justify=RIGHT)
En1.place(relx=.5, rely=.1, anchor="c")
#En1.insert(0,"ntcn")
EnPasswd = Entry(justify=RIGHT)
EnPasswd.place(relx=.5, rely=.2, anchor="c")
btnGO = Button(text="GO",  command=lambda: windows())
btnGO.place(relx=.6, rely=.3)
#btnPrint = Button(text="Print",  command = lambda:print(get_users_win_data(server_win_uri,ad_name,search_filter,attrs,win_bind_name,message.get())))
btnPrint = Button(text="Print",  command = lambda:write1())
btnPrint.place(relx=.5, rely=.3)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
root.mainloop()


 
  
#data2=get_users_win_data(server_win_uri,ad_name,search_filter,attrs,win_bind_name,message.get())
#pprint(data2)