from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)
    check.set(0)


def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpasswordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Mismatched')
    elif  check.get()==0:
        messagebox.showerror('Error','Please accept Terms and Conditions')    
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='mns_@shr_')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue,Please try agian') 
            return
        
        try:
            query='create database userlogin'   
            mycursor.execute(query)
            query='use userlogin'
            mycursor.execute(query) 
            query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(20),password varchar(10))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userlogin')    
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error','Username already exits')
        else:
            query='insert into data(email,username,password)values(%s,%s,%s)'    
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration Successful')
            clear()
            signup_window.destroy()
            import signin

        


        
    

                

        
    
        


def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.title('Signup page')
signup_window.resizable(False,False)

background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text="CREATE AN ACCOUNT",font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)


usernameLabel=Label(frame,text='username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=30,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmpasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termsandcondition=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',10,'bold'),
                              bg='white',fg='firebrick1',activebackground='white',activeforeground='firebrick1'
                              ,cursor='hand2',variable=check)
termsandcondition.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',
                    activeforeground='white',activebackground='firebrick1',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text='Dont have an account?',font=('Open Sans',9,'bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',
                   activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=170,y=404)










signup_window.mainloop()