from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
from datetime import datetime
# DATABASE
from db_maintenance import *

def writecsv(record_list):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(record_list)

GUI = Tk()
GUI.title('โปรแกรมซ่อมบำรุง by SKI')
GUI.geometry('500x500+50+50')
####FONT#####
FONT1 = ('Angsana New',20,'bold')
FONT2 = ('Angsana New',15)


#######TAB#######
Tab =ttk.Notebook(GUI)
T1 = Frame(Tab,)
T2 = Frame(Tab,)
T3 = Frame(Tab,)
Tab.add(T1,text='ใบแจ้งซ่อม')
Tab.add(T2,text='ดูใบแจ้งซ่อม')
Tab.add(T3,text='สรุป')
Tab.pack(fill=BOTH,expand=1)

#################
L = Label(T1,text='ใบแจ้งซ่อม',font=FONT1)
L.place(x=80,y=10)

#-------------
L = Label(T1,text='ชื่อผู้แจ้ง',font=FONT2)
L.place(x=30,y=50)
v_name = StringVar() #ตัวแปรพิเศษใช้กับ GUI
E1 = ttk.Entry(T1,textvariable=v_name, font=FONT2)
E1.place(x=150,y=50)

#-------------
L = Label(T1,text='แผนก',font=FONT2)
L.place(x=30,y=100)
v_department =StringVar()
E2 = ttk.Entry(T1,textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)
#-------------
L = Label(T1,text='อุปกรณ์/เครื่อง',font=FONT2)
L.place(x=30,y=150)
v_machine =StringVar()
E3 = ttk.Entry(T1,textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)
#-------------
L = Label(T1,text='อาการเสีย',font=FONT2)
L.place(x=30,y=200)
v_problem =StringVar()
E4 = ttk.Entry(T1,textvariable=v_problem ,font=FONT2)
E4.place(x=150,y=200)
#-------------
L = Label(T1,text='หมายเลข',font=FONT2)
L.place(x=30,y=250)
v_number =StringVar()
E5 = ttk.Entry(T1,textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)
#-------------
L = Label(T1,text='เบอร์โทร',font=FONT2)
L.place(x=30,y=300)
v_tel =StringVar()
E6 = ttk.Entry(T1,textvariable=v_tel,font=FONT2)
E6.place(x=150,y=300)

def save():
    name = v_name.get() # .get คือการดึงออกมาจาก StringVar
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()

    text = 'ชื่อผู้แจ้ง: ' + name + '\n' # \n คือขึ้นบรรทัดใหม่
    text = text + 'แผนก: ' + department + '\n'
    text = text + 'อุปกรณ์/เครื่อง: ' + machine + '\n'
    text = text + 'อาการเสีย: ' + problem + '\n'
    text = text + 'หมายเลข: ' + number + '\n'
    text = text + 'โทร: ' + tel + '\n'
    dt = datetime.now().strftime('%Y%m%d%H:%M:%S')
    #Generate Transaction
    tsid = str(int(datetime.now().strftime('%y%m%d%H%M%S')) + 114152147165)
    insert_mtworkorder(tsid,name,department,machine,problem,number,tel)
    v_name.set('')
    v_department.set('')
    v_machine.set('')
    v_problem.set('')
    v_number.set('')
    v_tel.set('')
  
    
    #datalist= [dt,name,department,machine,problem,number,tel]
    # writecsv(datalist)
    #.showinfo('กำลังบันทึกข้อมูล...',text)    



B = Button(T1, text='บันทึกใบแจ้งซ่อม',command=save)
B.place(x=200,y=350)



###############TAB2#####################
header = ['TSID','ชื่อ','แผนก','อุปกรณ์','อาการเสีย','หมายเลข','เบอร์โทรผู้แจ้ง']
headerw = [100,150,150,200,250,150,150]


mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=20)
mtworkorderlist.pack()

