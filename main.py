from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

root=Tk()
root.state("zoomed")
root.configure(bg="MediumOrchid1")

wel_admin_lbl = Label(root, text="Student Database Management", font=("Georgia", 50, "bold", "underline"),bg="sky blue", borderwidth=15, relief="sunken", fg="red4")
wel_admin_lbl.pack()

login_img=Image.open("images/login.png").resize((90,30))
login_imgtk=ImageTk.PhotoImage(login_img)

reset_img=Image.open("images/reset.png").resize((90,30))
reset_imgtk=ImageTk.PhotoImage(reset_img)

logout_img=Image.open("images/logout.png").resize((90,30))
logout_imgtk=ImageTk.PhotoImage(logout_img)

back_img=Image.open("images/back.png").resize((80,30))
back_imgtk=ImageTk.PhotoImage(back_img)

def login_frame():

    frm=Frame(root,bg="OliveDrab1",relief="ridge",borderwidth=20,highlightbackground="brown",highlightthickness=5)
    frm.place(relx=.27,rely=.22,width=600,height=450)

    def reset(event):
        Username_entry.delete(0,"end")
        Password_entry.delete(0,"end")
        Username_entry.focus()

    def admin_login_frame(event):
        user=Username_entry.get()
        pas=Password_entry.get()
        if(len(user)==0 and len(pas)==0):
            messagebox.showwarning("Login Unsuccessful", "Fields can't be Empty")

        elif(user=='admin' and pas=='admin'):
            m=messagebox.showinfo("Login","Login Successful")
            if(m=="ok"):
                frm.destroy()
                admin_frame()
        else:
            messagebox.showerror("Invalid","Username or Password is wrong")

    Username_lbl=Label(frm,text="Username:",font=("Verdana",17,"bold"),bg="OliveDrab1")
    Username_lbl.place(relx=.07,rely=.15)
    Username_entry=Entry(frm,font=("Verdana",15,"bold"),bd=5)
    Username_entry.place(relx=.35,rely=.15)

    Password_lbl=Label(frm,text="Password:",font=("Verdana",17,"bold"),bg="OliveDrab1")
    Password_lbl.place(relx=.07,rely=.32)
    Password_entry=Entry(frm,font=("Verdana",15,"bold"),bd=5,show="\u25CF")
    Password_entry.place(relx=.35,rely=.32)

    login_btn=Label(frm,image=login_imgtk,bg="OliveDrab1")
    login_btn.place(relx=.38,rely=.55)
    login_btn.bind("<Button>",admin_login_frame)

    reset_btn=Label(frm,image=reset_imgtk,bg="OliveDrab1")
    reset_btn.place(relx=.6,rely=.55)
    reset_btn.bind("<Button>",reset)
def admin_frame():
    frm = Frame(root,relief="ridge",borderwidth=20, bg="gold")
    frm.place(relx=.23, rely=.20, width=700, height=500)

    #student_db_lbl = Label(frm, text="Admin Control Panel", font=("Georgia", 20, "bold", "underline"),bg="MediumOrchid1",borderwidth=15,relief="sunken")
    #student_db_lbl.pack()

    welcome_admin=Label(frm,text="Welcome,Admin",font=("Georgia",17,"bold"),bg="gold").pack(anchor="w")


    def logout(event):
        m=messagebox.showinfo("Logout","Logout Successful")
        if(m=="ok"):
            frm.destroy()
            login_frame()

    def show_std_db():
        frm.destroy()
        show_std_db_frame()


    logout_btn=Label(frm,image=logout_imgtk,bg="gold")
    logout_btn.pack(anchor="e")
    logout_btn.bind("<Button>",logout)

    Add_student_btn=Button(frm,text="Add/Remove Students",font=("Comic Sans","15","bold"),bd=8,bg="plum1",fg="firebrick",width=22).place(relx=.29,rely=.15)
    show_db_btn=Button(frm,text="Show Database",font=("Comic Sans","15","bold"),bd=8,bg="plum1",fg="firebrick",width=22,command=show_std_db).place(relx=.29,rely=.35)
    Fee_Update_btn=Button(frm, text="Fee Update", font=("Comic Sans", "15", "bold"), bd=8, bg="plum1", fg="firebrick",width=22).place(relx=.29, rely=.55)
    Add_Course_btn=Button(frm, text="Add Course", font=("Comic Sans", "15", "bold"), bd=8, bg="plum1", fg="firebrick",width=22).place(relx=.29, rely=.75)


def show_std_db_frame():
    frm = Frame(root, relief="ridge", borderwidth=20, bg="DarkGoldenrod1")
    frm.place(relx=.07, rely=.13, width=1200, height=600)

    def back_button(event):
        frm.destroy()
        admin_frame()

    back_btn=Label(frm,image=back_imgtk,bg="DarkGoldenrod1")
    back_btn.pack(anchor="w")
    back_btn.bind("<Button>",back_button)

login_frame()
root.mainloop()