from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


root=Tk()
root.geometry("550x300")
root.title("Contact Details")


def insert():

    name=e_name.get()
    phno=e_phno.get()
    if(name=="" or phno==""):
        MessageBox.showinfo("Insert status","All fields are require")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="python-tkinter")
        cursor=con.cursor()
        cursor.execute("insert into  contactinfo values('"+name+"','"+phno+"')")
        cursor.execute("commit")

        e_name.delete(0,'end')
        e_phno.delete(0,'end')
        show()
        MessageBox.showinfo("Insert Status","inserted successfully")
        con.close()

def delete():
    if(e_name.get()==''):
        MessageBox.showinfo("Delete status","name is mandatory " )
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="python-tkinter")
        cursor=con.cursor()
        cursor.execute("delete from contactinfo where name='"+e_name.get()+"'")
        cursor.execute("commit")
        e_name.delete(0,'end')
        e_phno.delete(0,'end')
        show()
        MessageBox.showinfo("Delete Status","deleted  successfully")
        con.close()


def update():

    name=e_name.get()
    phno=e_phno.get()
    if( name=="" or phno==""):
        MessageBox.showinfo("update status","All fields are require")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="python-tkinter")
        cursor=con.cursor()
        cursor.execute("update contactinfo set phno='"+phno+"'where name='"+name+"' ")
        cursor.execute("commit")
        e_name.delete(0,'end')
        e_phno.delete(0,'end')
        show()
        MessageBox.showinfo("Update Status","updated successfully")
        con.close()


def view():
    if(e_name.get()==''):
        MessageBox.showinfo("View status","name is mandatory " )
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="python-tkinter")
        cursor=con.cursor()
        cursor.execute("select * from contactinfo where name='"+e_name.get()+"' ")
        rows=cursor.fetchall()
        for row in rows:
            e_phno.insert(0,row[1])

         #MessageBox.showinfo("View Status","viewed  successfully")
        con.close()
def show():
    con=mysql.connect(host="localhost",user="root",password="",database="python-tkinter")
    cursor=con.cursor()
    cursor.execute("select * from contactinfo ")
    rows=cursor.fetchall()
    list.delete(0,list.size())
    for row in rows:
        insertData=str(row[0])+'    '+row[1]
        list.insert(list.size()+1,insertData)
    con.close()

name=Label(root,text='Enter Name' ,font=("bold",10))
name.place(x=20,y=60)
e_name=Entry()
e_name.place(x=200,y=60)


phno=Label(root,text='Enter Phone No' ,font=("bold",10))
phno.place(x=20,y=90)
e_phno=Entry()
e_phno.place(x=200,y=90)

insrt=Button(root,text="INSERT",font=("bold",10),bg="white",command=insert)
insrt.place(x=100,y=140)

delete=Button(root,text="DELETE",font=("bold",10),bg="white",command=delete)
delete.place(x=180,y=140)

update=Button(root,text="UPDATE",font=("bold",10),bg="white",command=update)
update.place(x=260,y=140)

view=Button(root,text="VIEW",font=("bold",10),bg="white",command=view)
view.place(x=340,y=140)

list=Listbox(root)
list.place(x=400,y=30)
show()

root.mainloop()
