from tkinter import *
from tkinter import filedialog
import os
root = Tk()
import pymysql.connections



def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    print(filename)

    file = open(filename, errors="ignore")
    file_data = file.read()
    file.close()
    file_name = os.path.basename(filename)
    file1 = open(file_name, 'w+')

    file1.writelines(file_data)


button = Button(root, text='Upload', command=UploadAction, bg="yellow", fg="black")
button.pack()

pathlabel = Label(root)
pathlabel.pack()

root.mainloop()
