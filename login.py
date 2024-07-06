from tkinter import*
import sqlite3

root = Tk()
root.geometry('400x500')
root.title("register")


Fullname=StringVar()
Email=StringVar()
var=IntVar()
c=StringVar()
var1=IntVar()


def database():
    name1=Fullname.get()
    email=Email.get()
    gender=var.get()
    country=c.get()
    prog=var1.get()
    conn=sqlite3.connect('br.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute('create table if not exists students (Fullname TEXT,Gender TEXT,country TEXT)')
        cursor.execute('INSERT INTO  students(Fullname,Gender,Country)VALUES(?,?,?)',(name1,gender,country))
        conn.commit()

        conn = sqlite3.connect('grocery_store.db')
        c = conn.cursor()

        # Create the table if it doesn't exist
        c.execute('''
                    CREATE TABLE IF NOT EXISTS grocery (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        phone TEXT,
                        category TEXT,
                        product TEXT,
                        price REAL,
                        quantity INTEGER,
                        extended_price REAL
                    )
                ''')

        # Insert the data into the table
        c.execute('''
                    INSERT INTO grocery (name, phone, category, product, price, quantity, extended_price)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (name, phone, category, product, price, quantity, extended_price))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()


label_0 = Label(root,text="register",width=20,font=("bold",20))
label_0.place(x=90,y=53)

label_1= Label(root,text="FullName",width=20,font=("bold",10))
label_1.place(x=80,y=130)
entry_1 =Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2= Label(root,text="password",width=20,font=("bold",10))
label_2.place(x=68,y=180)

entry_2=Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3=Label(root,text="Gender",width=20,font=("bold",10))
label_3.place(x=70,y=230)

Radiobutton(root,text="male",padx=5,variable=var,value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx=20,variable=var,value=2).place(x=290,y=230)

'''label_4=Label(root,text= "country",width=20,font=("bold",10))
label_4.place(x=70,y=280)

list1=['']

droplist=OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set('select your city')
droplist.place(x=240,y=280)
'''
Button(root,text='submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)
root.mainloop()