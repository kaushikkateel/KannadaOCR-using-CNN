
#  Created by Kaushik Kateel on 4/05/19.
#  Copyright © 2019 Kaushik Kateel. All rights reserved.

import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import process
import predictor


HEIGHT = 500
WIDTH = 1000
flag = False

data =str()
root = tk.Tk(className=' KANNADA TEXT ANALYSER')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,)
canvas.pack()

frame = tk.Frame(root, bg='#339cff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.1, anchor='n')


fnamelbl = tk.Label(frame, font=40, text="")
fnamelbl.place(relwidth=0.37, relheight=1) 



def filedialogFunc():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select an image", filetype=[("jpeg","*.jpeg"),("png","*.png"),("jpg","*.jpg"),("All files", "*.*")])
    basefilename = os.path.basename(filename)
    fnamelbl.configure(text=basefilename)
    print(type(filename))
    setStatus()
    

    
button1 = tk.Button(frame, text="Upload", font=40, command= filedialogFunc)
button1.place(relx=0.38, relheight=1, relwidth=0.2)

def getData():
    global final_text
    final_text = process.processor(filename)
    flag = True
    printt()
    setStatus()
    button3['state'] = tk.ACTIVE
    

button2 = tk.Button(frame, text="Get data", font=40, command=getData)
button2.place(relx=0.59, relheight=1, relwidth=0.2)
button2['state'] = tk.DISABLED

# def analyseFunc():
#     print("done")
#     print(filename)
#     printt()

def saveFunc():
    f = filedialog.asksaveasfile(mode="wb", defaultextension=".txt")
    if f is None:
        return
    result = final_text.encode("utf-8")

    # res = result.decode('utf-8')

    f.write(result)
    # f.close()
    setStatus()


button3 = tk.Button(frame, text="Save as text file", font=40, command=saveFunc)
button3.place(relx=0.80, relheight=1, relwidth=0.2)
button3['state'] = tk.DISABLED

def setStatus():
    print(filename)
    if(not filename):
        button2['state'] = tk.DISABLED
        
       
    else:
        button2['state'] = tk.ACTIVE
      
        
        
    # if(not flag):
    #     button3['state'] = tk.DISABLED
    # else:
    #     button3['state'] = tk.ACTIVE
                             


lower_frame = tk.Frame(root, bg='#339cff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.7, anchor='n')


# def saveFunc():
#     f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
#     if f is None:
#         return
#     f.write(final_text)
#     setStatus()
    
# button4 = tk.Button(lower_frame, text="Save text", font=40, command = saveFunc)
# button4.place(relx=0.85 ,rely=0.9, relheight=0.1, relwidth=0.15)
# button4['state'] = tk.DISABLED
	
def printt():
	# data=str()
	# f=open("C:\\Users\\bhatk\\output.txt", encoding = "utf8")
	# data = b'\xe0\xb2\x87'
	# f.close()
    # result , i = predictor.predict("./seg_img/img1_1_1.jpeg")

    # res = result.decode('utf-8')
    result = final_text.encode("utf-8")

    res = result.decode('utf-8')

    label = tk.Label(lower_frame, bd=3, text=res, bg='#cce6ff', fg='#000000')

    label.place(relx=0.0,rely=0.0, relheight=1, relwidth=1)

    label.config(font = ("Courier",12))

root.mainloop()

