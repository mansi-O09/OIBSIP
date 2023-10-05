from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0") 

        #===========background image===============================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sasha\OneDrive\Desktop\mini prjts\user-login\images\sss.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
 



#===========class call&obj===============================       
if __name__ == "__main__":
    root=Tk()
    app = Register(root)
    root.mainloop()


