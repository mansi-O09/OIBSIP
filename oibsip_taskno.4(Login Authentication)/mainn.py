
import random
import time 
import datetime
from tkinter import messagebox
import mysql.connector

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



       
        imgl=Image.open(r"C:\Users\sasha\OneDrive\Desktop\projects\user-login\mmm.png")
        imgl=imgl.resize((100,100),Image.ANTIALIAS)
        self.photoimagel=ImageTk.PhotoImage(imgl)
        lblimgl=Label(image=self.photoimagel,bg="black",borderwidth=0)
        lblimgl.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        img2=Image.open(r"C:\Users\sasha\OneDrive\Desktop\projects\user-login\mmm.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimgl=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimgl.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\sasha\OneDrive\Desktop\projects\user-login\ppp.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimgl=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimgl.place(x=650,y=395,width=25,height=25)

        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="green")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=370,width=160)


    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)    



    def login(self):
        if self.txtuser.get()=="" or self.txtuser.get=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="mansi" and self.txtpass.get()=="momo":
            messagebox.showinfo("Success","WELCOME TO THE WORLD OF FOODIE CODER")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mns_@shr_",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                       self.txtuser.get(),
                                                                                       self.txtpass.get()
                                                                                     ))  
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and pasword")  
            else:
                open_main=messagebox.askyesno("Yes No","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Hospital(self.new_window)
                else:
                    if not open_main:
                       return    
            conn.commit()
            conn.close()

#==========================reset password============================

    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)    
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mns_@shr_",database="mydata")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row= my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)   
            else: 
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2) 
                self.root2.destroy()   




#===========================forget password window========================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showinfo("Error","Please enter the email address to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mns_@shr_",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s") 
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")  
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                 
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_securiy_Q=ttk.Combobox( self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_securiy_Q["values"]=("Select","Your Birth Place","Yur Bestie Name","Your Crush Name","Your Pet Name",)
                self.combo_securiy_Q.place(x=50,y=110,width=250)
                self.combo_securiy_Q.current(0)
                
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)




#===========main class===============================
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0") 



#==============variables================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        #===========background image===============================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sasha\OneDrive\Desktop\projects\user-login\qqq.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
 
        #===========left image===============================
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\sasha\OneDrive\Desktop\projects\user-login\mns.png")
        lbl_bg=Label(self.root,image=self.bg1)
        lbl_bg.place(x=50,y=100,width=470,height=550)


         #===========main frame===============================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        #===========top heading===============================
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)



         #===========row 1===============================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)



         #===========row 2===============================
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="E-mail",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)



         #===========row 3===============================
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

         #===========option dropdown menu===============================
        self.combo_securiy_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_securiy_Q["values"]=("Select","Your Birth Place","Yur Bestie Name","Your Crush Name","Your Pet Name",)
        self.combo_securiy_Q.place(x=50,y=270,width=250)
        self.combo_securiy_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)



        #===========row 4===============================
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


         #===========ter&con checkbox===============================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agreee The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)


         #===========register button===============================
        img=Image.open(r"C:\Users\sasha\OneDrive\Desktop\projects\user-login\rrr.png")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        bl=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        bl.place(x=10,y=420,width=200)



        #===========login button===============================
        img1=Image.open(r"C:\Users\sasha\OneDrive\Desktop\projects\user-login\lll.png")
        img1=img1.resize((200,55),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        bl=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        bl.place(x=330,y=420,width=200)



     #===============function declaration==================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms and Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mns_@shr_",database="mydata")
            my_cursor=conn.cursor()
            query=("Select * from  register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exists, Please enter another email")
            else:
                my_cursor.execute("insert into register value(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_pass.get()
                                                                                     ))    
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Sccessfully")



    def return_login(self):
        self.root.destroy()


    

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("Times New Roman",50,"bold")) 
        lbltitle.pack(side=TOP,fill=X)

        #============================ DATA FRAME ==============================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=480)

        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=("arial",12,"bold"),text="Patient Information")
        
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=("arial",12,"bold"),text="Prescription")
        
        DataframeRight.place(x=990,y=5,width=460,height=350)

        #============================ BUTTONDS FRAME =====================================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        #============================= DETAILS FRAME =====================================
        Detailframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailframe.place(x=0,y=600,width=1530,height=190)

        #============================== DATA FRAME LEFT =====================================
        lblNmaeTablet=Label(DataframeLeft,text="Name of the Tablet:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNmaeTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(DataframeLeft,state="readonly",font=("arial",12,"bold"),width=35)
        comNameTablet['values']=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amplodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1) 
          
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNOoftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablets:",padx=2,pady=6)
        lblNOoftablets.grid(row=3,column=0,sticky=W)
        txtNOoftablets=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNOoftablets.grid(row=3,column=1)
    
        lbllot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNOoftablets.grid(row=4,column=1)
        
        lblIssueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtlDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtlDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)
    
        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientID=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient ID:",padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientID.grid(row=4,column=3)

        lblNHSNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NHSN umber:",padx=2,pady=6)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        txtNHSNumber=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNHSNumber.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateofBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)

        #================================ DATA FRAME RIGHT ===================================
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

       
                                      
if __name__ == "__main__":
    main()
