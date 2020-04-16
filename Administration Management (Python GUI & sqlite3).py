#Soham_Sahare

from tkinter import *
import sqlite3

root = Tk()
root.title("Admin")
root.configure(bg = "black")

#CREATE A DATABASE AND TABLE
'''
connect = sqlite3.connect('admin.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE admin (adminid INTEGER PRIMARY KEY AUTOINCREMENT,
                                            username TEXT NOT NULL,
                                            paaswo TEXT NOT NULL)""")

connect.commit()
connect.close()
'''
#DB LOGIN

def login():

    def log():

        connect = sqlite3.connect('admin.db')
        cursor = connect.cursor()

        v = (username.get()).lower()
        u = (paaswo.get()).lower()

        if (v == "" or u == ""):
            mylabel = Label(loginroot, text="Input values can't be NULL", font=50, padx=60, pady=20, fg="white",bg="black")
            mylabel.grid(row=6, columnspan=3)

        #RETRIVING DATA QUERY FROM TABLE

        cursor.execute("SELECT adminid FROM admin WHERE username = (:username) AND paaswo =(:paaswo)",
                       {
                           'username': (username.get()).lower(),
                           'paaswo': (paaswo.get()).lower()
                       })

        a = cursor.fetchall()

        if a == []:
            unsuccesslogin()
        else:
            successlogin(a)
            root.destroy()
            loginroot.destroy()

        connect.commit()
        connect.close()

    def successlogin(a):

        def oka():
            succlog.destroy()
            newwindow(a)

        succlog = Tk()
        succlog.title("Logged In")
        succlog.configure(bg="black")

        suclabel = Label(succlog, text="Logged in Successfully \n As " + username.get(), font=50, padx=10, pady=20,
                         fg="white", bg="black")
        suclabel.grid(row=1, column=1)

        okbtn = Button(succlog, text='OK', command=oka, padx=20, font=35, bg="green", fg="white")
        okbtn.grid(row=5, columnspan=3, padx=30)

        spacelabel = Label(succlog, text=" ", fg="white", padx=10, bg="black")
        spacelabel.grid(row=7, column=0)

    def unsuccesslogin():

        connect = sqlite3.connect('admin.db')
        cursor = connect.cursor()

        cursor.execute("SELECT adminid FROM admin WHERE username = (:username)",
                       {
                           'username': (username.get()).lower()
                       })

        a = cursor.fetchone()

        if a is None:
            trya = Tk()
            trya.title("OOPS...")
            errlabel = Label(trya, text="Username does not exist \n Please Signup ", font=50, padx=10, pady=20, fg="white", bg="black")
            errlabel.grid(row=1, column=1)
            loginroot.destroy()
            signup()
        else:

            oopslabel = Label(loginroot, text="Incorrect Password \n Please Try again", font=50, padx=10, pady=20, fg="white", bg="black")
            oopslabel.grid(row=3, column=1)

            paaswo.delete(0, END)

        connect.commit()
        connect.close()


    def newwindow(a):

        b = a[0]
        c = str(b[0])

        connect = sqlite3.connect('admin.db')
        cursor = connect.cursor()

        tableexistsquery = "SELECT COUNT(name) FROM sqlite_master WHERE type = 'table' AND name ="+"'admin"+c+"'"


        cursor.execute(tableexistsquery)

        if (cursor.fetchone()[0] != 1):

            connect = sqlite3.connect('admin.db')
            cursor = connect.cursor()

            createquery = "CREATE TABLE " + "admin" + c + " (studid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, rollnumber TEXT NOT NULL, at INTEGER NOT NULL, py INTEGER NOT NULL, cn INTEGER NOT NULL)"

            cursor.execute(createquery)

            connect.commit()
            connect.close()

        nw = Tk()
        nw.title("Welcome")
        nw.configure(bg = "black")

        def star():

            global name, rollnumber, m1, m2, m3

            name = Entry(nw, width=30, text="Username")
            rollnumber = Entry(nw, width=30, text="Roll Number")
            m1 = Entry(nw, width=30, text="Automata Theory")
            m2 = Entry(nw, width=30, text="Python")
            m3 = Entry(nw, width=30, text="Computer Networks")

            nameLabel = Label(nw, text="Name : ", fg="white", bg="black", font=35)
            nameLabel.grid(row=1, column=59)
            name.grid(row=1, column=60, padx=20, pady=20)

            rollnumberLabel = Label(nw, text="Roll Number : ", fg="white", bg="black", font=35)
            rollnumberLabel.grid(row=2, column=59)
            rollnumber.grid(row=2, column=60, padx=20, pady=20)

            m1Label = Label(nw, text="Marks in Automata Theory :", fg="White", bg="black", font=35)
            m1Label.grid(row=3, column=59)
            m1.grid(row=3, column=60, padx=20, pady=20)

            m2Label = Label(nw, text="Marks in Python :", fg="White", bg="black", font=35)
            m2Label.grid(row=4, column=59)
            m2.grid(row=4, column=60, padx=20, pady=20)

            m3Label = Label(nw, text="Marks in Computer Networks:", fg="White", bg="black", font=35)
            m3Label.grid(row=5, column=59)
            m3.grid(row=5, column=60, padx=20, pady=20)

        def clear():
            name.delete(0, END)
            rollnumber.delete(0, END)
            m1.delete(0, END)
            m2.delete(0, END)
            m3.delete(0, END)

        def added():

            def oka():
                succwin.destroy()

            succwin = Tk()
            succwin.title("ADDED")
            succwin.configure(bg="black")

            if operation == 'add':
                suclabel = Label(succwin, text="ADDED Successfully ", font=50, padx=10, pady=20,fg="white", bg="black")
                suclabel.grid(row=1, column=1)
            else:
                suclabel = Label(succwin, text="DELETED Successfully ", font=50, padx=10, pady=20,fg="white", bg="black")
                suclabel.grid(row=1, column=1)

            okbtn = Button(succwin, text='OK', command=oka, padx=20, font=35, bg="green", fg="white")
            okbtn.grid(row=5, columnspan=3, padx=30)

            spacelabel = Label(succwin, text=" ", fg="white", padx=10, bg="black")
            spacelabel.grid(row=7, column=0)

        def submit():

            if operation == 'add':

                n = name.get()
                r = rollnumber.get()
                ma1 = float(m1.get())
                ma2 = float(m2.get())
                ma3 = float(m3.get())

                if (n =="" or r =="" or ma1 =="" or ma2 =="" or ma3 ==""):

                    lLabel = Label(nw, text="Input Values Can't be null", fg="White", bg="black", font=35)
                    lLabel.grid(row=10, column=60)
                else:

                    connect = sqlite3.connect('admin.db')
                    cursor = connect.cursor()

                    insertquery = "INSERT INTO " + "admin" + c + "(name, rollnumber, at, py, cn) VALUES (:name, :rollnumber, :at, :py, :cn)"

                    cursor.execute(insertquery,{
                        'name': name.get(),
                        'rollnumber': rollnumber.get(),
                        'at': m1.get(),
                        'py': m2.get(),
                        'cn': m3.get()
                     })

                    connect.commit()
                    connect.close()
                    clear()
                    added()

            elif operation == 'delete':

                n = nameup.get()
                r = rollnumberup.get()

                if (n =="" or r ==""):

                    lLabel = Label(nw, text="Input Values Can't be null", fg="White", bg="black", font=35)
                    lLabel.grid(row=10, column=60)
                else:

                    connect = sqlite3.connect('admin.db')
                    cursor = connect.cursor()

                    deletequery = "DELETE FROM " + "admin" + c + " WHERE name = (:name) AND rollnumber = (:rollnumber)"

                    cursor.execute(deletequery,{
                        'name': nameup.get(),
                        'rollnumber': rollnumberup.get()
                     })

                    connect.commit()
                    connect.close()
                    nameup.delete(0, END)
                    rollnumberup.delete(0, END)
                    added()

        def add():
            star()
            clear()

            global operation

            nameLabel = Label(nw, text="Enter the Values to add", fg="white", bg="black", font=35, padx = 25)
            nameLabel.grid(row=0, column=60)

            addbtn = Button(nw, text='ADD', command=submit, padx=38, font=35, bg="green", fg="white")
            addbtn.grid(row=6, columnspan=3, padx=100, column=60, pady=7)
            operation = 'add'

        def delete():
            star()
            clear()
            nw.destroy()
            global root1, rollnumberup, nameup

            root1 = Tk()
            root1.title("DELETE data")
            root1.configure(bg = "black")

            nameup = Entry(root1, width=30, text="Username")
            rollnumberup = Entry(root1, width=30, text="Roll Number")

            nameLabel = Label(root1, text="Name : ", fg="white", bg="black", font=35)
            nameLabel.grid(row=1, column=59)
            nameup.grid(row=1, column=60, padx=20, pady=20)

            rollnumberLabel = Label(root1, text="Roll Number : ", fg="white", bg="black", font=35)
            rollnumberLabel.grid(row=2, column=59)
            rollnumberup.grid(row=2, column=60, padx=20, pady=20)

            global operation, op

            operation = 'delete'

            delbtn = Button(root1, text='DELETE', command=submit, padx=23, font=35, bg="green", fg="white")
            delbtn.grid(row=6, columnspan=3, padx=30, column=60, pady=7)

            root1.mainloop()

        def show():

            root1 = Tk()
            root1.title("DELETE data")
            root1.configure(bg="black")

            connect = sqlite3.connect('admin.db')
            cursor = connect.cursor()

            showquery = "SELECT * FROM admin"+c

            cursor.execute(showquery)

            i = 0
            for row in cursor:

                querylabel = Label(root1, text=row, padx=20, bg="Black", fg="white", font = 60)
                querylabel.grid(row=i, column=0, padx=20, pady=20)

                i += 1

            connect.commit()
            connect.close()

            root1.mainloop()

        def logout():
            nw.destroy()

        spacelabel = Label(nw, text="Welcome", fg="white", padx=10, pady=10, font=900, bg="black")
        spacelabel.grid(row=0, column=0, columnspan = 10)

        spacelabel = Label(nw, text="Choose your option ", fg="white", padx=10, pady=10, font=900, bg="black")
        spacelabel.grid(row=1, column=0, columnspan = 10)

        addbtn = Button(nw, text='ADD', command=add, padx=20, font=35, bg="green", fg="white")
        addbtn.grid(row=2, columnspan=10, padx=30, pady=7)

        deletebtn = Button(nw, text='DELETE', command=delete, padx=20, font=35, bg="green", fg="white")
        deletebtn.grid(row=3, columnspan=10, padx=30, pady=7)

        showbtn = Button(nw, text='SHOW', command=show, padx=20, font=35, bg="green", fg="white")
        showbtn.grid(row=4, columnspan=10, padx=30, pady=7)

        logoutbtn = Button(nw, text='Logout', command=logout, padx=20, font=35, bg="green", fg="white")
        logoutbtn.grid(row=0, columnspan=10,column = 100, padx=10, pady=7)

        nw.mainloop()

    loginroot = Tk()
    loginroot.title("LogIn")
    loginroot.configure(bg = "black")

    username = Entry(loginroot, width = 30, text="Username")
    paaswo = Entry(loginroot, width = 30)

    paaswo.config(show="*")

    UsernameLabel = Label(loginroot, text="Username : ", fg="white", bg = "black", font = 35)
    UsernameLabel.grid(row=0, column=0)
    username.grid(row=0, column=1, padx=20, pady=20)

    paaswoLabel = Label(loginroot, text="Password : ", fg="white", bg = "black", font = 35)
    paaswoLabel.grid(row=1, column=0)
    paaswo.grid(row=1, column=1, padx=20, pady=20)

    loginbtn = Button(loginroot, text='Login', command=log, padx=20, font=35, bg="green", fg="white")
    loginbtn.grid(row=2, columnspan=3, padx=30)

    spacelabel = Label(loginroot, text=" ", fg="white", padx=10, bg="black")
    spacelabel.grid(row=7, column=0)

    loginroot.mainloop()

