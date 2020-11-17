#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import getpass
import ldap3
from pprint import pprint
from tkinter import *

ad_name='OU=Users,OU=spb,OU=KATREN,DC=katren,DC=net'
server_win_uri = 'katren.net'
search_filter = "(&(objectClass=person)(sAMAccountName=*)(sn=*))"
win_bind_name = 'katren\mirohinev'
#print ("Введите пароль: ")
win_bind_passwd = getpass.getpass("Введите пароль(ввод не отображается): ")
#attrs = ['*']
attrs = ['name','telephoneNumber','description','department','mail','mailNickname']
def get_users_win_data(ip,search_base,search_filter,attrs,win_bind_name,win_bind_passwd):
    server = ldap3.Server('ldap://{}'.format(ip))
    with ldap3.Connection(server,user=win_bind_name,password=win_bind_passwd) as conn:
        conn.search(search_base, search_filter, attributes=attrs)
        return(conn.entries)
 
  
data2=get_users_win_data(server_win_uri,ad_name,search_filter,attrs,win_bind_name,win_bind_passwd)
pprint(data2)