for h,w in zip(header,headerw):
    mtworkorderlist.heading(h,text=h)
    mtworkorderlist.column(h,width=w,anchor='center')
mtworkorderlist.column('TSID',anchor='e')

style = ttk.Style()
style.configure('Treeview.Heading',padding=(10,10),font=('Angsana New',20, 'bold'))
style.configure('Treeview',rowheight=25,font=('Angsana New',15))
#mtworkorderlist.insert('','end',values=['A','B','C','D','E','F','G',])

def updata_table():
    #clear ข้อมูลเก่า
    mtworkorderlist.delete(*mtworkorderlist.get_children())
    data = view_mtworkorder()
    for d in data:
        d = list(d)
        del d[0]
        mtworkorderlist.insert('','end',values=d)


####START UP####
    updata_table()
    



def EditPage_mtworkorder(event=None):
    select = mtworkorderlist.selection()
    output = mtworkorderlist.item(select)
    op (output['values'])

    tsid  = op[0]
    name = op[1]
    department = op[2]
    machine = op[3]
    problem = op[4]
    number = op[5]
    tel = op[6]


    GUI2 = Toplevel()
    GUI2.title('หน้าแก้ไขข้อมูลแจ้งซ่อม')
    GUI2.geometry('500x500')
    
    L = Label(GUI2,text='ใบแจ้งซ่อม',font=FONT1)
L.place(x=80,y=10)

#-------------
L = Label(GUI2,text='ชื่อผู้แจ้ง',font=FONT2)
L.place(x=30,y=50)
v_name2 = StringVar() #ตัวแปรพิเศษใช้กับ GUI
E1 = ttk.Entry(GUI2,textvariable=v_name2, font=FONT2)
E1.place(x=150,y=50)

#-------------
L = Label(GUI2,text='แผนก',font=FONT2)
L.place(x=30,y=100)
v_department2 =StringVar()
E2 = ttk.Entry(GUI2,textvariable=v_department2,font=FONT2)
E2.place(x=150,y=100)
#-------------
L = Label(GUI2,text='อุปกรณ์/เครื่อง',font=FONT2)
L.place(x=30,y=150)
v_machine2 =StringVar()
E3 = ttk.Entry(GUI2,textvariable=v_machine2,font=FONT2)
E3.place(x=150,y=150)
#-------------
L = Label(GUI2,text='อาการเสีย',font=FONT2)
L.place(x=30,y=200)
v_problem2 =StringVar()
E4 = ttk.Entry(GUI2,textvariable=v_problem2 ,font=FONT2)
E4.place(x=150,y=200)
#-------------
L = Label(GUI2,text='หมายเลข',font=FONT2)
L.place(x=30,y=250)
v_number2 =StringVar()
E5 = ttk.Entry(GUI2,textvariable=v_number2,font=FONT2)
E5.place(x=150,y=250)
#-------------
L = Label(GUI2,text='เบอร์โทร',font=FONT2)
L.place(x=30,y=300)
v_tel2 =StringVar()
E6 = ttk.Entry(GUI2,textvariable=v_tel2,font=FONT2)
E6.place(x=150,y=300)

def save():
    name = v_name2.get() # .get คือการดึงออกมาจาก StringVar
    department = v_department2.get()
    machine = v_machine2.get()
    problem = v_problem2.get()
    number = v_number2.get()
    tel = v_tel2.get()
    
    
    dt = datetime.now().strftime('%Y%m%d%H:%M:%S')
    update_mtworkorder(tsid,'name')
   
    
    updata_table()
    
    #datalist= [dt,name,department,machine,problem,number,tel]
    # writecsv(datalist)
    #.showinfo('กำลังบันทึกข้อมูล...',text)    


    B = Button(T1, text='บันทึกใบแจ้งซ่อม',command=save)
    B.place(x=200,y=350)

    GUI2.mainloop()

mtworkorderlist.bind('<Double-1>',EditPage_mtworkorder)

GUI.mainloop()