#DB SIGNUP

def signup():

    def sign():

        connect = sqlite3.connect('admin.db')
        cursor = connect.cursor()

        cursor.execute("SELECT username FROM admin")
        ans = cursor.fetchall()

        v = (username.get()).lower()
        u = (paaswo.get()).lower()

        for i in ans:
            str = ''.join(i)
            if(v == "" or u ==""):
                mylabel = Label(signuproot, text="Input values can't be NULL", font=50, padx=60, pady=20,fg="white", bg="black")
                mylabel.grid(row=6, columnspan=3)
            else:
                if (str == v):
                    unsuccesssignup()
                    break
                else:
                    connect = sqlite3.connect('admin.db')
                    cursor = connect.cursor()

                    #INSERT QUERY

                    cursor.execute("INSERT INTO admin (username, paaswo) VALUES (:username, :paaswo)",
                                   {
                                       'username': (username.get()).lower(),
                                       'paaswo': (paaswo.get()).lower()
                                   })
                    connect.commit()
                    connect.close()

                    successsignup()
                    signuproot.destroy()

                    break

        username.delete(0, END)
        paaswo.delete(0, END)

    def successsignup():

        succ = Tk()
        succ.title("All good...")
        errlabel = Label(succ, text="SIGNUP SUCCESSFULL", font=50, padx=60, pady=20, fg="white", bg="black")
        errlabel.grid(row=1, column=1)
    
    def unsuccesssignup():

        exist = Tk()
        exist.title("OOPS...")
        errlabel = Label(exist, text="Username already exist \n Try another username \n Or Please Login", font=50, padx=10, pady=20,
                         fg="white", bg="black")
        errlabel.grid(row=1, column=1)

    signuproot = Tk()
    signuproot.title("SignUp")
    signuproot.configure(bg = "black")

    username = Entry(signuproot, width=30, text="Username")
    paaswo = Entry(signuproot, width=30)

    paaswo.config(show="*")

    UsernameLabel = Label(signuproot, text="Username : ", fg="white", bg="black", font = 35)
    UsernameLabel.grid(row=0, column=0)
    username.grid(row=0, column=1, padx=20, pady=20)

    paaswoLabel = Label(signuproot, text="Password : ", fg="white", bg="black", font = 35)
    paaswoLabel.grid(row=1, column=0)
    paaswo.grid(row=1, column=1, padx=20, pady=20)


    signupbtn = Button(signuproot, text='SignUp', command=sign, padx=20, font=35, bg="green", fg="white")
    signupbtn.grid(row=2, columnspan=3, padx=30)

    spacelabel = Label(signuproot, text=" ", fg="white", padx=10, bg="black")
    spacelabel.grid(row=7, column=0)

    signuproot.mainloop()

