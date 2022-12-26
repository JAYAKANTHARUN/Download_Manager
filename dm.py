from tkinter import *
import tkinter as tk
from tkinter import messagebox,filedialog
import os
from urllib.request import urlopen, HTTPError, URLError
import _thread     

fd='' 
filesize=''

def startdownloadcheck():
    if entry1.get()=='':
        messagebox.showerror("ERROR","INVALID URL")
    else:
        startdownload()    

def startdownload():
    global fd
    fd=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save Image File",filetypes=(("JPG Image","*.jpg"),("PNG Image","*.png"),("EXE File","*.exe"),("All Files","*.*")))  
    filename.set(os.path.basename(fd))
    _thread.start_new_thread(initDownload, ())    
def initDownload():
    global filesize
    fileurl=url.get()
    target=urlopen(fileurl)
    meta=target.info()
    filesize=float(meta['Content-Length'])
    filesizemb=round((filesize/1024/1024),2)
    downloaded=0
    chunks=1024*5 
    with open(fd,"wb") as f:
        while True:
            parts=target.read(chunks)
            if not parts:
                messagebox.showinfo("MESSAGE","DOWNLOAD COMPLETED SUCCESSFULLY")
                break
            downloaded+=chunks
            percentage=round(((downloaded/filesize)*100),2)
            if percentage>100:
                percentage=100
            downloadprogress.set(str(round((downloaded/1024/1024),2))+" MB / "+str(filesizemb)+" MB")
            downloadpercentage.set(str(percentage)+" %")
            f.write(parts)
    f.close() 
           
def close():
    if messagebox.askyesno("CONFIRMATION","ARE YOU SURE THAT YOU WANT TO QUIT ?")==FALSE:
        return FALSE
    root.destroy()

root=Tk() 

url=StringVar()
filename=StringVar()
downloadprogress=StringVar()
downloadpercentage=StringVar()

filename.set("N/A")
downloadprogress.set("N/A")
downloadpercentage.set("N/A")

root.title("DOWNLOAD MANAGER")
root.geometry("700x500")
root.configure(bg="thistle3")
icon=PhotoImage(file="dmimage.png")
root.iconphoto(False, icon)

frame1 = LabelFrame(root,highlightbackground="thistle4", highlightthickness=5,text="File URL",font=('fixedsys', 20,"bold"))
frame1.pack(fill="both",expand="yes",padx=20,pady=20)

frame2 = LabelFrame(root,highlightbackground="thistle4", highlightthickness=5,text="Download Information",font=('fixedsys', 20,"bold"))
frame2.pack(fill="both",expand="yes",padx=20,pady=20)

frame1.config(bg="thistle1")

frame2.config(bg="thistle1")

label1=Label(frame1,text="Download URL :",bg="thistle1",font=('fixedsys', 13))
label1.pack(side=tk.LEFT,padx=10,pady=10)

entry1=Entry(frame1,textvariable=url,font=('fixedsys', 13))
entry1.pack(side=tk.LEFT,padx=10,pady=10)

button1=Button(frame1,text="Download",command=startdownloadcheck,bg="thistle2",font=('fixedsys', 13))
button1.pack(side=tk.LEFT,padx=10,pady=10)

label2=Label(frame2,text="File :",bg="thistle1",font=('fixedsys', 13))
label2.grid(row=0,column=0,padx=10,pady=10)

label3=Label(frame2,text="Download Progress :",bg="thistle1",font=('fixedsys', 13))
label3.grid(row=1,column=0,padx=10,pady=10)

label4=Label(frame2,text="Download Percentage :",bg="thistle1",font=('fixedsys', 13))
label4.grid(row=2,column=0,padx=10,pady=10)

label4=Label(frame2,textvariable=filename,bg="thistle1",font=('fixedsys', 13))
label4.grid(row=0,column=1,padx=10,pady=10)

label4=Label(frame2,textvariable=downloadprogress,bg="thistle1",font=('fixedsys', 13))
label4.grid(row=1,column=1,padx=10,pady=10)

label4=Label(frame2,textvariable=downloadpercentage,bg="thistle1",font=('fixedsys', 13))
label4.grid(row=2,column=1,padx=10,pady=10)


button2=Button(root,text="Exit Download Manager",command=close,bg="thistle2",font=('fixedsys', 13))
button2.pack(padx=20,pady=20)

root.mainloop()
