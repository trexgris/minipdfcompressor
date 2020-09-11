import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os

import youtube_dl

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',       
    'outtmpl': '%(id)s',        
    'progress_hooks': [my_hook],  
}

class Application(Tk):    
    def __init__(self):
       Tk.__init__(self)
       self.__create_widgets()
       self.config(menu=self.__menu_bar)

    def __browse_to_pdf(self):
        file = filedialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        if file != None:
            self.__pdf_name.set(os.path.basename(file.name))
            file.close()
            self.update_idletasks



    def __create_widgets(self):
       self.__pdf_name = StringVar()
    #menu bar
       self.__menu_bar = Menu(master=self)
       self.filemenu = Menu(self.__menu_bar, tearoff=0)
       self.filemenu.add_command(label="New", command=self.__browse_to_pdf)
       self.__menu_bar.add_cascade(label="File", menu=self.filemenu)
       self.__menu_bar.add_command(label="About", command=None)

    #playlist link
       self.__pdf_name_label = Label(master=self, textvariable = self.__pdf_name)
       self.__pdf_name_label.pack(side="top")
     #  self.__pdf_name_label.pack(side="top")
       self.update()    





if __name__ == "__main__":
    ui = Application()
    ui.mainloop()