#DB DELETE

def delete():

    def dele():

        paaswoconf = Entry(delroot, width=30)
        paaswoconf.config(show = "*")
        paaswoconfLabel = Label(delroot, text="Confirm Password : ", fg="white", bg="black", font=35)
        paaswoconfLabel.grid(row=4, column=0)
        paaswoconf.grid(row=4, column=1, padx=20, pady=20)

        delbtn.destroy()

        dellabel = Label(delroot, text="Are you sure you want to delete? \n You won't be able to recover it\n "
                                       "If YES then confirm password and press OK \n "
                                       "Or else Press X on right top", font=50, padx=60, pady=20,
                                        fg="white", bg="black")
        dellabel.grid(row = 3, columnspan = 3)

        def unsuccessdelusername():

            deletesu = Tk()
            deletesu.title("Logged In")
            label = Label(deletesu, text="Entered Username does not exist\n Please try again", font=50, padx=10, pady=20, fg="white", bg="black")
            label.grid(row=1, column=1)

        def ok():

            v = (username.get()).lower()
            u = (paaswo.get()).lower()

            if (v == "" or u == ""):
                mylabel = Label(delroot, text="Input values can't be NULL", font=50, padx=60, pady=20, fg="white",
                                bg="black")
                mylabel.grid(row=6, columnspan=3)
            else:
                paas1 = paaswo.get()
                paas2 = paaswoconf.get()

                connect = sqlite3.connect('admin.db')
                cursor = connect.cursor()

                cursor.execute("SELECT adminid FROM admin WHERE username = (:username)",
                               {
                                   'username': (username.get()).lower()
                               })

                a = cursor.fetchone()

                if a is None:
                    unsuccessdelusername()
                    username.delete(0, END)
                    paaswo.delete(0, END)
                    paaswoconf.delete(0, END)
                else:
                    if (paas1 == paas2):
                        connect = sqlite3.connect('admin.db')
                        cursor = connect.cursor()

                        # DELETE QUERY

                        cursor.execute("DELETE FROM admin WHERE username = (:username) AND paaswo = (:paaswo)",
                                       {
                                           'username': (username.get()).lower(),
                                           'paaswo': paaswo.get()
                                       })

                        connect.commit()
                        connect.close()
                        delroot.destroy()

                        successdel()
                        delroot.destroy()

                    else:
                        unsuccessdel()
                        paaswo.delete(0, END)
                        paaswoconf.delete(0, END)


        okbtn = Button(delroot, text='OK', command=ok, padx=20, font=35, bg="green", fg="white")
        okbtn.grid(row=5, columnspan=3, padx=30)

    def successdel():

        deletesu = Tk()
        deletesu.title("Logged In")
        label = Label(deletesu, text="DELETED SUCCESSFULLY", font=50, padx=10, pady=20, fg="white", bg="black")
        label.grid(row=1, column=1)

    def unsuccessdel():

        deleteunsu = Tk()
        deleteunsu.title("Logged In")
        label = Label(deleteunsu, text="Password Does not match \n Please try again", font=50, padx=10, pady=20, fg="white", bg="black")
        label.grid(row=1, column=1)

    delroot = Tk()
    delroot.title("Delete")
    delroot.configure(bg = "black")

    username = Entry(delroot, width=30, text="Username")
    paaswo = Entry(delroot, width=30)

    paaswo.config(show="*")

    UsernameLabel = Label(delroot, text="Username : ", fg="white", bg="black", font=35)
    UsernameLabel.grid(row=0, column=0)
    username.grid(row=0, column=1, padx=20, pady=20)

    paaswoLabel = Label(delroot, text="Password : ", fg="white", bg="black", font=35)
    paaswoLabel.grid(row=1, column=0)
    paaswo.grid(row=1, column=1, padx=20, pady=20)

    delbtn = Button(delroot, text='Delete', command=dele, padx=20, font=35, bg="green", fg="white")
    delbtn.grid(row=2, columnspan=3, padx=30)

    spacelabel = Label(delroot, text=" ", fg="white", padx=10, bg="black")
    spacelabel.grid(row=7, column=0)

    delroot.mainloop()

#ROOT WIDGETS

spacelabel = Label(root, text = "If already registered then, ", fg = "white", padx = 50, pady = 10, font = 35, bg = "black" )
spacelabel.grid(row = 0, column = 0)

loginbtn = Button(root, text = 'Login', command = login, padx = 20, font = 35, bg = "green", fg = "white")
loginbtn.grid(row = 1, columnspan = 3, padx = 30)

spacelabel = Label(root, text = "if not, ", fg = "white", padx = 10, pady = 10, font = 35, bg = "black")
spacelabel.grid(row = 2, column = 0)

signupbtn = Button(root, text = 'Signup', command =signup, padx = 20, font = 35, bg = "green", fg = "white")
signupbtn.grid(row = 3, columnspan = 10, padx = 30)

spacelabel = Label(root, text = "or you want to delete user", fg = "white", padx = 10, pady = 10, font = 35, bg = "black")
spacelabel.grid(row = 5, column = 0)

delbtn = Button(root, text = 'Delete', command =delete, padx = 20, font = 35, bg = "green", fg = "white")
delbtn.grid(row = 6, columnspan = 10, padx = 30, pady = 7)




root.mainloop()