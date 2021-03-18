import os
import time
import pyperclip as pc
import string
import tkinter
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox as mg
from EasyCode.EasyCode import get_all_drives
available_drives = get_all_drives()
available_drives.insert(0, "Select")
available_drives.append("Desktop")
class App:
    search_over = False
    def __init__(self, root):
        # initilizing the root as a part of class
        self.root = root
        # making initial size of the root
        self.root.geometry("500x250+510+250")
        # Setting apps title 
        self.root.title("File Finder")
        ################ Row 1 ####################
        self.label1 = Label(self.root, text="Disk:", font=("times new roman", 20))
        self.label1.place(x=80, y=50)
        self.com = Combobox(self.root, state="readonly",font = ("times new roman", 15))
        self.com.place(x=200, y = 50)
        self.com['values'] = available_drives
        self.com.current(0)
        ################ Row 2 ######################
        self.label2 = Label(self.root, text="Filename: ", font=("times new roman", 20))
        self.label2.place(x = 80, y=120)
        self.text = Entry(self.root, font=("times new roman", 20), bg="lightgray", fg="black")
        self.text.place(x=200, y=120, width=250)
        ################ Creating a button for search #########################
        self.button = Button(self.root, text="Search ",bd=3, relief=RAISED, command=self.get_info)
        self.button.place(x=190, y=200, width=150)
        

    def get_info(self):
        
        drive = self.com.get()+"\\"
        if "desktop" in drive.lower():
            drive = os.path.join(os.environ['USERPROFILE'], "Desktop")
        filename = self.text.get()
        self.search(drive, filename)


    def search(self, drive, fn):
        self.var = StringVar()
        self.var.set("Searching...")
        
        self.label3 = Label(self.root, textvariable=self.var, font=("times new roman", 10))
        self.label3.place(x=0,y=220)
        self.root.update()
        time.sleep(0.8)
        
        self.drive = drive 
        self.fn = fn
        for root, dirs, files in os.walk(drive):
            for file in files:
                filename = file
                path_of_file = os.path.join(root, file)
                if fn.lower() in filename.lower():
                    self.search_over = True
                    os.startfile(path_of_file)
                    mg.showinfo("Succes", f"""
                    File was found
                    The file was located in :  {root}
                    The path of the file is :  {path_of_file}""")
                    pc.copy(root)
                    self.var.set("Completed")
                    self.root.update()
                    return

        mg.showerror("No file found", "No such file found")
    def animate(self):
        no=0
        while not self.search_over:
            if no==0:
                self.var.set("Searching.")
                self.root.update()
                time.sleep(0.8)
                no+=1
            elif no==1:
                self.var.set("Searching..")
                self.root.update()
                time.sleep(0.8)
                no+=1
            elif no==2:
                self.var.set("Searching...")
                self.root.update()
                time.sleep(0.8)
                no = 0
                    
root = Tk()
app = App(root)
root.mainloop()
