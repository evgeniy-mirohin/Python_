#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import getpass
import ldap3
from pprint import pprint
from tkinter import *
import sys

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
w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
root.title("Запросы из AD")
root.geometry("400x600")
#root.resizable(False, False) # запрещаем изменять размер окна
### Функции ######
def get_users_win_data(ip,search_base,search_filter,attrs,win_bind_name,win_bind_passwd):
    server = ldap3.Server('ldap://{}'.format(ip))
    with ldap3.Connection(server,user=win_bind_name,password=win_bind_passwd) as conn:
        conn.search(search_base, search_filter, attributes=attrs)
        return(conn.entries)

def GO():
    top=Toplevel()
    top.geometry("200x100")
    l=Label(top,text="введите пароль")
    l.pack()
    e=Entry(top)
    e.pack()
    b=Button(top,text='Ok',command=cleanup)
    b.pack()

def cleanup():
    value=e.get()
    top.destroy()    
# # # # # # # # # #


######## Элементы формы #########
L1 = Label(text="укажите параметры которые отображать, *=все")
L1.place(relx=.1, rely=.0)
L2 = Label(text="введите пароль")
L2.place(relx=.2, rely=.15)
En1 = Entry(justify=RIGHT)
En1.place(relx=.5, rely=.1, anchor="c")
EnPasswd = Entry(justify=RIGHT)
EnPasswd.place(relx=.5, rely=.2, anchor="c")
btnGO = Button(text="GO",  command=lambda: GO())
btnGO.place(relx=.6, rely=.3)




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
root.mainloop()


 
  
data2=get_users_win_data(server_win_uri,ad_name,search_filter,attrs,win_bind_name,win_bind_passwd)
pprint(data2)