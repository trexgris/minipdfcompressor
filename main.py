import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import subprocess
import PyPDF2

class Application(Tk):    
    def __init__(self):
       Tk.__init__(self)
       self.__create_widgets()
       self.config(menu=self.__menu_bar)
    def __browse_to_pdf(self):
        tmp_file = filedialog.askopenfile(parent=self,mode='rb',title='Choose a file', filetypes=[('PDF file', '*.pdf')])
        if tmp_file is not None:
            self.__file = tmp_file
            self.__pdf_name.set(os.path.basename(self.__file.name))
            tmp_file.close()
    def __compress_pdf(self, in_pdf):
        tmp_w_file = filedialog.asksaveasfilename(parent=self,  filetypes=[('PDF file', '*.pdf')], defaultextension='.pdf')
        if tmp_w_file is None or tmp_w_file == '':
            return
        writer = PyPDF2.PdfFileWriter()
        reader = PyPDF2.PdfFileReader(self.__file.name)
        for i in range(reader.numPages):
            page = reader.getPage(i)
            page.compressContentStreams()
            writer.addPage(page)
        with open(tmp_w_file, 'wb') as f:
            writer.write(f)
        f.close()
    def __create_widgets(self):
       self.__pdf_name = StringVar()
       #menu bar
       self.__menu_bar = Menu(master=self)
       self.filemenu = Menu(self.__menu_bar, tearoff=0)
       self.filemenu.add_command(label="New", command=self.__browse_to_pdf)
       self.__menu_bar.add_cascade(label="File", menu=self.filemenu)
       #selected pdf
       self.__pdf_name_label = Label(master=self, textvariable = self.__pdf_name)     
       self.__pdf_name_label.pack(side="top")
       # button compress to
       self.__button_compression = Button(master=self, text="Compress", command=lambda: self.__compress_pdf(self.__file.name))
       self.__button_compression.pack(side="right")
if __name__ == "__main__":
    ui = Application()
    ui.resizable(False, False)
    ui.geometry('120x80')
    ui.iconbitmap('test.ico')
    ui.mainloop()