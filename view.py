#!/usr/bin/python
#-*- coding:UTF-8 -*-
import Tkinter,tkFileDialog,thread
from yumlist import Yumlist

def CreateWindow():
    global Window,Box
    Window=Tkinter.Tk()
    Window.geometry('800x600+250+100')
    Window['bg'] = '#CDC8B1'
    Window.title('源下载工具')
    Window.iconbitmap('icon.ico')
    CreateLabel('下载地址:', 60, 10, 10, 60, 20)
    CreateLabel('保存目录:', 60, 10, 35, 60, 20)
    CreateEntry(80, 10, 660, 20)
    CreateButton('查询', 750, 10, 30, 20,ChickButton_Search)
    CreateButton('打开', 750, 35, 30, 20,ChickButton_Open)
    CreateButton('下载', 750, 60, 30, 20,ChickButton_Load)
    CreateRadioButton()
    
    #Binding Scrollbar wtih Listbox.items
    Scrollbar=Tkinter.Scrollbar(Window)
    Scrollbar.place(x=780,y=90,width=20,height=500)
    Box=Tkinter.Listbox(Window,selectmode='multiple')
    Box.place(x=10,y=90,width=770,height=500)
    Box['yscrollcommand'] = Scrollbar.set
    Scrollbar['command'] = Box.yview
    Window.mainloop()
    

def CreateLabel(conents=None,wr=None,a=None,b=None,c=None,d=None):
    Label=Tkinter.Label(Window)
    Label['text'] = conents
    Label['wraplength'] = wr
    Label.place(x=a,y=b,width=c,height=d)
    
def CreateButton(conents=None,a=None,b=None,c=None,d=None,Chick=None):
    Button=Tkinter.Button(Window)
    Button['text'] = conents
    Button['activebackground'] = '#33FF33'
    Button['foreground'] = 'Red'
    Button['command'] = Chick
    Button.place(x=a,y=b,width=c,height=d)

def CreateEntry(a=None,b=None,c=None,d=None):
    global EnVar,Entry
    EnVar=Tkinter.StringVar()
    Entry=Tkinter.Entry(Window,textvariable= EnVar)
    EnVar.set('')
    Entry.place(x=a,y=b,width=c,height=d)

def CreateRadioButton():
    global RadioInVar
    RadioInVar=Tkinter.IntVar()
    RadioButton_ALL=Tkinter.Radiobutton(Window,variable = RadioInVar,text = '全选',value = 1,command=ChickRadio)
    RadioButton_ALL.place(x=10,y=70,width=70,height=20)
    RadioButton_None=Tkinter.Radiobutton(Window,variable = RadioInVar,text = '不选',value = 2,command=ChickRadio)
    RadioButton_None.place(x=80,y=70,width=70,height=20)
    
def ChickButton_Search():
    global yum,namelist
    Box.delete(0,'end')
    yum=Yumlist(EnVar.get())
    namelist=yum.getlist()
    for i in namelist:
        Box.insert('end',str(i))

def ChickButton_Load():
    downlist=Box.curselection()
    for i in downlist:
        yum.download(namelist[int(i)],save_path)

def ChickButton_Open():
    global save_path
    save_path=tkFileDialog.askdirectory()
    CreateLabel(str(save_path),660,80,35,660,20)

def ChickRadio():
    if RadioInVar.get() == 1:
        Box.selection_set(0,'end')
    elif RadioInVar.get() == 2:
        Box.select_clear(0, 'end')
        
if __name__ == '__main__':
    CreateWindow()