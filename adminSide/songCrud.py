from tkinter import *
from tkinter import filedialog
import os

root = Tk()
import pymysql.connections

# import mysql.connector
global conn, cursor
conn = pymysql.connect(host='localhost',
                       database='registerdb',
                       user='root',
                       password='')
cursor = conn.cursor()


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    print(filename)
    sql = "INSERT INTO track (track_id, song_name) VALUES (%s, %s)"
    val = (filename,'')
    cursor.execute(sql, val)
    print(cursor)
    cursor.close()
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
