import tkinter as tk
#import mysql.connector
from tkinter import *
from tkinter import ttk
#import requests
LARGEFONT =("Verdana", 35)



#db = mysql.connector.connect(host ="localhost",user = 'root',password = 'root',db ="school")
#cursor = db.cursor()
#if(cursor!=None):
   # print("success")

 
def submitact():
    obj=dashBoard(root,"User1")
    ''' 
    user = Username.get()
    passw = password.get()
  
    print("The name entered by you is {user} {passw}")
  
    logintodb(user, passw)

    '''
def exitact():
    root.destroy()

    
class dashBoard:
    def __init__(self,root,usr):
        self.root=root
        #db.commit()
        self.usr=usr
        self.root.title("LIQR SHOP MANAGEMENT")
        self.root.geometry("1350x700+0+0")

        
        M_F= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_F.place(x=20,y=100,width=1300,height=580)

        
        M_FB1= Frame(self.root,bd=0,relief=RIDGE,bg="#f3fbfe")
        M_FB1.place(x=120,y=120,width=1100,height=180)
        
        M_title=Label(M_FB1,text=" Welcome  "+usr+" !",font=("times new roman",12,"bold"),bg="#f3fbfe",fg='red')
        M_title.grid(row=0,column=18,padx=30,pady=80)

        M_Date=Label(M_FB1,text="                                                    Last login Sep 6th 2021!          ",font=("times new roman",12,"bold"),bg="#f3fbfe",fg='red')
        M_Date.grid(row=0,column=26,padx=38,pady=80)
 
        M_logout=Label(M_FB1,text="                                                        LOG OUT                         ",font=("times new roman",12,"bold"),bg="#f3fbfe",fg='red')
        M_logout.grid(row=0,column=36,padx=38,pady=80)     

        '''


        M_title=Label(D_F,text="SEARCH BY DEPARTMENTS",font=("times new roman",10,"bold"),bg="crimson",fg='white')
        M_title.grid(row=0,columnspan=2,pady=20)
        '''

        '''
        lbl_roll=Label(M_F,text="STUDENT:",font=("times new roman",15,"bold"),bg="crimson",fg='white')
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        ''' 
        '''
        combo_srch=ttk.Combobox(M_F,font=("times new roman",10,"bold"),state='readonly')
        combo_srch['values']=("DIPLOMA","UG","PG","PH.D","OTHERS")
        combo_srch.grid(row=1,column=1,padx=20,pady=10)
        '''
        M_FB= Frame(self.root,bd=0,relief=RIDGE,bg="#f3fbfe")
        M_FB.place(x=400,y=400,width=600,height=180)
        
        SrchBtn=Button(M_FB,text="MANAGE",command=self.userManagment,width=20,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=25,padx=40,pady=40)

             
        SrchEBtn=Button(M_FB,text="SELL",command=self.fetch_Edata,width=20,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=30,padx=60,pady=40)

       
        


    def userManagment(self):
        self.root=root
        #db.commit()
        #self.usr=usr
        self.root.title("LIQR SHOP MANAGEMENT")
        self.root.geometry("1350x700+0+0")
    
        M_F= Frame(self.root,bd=4,relief=RIDGE,bg="#f3fbfe")
        M_F.place(x=20,y=100,width=350,height=580)

        D_F= Frame(self.root,bd=4,relief=RIDGE,bg="#f3fbfe")
        D_F.place(x=300,y=100,width=1030,height=580)

        
        M_title=Label(M_F,text="Welcome  "+self.usr+" !",font=("times new roman",12,"bold"),bg="crimson",fg='white')
        M_title.grid(row=0,columnspan=2,pady=20)

        '''


        M_title=Label(D_F,text="SEARCH BY DEPARTMENTS",font=("times new roman",10,"bold"),bg="crimson",fg='white')
        M_title.grid(row=0,columnspan=2,pady=20)
        '''

        '''
        lbl_roll=Label(M_F,text="STUDENT:",font=("times new roman",15,"bold"),bg="crimson",fg='white')
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        ''' 
        '''
        combo_srch=ttk.Combobox(M_F,font=("times new roman",10,"bold"),state='readonly')
        combo_srch['values']=("DIPLOMA","UG","PG","PH.D","OTHERS")
        combo_srch.grid(row=1,column=1,padx=20,pady=10)
        '''
        
        SrchBtn=Button(M_F,text="DASHBOARD",command=self.fetch_Dashboard,width=30,bg="#2f8fdd",fg="white").grid(row=3,column=0,padx=20,pady=20)

        SrchEBtn=Button(M_F,text="CUSTOMER MANAGEMENT",command=self.custMgmtdata,width=30,bg="#2f8fdd",fg="white").grid(row=5,column=0,padx=20,pady=20)     

        SrchEBtn=Button(M_F,text="INVENTORY MANAGEMENT",command=self.inventMgmtdata,width=30,bg="#2f8fdd",fg="white").grid(row=7,column=0,padx=20,pady=20)

       
        SrchSBtn=Button(M_F,text="RANK MANAGEMENT",command=self.rankMgmtdata,width=30,bg="#2f8fdd",fg="white").grid(row=9,column=0,padx=20,pady=20)

       
        Log_Btn=Button(M_F,text="QUOTA MANAGEMENT",command=self.quotMgmtdata,width=30,bg="#2f8fdd",fg="white").grid(row=11,column=0,padx=20,pady=20)

        SrchEBtn=Button(M_F,text="USER MANAGEMENT",command=self.userMgmtdata,width=30,bg="#2f8fdd",fg="white").grid(row=13,column=0,padx=20,pady=20)

        #Log_Btn=Button(M_F,text="LOG OUT",command=lambda: self.logout("Logout"),width=30,bg="#2f8fdd",fg="white").grid(row=9,column=0,padx=20,pady=20)

    def userMgmtdata(self):
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="USER MANAGEMENT",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=1,column=15,padx= 25,pady=25)

        M_FB= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_FB.place(x=400,y=200,width=800,height=180)
        
        SrchBtn=Button(M_FB,text="ADD",command=self.adduser,width=30,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=25,padx=40,pady=40)

             
        SrchEBtn=Button(M_FB,text="AUDIT LOG",command=self.fetch_Edata,width=30,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=45,padx=60,pady=40)

        M_FB1= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_FB1.place(x=400,y=500,width=800,height=180)

        lst = [("User Name","Password","Name","Email","Address"),("user1","*******","Raj","raj092021@gmail.com","New Delhi")]
        coln=len(lst[0])
        #print(len(lst))

        for x in range(len(lst)):
            for y in range(coln):
                self.Table_Row=Entry(M_FB1,width=15,fg='#2f8fdd',font=('Arial',10,'bold'))
                self.Table_Row.grid(row=x,column=y)
                self.Table_Row.insert(END,lst[x][y])

        Act_title=Label(M_FB1,text="Action",font=('Arial',10,'bold'),fg='#2f8fdd').grid(row=0,column=10,padx= 20,pady=20)
        updateBtn=Button(M_FB1,text="UPDATE",command=self.updateUser,width=8,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=10,padx=15,pady=15)
        deleteBtn=Button(M_FB1,text="DELETE",command=self.userManagment,width=8,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=12,padx=20,pady=20)
        
        #Tbl_Frame=Frame(D_F,bd=2,relief=RIDGE,bg="#2f8fdd",fg="white")
        #Tbl_Frame.place(x=5,y=160,width=760,height=500)
        #treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        #t = Table(root)

      
        
        '''
        treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(Tbl_Frame,orient ="vertical",command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3","4","5")
          
        # Defining heading
        treev['show'] = 'headings'
          
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 100, anchor ='c')
        treev.column("2", width = 150, anchor ='c')
        treev.column("3", width = 300, anchor ='c')
        treev.column("4", width = 80, anchor ='c')
        treev.column("5", width = 100, anchor ='c')
          
        # Assigning the heading names to the 
        # respective columns
        treev.heading("1", text ="ID")
        treev.heading("2", text ="NAME")
        treev.heading("3", text ="RANK")
        treev.heading("4", text ="ACTION")
        #treev.heading("5", text ="EPARTMENT")
        
        
  
# Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        #cursor.execute("select * from t_courses")
        
        #result= cursor.fetchall()
        #print(len(result))
        result=("123","abc","rank1")
        
        for x in result:
            treev.insert("", 'end', text ="",values =(x[0], x[1], x[2]))
            
        #treev.tag_configure('odd', foreground="white",background='black')
        #treev.tag_configure('even', foreground="black",background='white')
        '''
    '''
    def logout(self,text):
        print(text)

        #3opennewWindow(self)
        root.destroy()
        import login
        #root.destroy()
    '''
        
    def updateUser(self):
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="EDIT USER",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
          
        #cursor.execute("select * from register where username=%s")
        
        e1_Lbl=Label(D_F,text="User Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e1_Lbl.grid(row=2,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=2, column=4,padx= 15, pady= 15)
        e1.insert(1, "user123")
 
        e2_Lbl=Label(D_F,text="Password:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e2_Lbl.grid(row=4,column=3)

        
        e2 = Entry(D_F, width=40,borderwidth=5)
        e2.grid(row=4, column=4,padx= 10, pady= 10)
        e2.insert(0, "123123")
 
        e3_Lbl=Label(D_F,text="First Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e3_Lbl.grid(row=6,column=3)


        e3 = Entry(D_F, width=40,borderwidth=5)
        e3.grid(row=6, column=4,padx= 10, pady= 10)
        e3.insert(0, "ABC")

        e4_Lbl=Label(D_F,text="Last Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e4_Lbl.grid(row=8,column=3)


        e4 = Entry(D_F, width=40,borderwidth=5)
        e4.grid(row=8, column=4,padx= 10, pady= 10)
        e4.insert(0, "XYZ")

        e5_Lbl=Label(D_F,text="Email:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e5_Lbl.grid(row=10,column=3)

        e6 = Entry(D_F, width=40,borderwidth=5)
        e6.grid(row=10, column=4,padx= 10, pady= 10)
        e6.insert(0, "")

        e5_Lbl=Label(D_F,text="Address:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e5_Lbl.grid(row=12,column=3)

        e6 = Entry(D_F, width=40,borderwidth=5)
        e6.grid(row=12, column=4,padx= 10, pady= 10)
        e6.insert(0, "NEW DELHI")

        
       
        submitBtn=Button(D_F,text="SUBMIT", command=self.submit_AddCstData,width=30,bg="#2f8fdd",fg='white').grid(row=14,column=4,padx=20,pady=20)
        

    def adduser(self):
        
        
        #print("Student details")
        #usr=fetch_Studentdata(r)
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="ADD USER",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
          
        #cursor.execute("select * from register where username=%s")
        
        e1_Lbl=Label(D_F,text="User Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e1_Lbl.grid(row=2,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=2, column=4,padx= 15, pady= 15)
        e1.insert(1, "")
 
        e2_Lbl=Label(D_F,text="Password:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e2_Lbl.grid(row=4,column=3)

        
        e2 = Entry(D_F, width=40,borderwidth=5)
        e2.grid(row=4, column=4,padx= 10, pady= 10)
        e2.insert(0, "")
 
        e3_Lbl=Label(D_F,text="First Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e3_Lbl.grid(row=6,column=3)


        e3 = Entry(D_F, width=40,borderwidth=5)
        e3.grid(row=6, column=4,padx= 10, pady= 10)
        e3.insert(0, "")

        e4_Lbl=Label(D_F,text="Last Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e4_Lbl.grid(row=8,column=3)


        e4 = Entry(D_F, width=40,borderwidth=5)
        e4.grid(row=8, column=4,padx= 10, pady= 10)
        e4.insert(0, "")

        e5_Lbl=Label(D_F,text="Email:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e5_Lbl.grid(row=10,column=3)

        e6 = Entry(D_F, width=40,borderwidth=5)
        e6.grid(row=10, column=4,padx= 10, pady= 10)
        e6.insert(0, "")

        e5_Lbl=Label(D_F,text="Address:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e5_Lbl.grid(row=12,column=3)

        e6 = Entry(D_F, width=40,borderwidth=5)
        e6.grid(row=12, column=4,padx= 10, pady= 10)
        e6.insert(0, "")

               
        submitBtn=Button(D_F,text="SUBMIT", command=self.submit_AddCstData,width=30,bg="#2f8fdd",fg='white').grid(row=14,column=4,padx=20,pady=20)
    



    def fetch_Dashboard(self):
        #self.root.destroy()
        obj=dashBoard(root,"User1")
        
    def custMgmtdata(self):
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="CUSTOMER MANAGEMENT",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=1,column=15,padx= 25,pady=25)

        M_FB= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_FB.place(x=400,y=200,width=800,height=180)
        
        SrchBtn=Button(M_FB,text="ADD",command=self.addCustomr,width=30,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=25,padx=40,pady=40)

             
        SrchEBtn=Button(M_FB,text="AUDIT LOG",command=self.fetch_Edata,width=30,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=45,padx=60,pady=40)

        M_FB1= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_FB1.place(x=400,y=500,width=800,height=180)


        lst = [("Id","Name","Rank"),(123,"Raj","1st")]
        coln=len(lst[0])
        #print(len(lst))

        for x in range(len(lst)):
            for y in range(coln):
                self.Table_Row=Entry(M_FB1,width=15,fg='#2f8fdd',font=('Arial',10,'bold'))
                self.Table_Row.grid(row=x,column=y)
                self.Table_Row.insert(END,lst[x][y])

        Act_title=Label(M_FB1,text="Action",font=('Arial',10,'bold'),fg='#2f8fdd').grid(row=0,column=10,padx= 20,pady=20)
        updateBtn=Button(M_FB1,text="UPDATE",command=self.updateCust,width=8,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=10,padx=15,pady=15)
        deleteBtn=Button(M_FB1,text="DELETE",command=self.userManagment,width=8,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=12,padx=20,pady=20)



        
        
        #Tbl_Frame=Frame(D_F,bd=2,relief=RIDGE,bg="#2f8fdd",fg="white")
        #Tbl_Frame.place(x=5,y=160,width=760,height=500)
        #treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        #t = Table(root)

      
        
        '''
        treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(Tbl_Frame,orient ="vertical",command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3","4","5")
          
        # Defining heading
        treev['show'] = 'headings'
          
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 100, anchor ='c')
        treev.column("2", width = 150, anchor ='c')
        treev.column("3", width = 300, anchor ='c')
        treev.column("4", width = 80, anchor ='c')
        treev.column("5", width = 100, anchor ='c')
          
        # Assigning the heading names to the 
        # respective columns
        treev.heading("1", text ="ID")
        treev.heading("2", text ="NAME")
        treev.heading("3", text ="RANK")
        treev.heading("4", text ="ACTION")
        #treev.heading("5", text ="EPARTMENT")
        
        
  
# Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        #cursor.execute("select * from t_courses")
        
        #result= cursor.fetchall()
        #print(len(result))
        result=("123","abc","rank1")
        
        for x in result:
            treev.insert("", 'end', text ="",values =(x[0], x[1], x[2]))
            
        #treev.tag_configure('odd', foreground="white",background='black')
        #treev.tag_configure('even', foreground="black",background='white')
        '''
    '''
    def logout(self,text):
        print(text)

        #3opennewWindow(self)
        root.destroy()
        import login
        #root.destroy()
    '''
        
    def updateCust(self):
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="EDIT CUSTOMER",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
          
        #cursor.execute("select * from register where username=%s")
        
        e1_Lbl=Label(D_F,text="First Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e1_Lbl.grid(row=2,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=2, column=4,padx= 15, pady= 15)
        e1.insert(1, "ABC")
 
        e2_Lbl=Label(D_F,text="Last Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e2_Lbl.grid(row=4,column=3)

        
        e2 = Entry(D_F, width=40,borderwidth=5)
        e2.grid(row=4, column=4,padx= 10, pady= 10)
        e2.insert(0, "XYZ")
 
        e3_Lbl=Label(D_F,text="Rank:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e3_Lbl.grid(row=6,column=3)


        e3 = Entry(D_F, width=40,borderwidth=5)
        e3.grid(row=6, column=4,padx= 10, pady= 10)
        e3.insert(0, "Army")

        e4_Lbl=Label(D_F,text="Mobile:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e4_Lbl.grid(row=8,column=3)


        e4 = Entry(D_F, width=40,borderwidth=5)
        e4.grid(row=8, column=4,padx= 10, pady= 10)
        e4.insert(0, "79798789")

        e5_Lbl=Label(D_F,text="Address:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e5_Lbl.grid(row=10,column=3)

        e6 = Entry(D_F, width=40,borderwidth=5)
        e6.grid(row=10, column=4,padx= 10, pady= 10)
        e6.insert(0, "New delhi")

        
       
        submitBtn=Button(D_F,text="SUBMIT", command=self.submit_AddCstData,width=30,bg="#2f8fdd",fg='white').grid(row=12,column=4,padx=20,pady=20)
        

    def addCustomr(self):
        
        
        #print("Student details")
        #usr=fetch_Studentdata(r)
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="ADD CUSTOMER",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
          
        #cursor.execute("select * from register where username=%s")
        
        e1_Lbl=Label(D_F,text="First Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e1_Lbl.grid(row=2,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=2, column=4,padx= 15, pady= 15)
        e1.insert(1, "")
 
        e2_Lbl=Label(D_F,text="Last Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e2_Lbl.grid(row=4,column=3)

        
        e2 = Entry(D_F, width=40,borderwidth=5)
        e2.grid(row=4, column=4,padx= 10, pady= 10)
        e2.insert(0, "")
 
        e3_Lbl=Label(D_F,text="Rank:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e3_Lbl.grid(row=6,column=3)


        e3 = Entry(D_F, width=40,borderwidth=5)
        e3.grid(row=6, column=4,padx= 10, pady= 10)
        e3.insert(0, "")

        e4_Lbl=Label(D_F,text="Mobile:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e4_Lbl.grid(row=8,column=3)


        e4 = Entry(D_F, width=40,borderwidth=5)
        e4.grid(row=8, column=4,padx= 10, pady= 10)
        e4.insert(0, "")

        e5_Lbl=Label(D_F,text="Address:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e5_Lbl.grid(row=10,column=3)

        e6 = Entry(D_F, width=40,borderwidth=5)
        e6.grid(row=10, column=4,padx= 10, pady= 10)
        e6.insert(0, "")

        
       
        submitBtn=Button(D_F,text="SUBMIT", command=self.submit_AddCstData,width=30,bg="#2f8fdd",fg='white').grid(row=12,column=4,padx=20,pady=20)
        #print(ST_DETAILS)

        #SubmitBtn=Button(D_F,text="EDIT & UPDATE",                 command=lambda: self.submit_Data(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get())
                        # ,width=30,bg="yellow",fg="crimson").grid(row=16,column=3,padx=20,pady=20)        


    def inventMgmtdata(self):
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="INVENTORY MANAGEMENT",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=1,column=15,padx= 25,pady=25)

        M_FB= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_FB.place(x=400,y=200,width=900,height=180)
        
        SrchBtn=Button(M_FB,text="ADD",command=self.addItem,width=30,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=25,padx=40,pady=40)

             
        SrchEBtn=Button(M_FB,text="AUDIT LOG",command=self.fetch_Edata,width=30,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=45,padx=60,pady=40)

        M_FB1= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_FB1.place(x=400,y=500,width=800,height=180)


        lst = [("Name","Quantity","Landing Price","Tax","Handling Charge"),('Raj',10,19,5,10)]
        coln=len(lst[0])
        #print(len(lst))

        for x in range(len(lst)):
            for y in range(coln):
                self.Table_Row=Entry(M_FB1,width=15,fg='#2f8fdd',font=('Arial',10,'bold'))
                self.Table_Row.grid(row=x,column=y)
                self.Table_Row.insert(END,lst[x][y])

        Act_title=Label(M_FB1,text="Action",font=('Arial',10,'bold'),fg='#2f8fdd').grid(row=0,column=10,padx= 20,pady=20)
        updateBtn=Button(M_FB1,text="UPDATE",command=self.updateItem,width=8,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=10,padx=15,pady=15)
        deleteBtn=Button(M_FB1,text="DELETE",command=self.userManagment,width=8,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=12,padx=20,pady=20)
        
        #Tbl_Frame=Frame(D_F,bd=2,relief=RIDGE,bg="#2f8fdd",fg="white")
        #Tbl_Frame.place(x=5,y=160,width=760,height=500)
        #treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        #t = Table(root)

      
        
        '''
        treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(Tbl_Frame,orient ="vertical",command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3","4","5")
          
        # Defining heading
        treev['show'] = 'headings'
          
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 100, anchor ='c')
        treev.column("2", width = 150, anchor ='c')
        treev.column("3", width = 300, anchor ='c')
        treev.column("4", width = 80, anchor ='c')
        treev.column("5", width = 100, anchor ='c')
          
        # Assigning the heading names to the 
        # respective columns
        treev.heading("1", text ="ID")
        treev.heading("2", text ="NAME")
        treev.heading("3", text ="RANK")
        treev.heading("4", text ="ACTION")
        #treev.heading("5", text ="EPARTMENT")
        
        
  
# Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        #cursor.execute("select * from t_courses")
        
        #result= cursor.fetchall()
        #print(len(result))
        result=("123","abc","rank1")
        
        for x in result:
            treev.insert("", 'end', text ="",values =(x[0], x[1], x[2]))
            
        #treev.tag_configure('odd', foreground="white",background='black')
        #treev.tag_configure('even', foreground="black",background='white')
        '''
    '''
    def logout(self,text):
        print(text)

        #3opennewWindow(self)
        root.destroy()
        import login
        #root.destroy()
    '''
        
    def updateItem(self):
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="EDIT ITEM",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
          
        #cursor.execute("select * from register where username=%s")
        
        e1_Lbl=Label(D_F,text="Item Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e1_Lbl.grid(row=2,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=2, column=4,padx= 15, pady= 15)
        e1.insert(1, "ABC")
 
        e2_Lbl=Label(D_F,text="Quantity:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e2_Lbl.grid(row=4,column=3)

        
        e2 = Entry(D_F, width=40,borderwidth=5)
        e2.grid(row=4, column=4,padx= 10, pady= 10)
        e2.insert(0, "10")
 
        e3_Lbl=Label(D_F,text="Landing Price:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e3_Lbl.grid(row=6,column=3)


        e3 = Entry(D_F, width=40,borderwidth=5)
        e3.grid(row=6, column=4,padx= 10, pady= 10)
        e3.insert(0, "100")

        e4_Lbl=Label(D_F,text="Tax:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e4_Lbl.grid(row=8,column=3)


        e4 = Entry(D_F, width=40,borderwidth=5)
        e4.grid(row=8, column=4,padx= 10, pady= 10)
        e4.insert(0, "10")

        e5_Lbl=Label(D_F,text="Handling Charge:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e5_Lbl.grid(row=10,column=3)

        e5 = Entry(D_F, width=40,borderwidth=5)
        e5.grid(row=10, column=4,padx= 10, pady= 10)
        e5.insert(0, "10")

        e6_Lbl=Label(D_F,text="Rate:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e6_Lbl.grid(row=12,column=3)

        e6 = Entry(D_F, width=40,borderwidth=5)
        e6.grid(row=12, column=4,padx= 10, pady= 10)
        e6.insert(0, "1000")

        
       
        submitBtn=Button(D_F,text="SUBMIT", command=self.submit_AddCstData,width=30,bg="#2f8fdd",fg='white').grid(row=14,column=4,padx=20,pady=20)
        

    def addItem(self):
        
        
        #print("Student details")
        #usr=fetch_Studentdata(r)
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="ADD ITEM",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
          
        #cursor.execute("select * from register where username=%s")
        
        e1_Lbl=Label(D_F,text="Item Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e1_Lbl.grid(row=2,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=2, column=4,padx= 15, pady= 15)
        e1.insert(1, "")
 
        e2_Lbl=Label(D_F,text="Quantity:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e2_Lbl.grid(row=4,column=3)

        
        e2 = Entry(D_F, width=40,borderwidth=5)
        e2.grid(row=4, column=4,padx= 10, pady= 10)
        e2.insert(0, "")
 
        e3_Lbl=Label(D_F,text="Landing Price:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e3_Lbl.grid(row=6,column=3)


        e3 = Entry(D_F, width=40,borderwidth=5)
        e3.grid(row=6, column=4,padx= 10, pady= 10)
        e3.insert(0, "")

        e4_Lbl=Label(D_F,text="Tax:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e4_Lbl.grid(row=8,column=3)


        e4 = Entry(D_F, width=40,borderwidth=5)
        e4.grid(row=8, column=4,padx= 10, pady= 10)
        e4.insert(0, "")

        e5_Lbl=Label(D_F,text="Handling Charge:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e5_Lbl.grid(row=10,column=3)

        e5 = Entry(D_F, width=40,borderwidth=5)
        e5.grid(row=10, column=4,padx= 10, pady= 10)
        e5.insert(0, "")

        e6_Lbl=Label(D_F,text="Rate:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e6_Lbl.grid(row=12,column=3)

        e6 = Entry(D_F, width=40,borderwidth=5)
        e6.grid(row=12, column=4,padx= 10, pady= 10)
        e6.insert(0, "")

        
       
        submitBtn=Button(D_F,text="SUBMIT", command=self.submit_AddCstData,width=30,bg="#2f8fdd",fg='white').grid(row=14,column=4,padx=20,pady=20)

    def rankMgmtdata(self):
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="RANK MANAGEMENT",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=1,column=15,padx= 25,pady=25)

        M_FB= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_FB.place(x=400,y=200,width=800,height=180)
        
        SrchBtn=Button(M_FB,text="ADD",command=self.addRank,width=30,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=25,padx=40,pady=40)

             
        SrchEBtn=Button(M_FB,text="AUDIT LOG",command=self.fetch_Edata,width=30,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=45,padx=60,pady=40)

        M_FB1= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_FB1.place(x=400,y=500,width=800,height=180)

        lst = [("Rank Id","Rank Name","Created Date"),(123,"Raj","08th sep 2021")]
        coln=len(lst[0])
        #print(len(lst))

        for x in range(len(lst)):
            for y in range(coln):
                self.Table_Row=Entry(M_FB1,width=15,fg='#2f8fdd',font=('Arial',10,'bold'))
                self.Table_Row.grid(row=x,column=y)
                self.Table_Row.insert(END,lst[x][y])

        Act_title=Label(M_FB1,text="Action",font=('Arial',10,'bold'),fg='#2f8fdd').grid(row=0,column=10,padx= 20,pady=20)
        updateBtn=Button(M_FB1,text="UPDATE",command=self.updateRank,width=8,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=10,padx=15,pady=15)
        deleteBtn=Button(M_FB1,text="DELETE",command=self.userManagment,width=8,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=12,padx=20,pady=20)


        
        #Tbl_Frame=Frame(D_F,bd=2,relief=RIDGE,bg="#2f8fdd",fg="white")
        #Tbl_Frame.place(x=5,y=160,width=760,height=500)
        #treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        #t = Table(root)

      
        
        '''
        treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(Tbl_Frame,orient ="vertical",command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3","4","5")
          
        # Defining heading
        treev['show'] = 'headings'
          
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 100, anchor ='c')
        treev.column("2", width = 150, anchor ='c')
        treev.column("3", width = 300, anchor ='c')
        treev.column("4", width = 80, anchor ='c')
        treev.column("5", width = 100, anchor ='c')
          
        # Assigning the heading names to the 
        # respective columns
        treev.heading("1", text ="ID")
        treev.heading("2", text ="NAME")
        treev.heading("3", text ="RANK")
        treev.heading("4", text ="ACTION")
        #treev.heading("5", text ="EPARTMENT")
        
        
  
# Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        #cursor.execute("select * from t_courses")
        
        #result= cursor.fetchall()
        #print(len(result))
        result=("123","abc","rank1")
        
        for x in result:
            treev.insert("", 'end', text ="",values =(x[0], x[1], x[2]))
            
        #treev.tag_configure('odd', foreground="white",background='black')
        #treev.tag_configure('even', foreground="black",background='white')
        '''
    '''
    def logout(self,text):
        print(text)

        #3opennewWindow(self)
        root.destroy()
        import login
        #root.destroy()
    '''
        
    def updateRank(self):
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="EDIT RANK",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
          
        #cursor.execute("select * from register where username=%s")
        
        e1_Lbl=Label(D_F,text="Rank Id:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e1_Lbl.grid(row=2,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=2, column=4,padx= 15, pady= 15)
        e1.insert(1, "ABC")
 
        e2_Lbl=Label(D_F,text="Rank Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e2_Lbl.grid(row=4,column=3)

        
        e2 = Entry(D_F, width=40,borderwidth=5)
        e2.grid(row=4, column=4,padx= 10, pady= 10)
        e2.insert(0, "XYZ")
 
               
       
        submitBtn=Button(D_F,text="SUBMIT", command=self.submit_AddCstData,width=30,bg="#2f8fdd",fg='white').grid(row=6,column=4,padx=20,pady=20)
        

    def addRank(self):
        
        
        #print("Student details")
        #usr=fetch_Studentdata(r)
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="ADD RANK",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
          
        #cursor.execute("select * from register where username=%s")
        
        e1_Lbl=Label(D_F,text="Rank Id:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e1_Lbl.grid(row=2,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=2, column=4,padx= 15, pady= 15)
        e1.insert(1, "")
 
        e2_Lbl=Label(D_F,text="Rank Name:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e2_Lbl.grid(row=4,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=4, column=4,padx= 15, pady= 15)
        e1.insert(1, "")

        
        

        
       
        submitBtn=Button(D_F,text="SUBMIT", command=self.submit_AddCstData,width=30,bg="#2f8fdd",fg='white').grid(row=6,column=4,padx=20,pady=20)

    def quotMgmtdata(self):
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="QUOTA MANAGEMENT",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=1,column=15,padx= 25,pady=25)

        M_FB= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_FB.place(x=400,y=200,width=800,height=180)
        
        SrchBtn=Button(M_FB,text="ADD",command=self.addQuota,width=30,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=25,padx=40,pady=40)

             
        SrchEBtn=Button(M_FB,text="AUDIT LOG",command=self.fetch_Edata,width=30,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=45,padx=60,pady=40)

        M_FB1= Frame(self.root,bd=2,relief=RIDGE,bg="#f3fbfe")
        M_FB1.place(x=400,y=500,width=800,height=180)

        lst = [("Rank ","Quantity"),(123,100)]
        coln=len(lst[0])
        #print(len(lst))

        for x in range(len(lst)):
            for y in range(coln):
                self.Table_Row=Entry(M_FB1,width=15,fg='#2f8fdd',font=('Arial',10,'bold'))
                self.Table_Row.grid(row=x,column=y)
                self.Table_Row.insert(END,lst[x][y])

        Act_title=Label(M_FB1,text="Action",font=('Arial',10,'bold'),fg='#2f8fdd').grid(row=0,column=10,padx= 20,pady=20)
        updateBtn=Button(M_FB1,text="UPDATE",command=self.updateQuota,width=8,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=10,padx=15,pady=15)
        deleteBtn=Button(M_FB1,text="DELETE",command=self.userManagment,width=8,height=2,bg="#2f8fdd",fg="white").grid(row=1,column=12,padx=20,pady=20)
        
        #Tbl_Frame=Frame(D_F,bd=2,relief=RIDGE,bg="#2f8fdd",fg="white")
        #Tbl_Frame.place(x=5,y=160,width=760,height=500)
        #treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        #t = Table(root)

      
        
        '''
        treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(Tbl_Frame,orient ="vertical",command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3","4","5")
          
        # Defining heading
        treev['show'] = 'headings'
          
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 100, anchor ='c')
        treev.column("2", width = 150, anchor ='c')
        treev.column("3", width = 300, anchor ='c')
        treev.column("4", width = 80, anchor ='c')
        treev.column("5", width = 100, anchor ='c')
          
        # Assigning the heading names to the 
        # respective columns
        treev.heading("1", text ="ID")
        treev.heading("2", text ="NAME")
        treev.heading("3", text ="RANK")
        treev.heading("4", text ="ACTION")
        #treev.heading("5", text ="EPARTMENT")
        
        
  
# Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        #cursor.execute("select * from t_courses")
        
        #result= cursor.fetchall()
        #print(len(result))
        result=("123","abc","rank1")
        
        for x in result:
            treev.insert("", 'end', text ="",values =(x[0], x[1], x[2]))
            
        #treev.tag_configure('odd', foreground="white",background='black')
        #treev.tag_configure('even', foreground="black",background='white')
        '''
    '''
    def logout(self,text):
        print(text)

        #3opennewWindow(self)
        root.destroy()
        import login
        #root.destroy()
    '''
        
    def updateQuota(self):
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="EDIT QUOTA",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
          
        #cursor.execute("select * from register where username=%s")
        
        e1_Lbl=Label(D_F,text="Rank:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e1_Lbl.grid(row=2,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=2, column=4,padx= 15, pady= 15)
        e1.insert(1, "123")
 
        e2_Lbl=Label(D_F,text="Quantity:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e2_Lbl.grid(row=4,column=3)

        
        e2 = Entry(D_F, width=40,borderwidth=5)
        e2.grid(row=4, column=4,padx= 10, pady= 10)
        e2.insert(0, "100")
 
                
       
        submitBtn=Button(D_F,text="SUBMIT", command=self.submit_AddCstData,width=30,bg="#2f8fdd",fg='white').grid(row=6,column=4,padx=20,pady=20)
        

    def addQuota(self):
        
        
        #print("Student details")
        #usr=fetch_Studentdata(r)
        D_F= Frame(self.root,bd=2,relief=RAISED,bg="#f3fbfe")
        D_F.place(x=400,y=100,width=1030,height=580)
          
        M_title=Label(D_F,text="ADD QUOTA",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
          
        #cursor.execute("select * from register where username=%s")
        
        e1_Lbl=Label(D_F,text="Rank:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e1_Lbl.grid(row=2,column=3)

        e1 = Entry(D_F, width=40,borderwidth=5)
        e1.grid(row=2, column=4,padx= 15, pady= 15)
        e1.insert(1, "")
 
        e2_Lbl=Label(D_F,text="Quantity:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        e2_Lbl.grid(row=4,column=3)

        
        e2 = Entry(D_F, width=40,borderwidth=5)
        e2.grid(row=4, column=4,padx= 10, pady= 10)
        e2.insert(0, "")
 
               
       
        submitBtn=Button(D_F,text="SUBMIT", command=self.submit_AddCstData,width=30,bg="#2f8fdd",fg='white').grid(row=6,column=4,padx=20,pady=20)

    def submit_AddCstData(self):
        pass
        '''
        
    def submit_Data(self,E1,E2,E3,E4,E5,E6,E7):
        pass
        '''
        '''
        #print(E1)
        Update = "Update register set Firstname='%s', Lastname='%s', Email='%s', Phone='%s', State='%s', City='%s',Country='%s' where username='%s'" % (
                  E1, E2, E3, E4, E5, E6 , E7, self.usr[0])
        cursor.execute(Update)
        db.commit()
        #S_l1=[E1, E2, E3, E4, E5, E6 , E7]
        #print(S_l1)
        
        
        D_F= Frame(self.root,bd=4,relief=RAISED,bg="#2f8fdd")
        D_F.place(x=300,y=100,width=800,height=600)
          
        M_title=Label(D_F,text="UPDATED SUCCESSFULLY",font=("times new roman",10,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,columnspan=2,pady=20)

        SubmitBtn=Button(D_F,text="RETURN",
                         command=self.fetch_STdata,width=30,bg="#2f8fdd",fg="white").grid(row=16,column=3,padx=20,pady=20)
        
        print("Submit student details")        
        '''

    def fetch_Edata(self):
        pass
        #print("HI")
        '''
        D_F= Frame(self.root,bd=4,relief=RIDGE,bg="#2f8fdd")
        D_F.place(x=300,y=100,width=850,height=600)
        M_title=Label(D_F,text="EDUCATION LEVEL",font=("times new roman",20,"bold"),bg="crimson",fg='white')
        M_title.grid(row=0,padx=20,pady=20)
        

        combo_srch=ttk.Combobox(D_F,font=("times new roman",10,"bold"),state='readonly')
        combo_srch['values']=("DIPLOMA","UG","PG","PH.D","OTHERS")
        combo_srch.grid(row=1,column=1,padx=20,pady=10)
        
           
        Tbl_Frame=Frame(D_F,bd=4,relief=RIDGE,bg="crimson")
        Tbl_Frame.place(x=5,y=60,width=760,height=500)
        
        treev = ttk.Treeview(Tbl_Frame, selectmode ='browse')
        
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(Tbl_Frame,orient ="vertical",command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3","4","5")
          
        # Defining heading
        treev['show'] = 'headings'
          
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 100, anchor ='c')
        treev.column("2", width = 150, anchor ='c')
        treev.column("3", width = 300, anchor ='c')
        treev.column("4", width = 80, anchor ='c')
        treev.column("5", width = 100, anchor ='c')
          
        # Assigning the heading names to the 
        # respective columns
        treev.heading("1", text ="COURSE CODE")
        treev.heading("2", text ="COURSE NAME")
        treev.heading("3", text ="COURSE DESCRIPTION")
        treev.heading("4", text ="COURSE TYPE")
        treev.heading("5", text ="DEPARTMENT")
        
        
  
# Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        cursor.execute("select * from t_courses")
        
        result= cursor.fetchall()
        print(len(result))
        i=0
        for x in result:
            
            if len(result)%2==0:
                treev.insert("", 'end', text ="",values =(x[0], x[1], x[2],x[3],x[4]),tags=("even",))
            else:
                treev.insert("", 'end', text ="",values =(x[0], x[1], x[2],x[3],x[4]),tags=("odd",))
            i=i+1
        treev.tag_configure('odd', foreground="white",background='black')
        treev.tag_configure('even', foreground="black",background='white')
        Btn_Sub=Button(D_F,text=" ENROLL SUBJECT DETAILS",command=self.fetch_Subjdetails,width=30,bg="yellow",fg="crimson").grid(row=8,column=1,padx=20,pady=20)
        '''

                   
    def fetch_Subjdetails(self):
        pass
        #print("Subject details")
        '''

        D_F= Frame(self.root,bd=4,relief=RAISED,bg="crimson")
        D_F.place(x=300,y=100,width=800,height=600)
        nam=self.usr[2].upper()
        M_title=Label(D_F,text="Enroll Subject Details",font=("times new roman",20,"bold"),bg="#2f8fdd",fg='white')
        M_title.grid(row=0,column=3,padx= 15,pady=15)
        s1_Lbl=Label(D_F,text="Subject Enrollment for : "+nam,font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        s1_Lbl.grid(row=2,column=2)

        
        #s1.insert(1, self.usr[9])

        s2_Lbl=Label(D_F,text="SUBJECT NAME:",font=("times new roman",13,"bold"),bg="#2f8fdd",fg='white')
        s2_Lbl.grid(row=3,column=2)
        
        #s2.insert(0, self.usr[3])
        
        combo_srch=ttk.Combobox(D_F,font=("times new roman",10,"bold"),state='readonly')
        combo_srch['values']=("SUBJ1","SUBJ2","SUBJ3","SUBJ4","SUBJ5")
        combo_srch.grid(row=3,column=3,padx=20,pady=10)

        Btn_SubDetails=Button(D_F,text="ENROLL SUBJECT",command=self.SubmitSubDetails,width=30,bg="yellow",fg="crimson").grid(row=5,column=3,padx=20,pady=20)
        '''
        

        

    def SubmitSubDetails(self):
        pass
        
    def fetch_Sdata(self):
        pass
        #print("HI")
        '''

        D_F= Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        D_F.place(x=300,y=100,width=850,height=600)    
        

        Btn_Staff=Button(D_F,text="STAFF INFO...",
                         command=self.fetch_STdetails,width=30,bg="yellow",fg="crimson").grid(row=8,column=1,padx=20,pady=20)

        Btn_Mgmt=Button(D_F,text="MANAGEMENT INFO...",command=self.fetchMgmtDetails,width=30,bg="yellow",fg="crimson").grid(row=8,column=2,padx=20,pady=20)

        Btn_AcdMgmt=Button(D_F,text="ACADEMIC INFO...",command=self.fetchAcadDetails,width=30,bg="yellow",fg="crimson").grid(row=8,column=3,padx=20,pady=20)
        

        
        
        T = Text(self.root, height = 5, width = 52)
        Fact = """A man can be arrested in Italy for wearing a skirt in public."""
        T.pack()

        T.insert(tk.END, Fact)
        
        
        
        combo_srch=ttk.Combobox(D_F,font=("times new roman",10,"bold"),state='readonly')
        combo_srch['values']=("ADMIN","TEACHING","NON-TEACHING","OTHERS")
        combo_srch.grid(row=1,column=1,padx=20,pady=10)
        
        '''
  
    def fetch_STdetails(self):
        pass
        

        '''
        D_F= Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        D_F.place(x=300,y=200,width=850,height=600)
        M_title=Label(D_F,text="STAFF DETAILS  ",font=("times new roman",20,"bold"),bg="crimson",fg='white')
        M_title.grid(row=0,padx= 15,pady=15)

        Tbl_Frame=Frame(D_F,bd=4,relief=RIDGE,bg="crimson")
        Tbl_Frame.place(x=5,y=60,width=760,height=500)
        
        trv=ttk.Treeview(Tbl_Frame,selectmode='browse')
        trv.pack(side='top')
        verscrlbar = ttk.Scrollbar(Tbl_Frame,orient ="vertical",command = trv.yview)
        verscrlbar.pack(side ='right', fill ='x')
        trv.configure(xscrollcommand = verscrlbar.set)
        trv["columns"] = ("1", "2", "3")
        trv['show'] = 'headings'
        trv.column("1", width = 100, anchor ='c')
        trv.column("2", width = 150, anchor ='c')
        trv.column("3", width = 300, anchor ='c')
        trv.heading("1", text ="STAFF ID")
        trv.heading("2", text ="STAFF TYPE")
        trv.heading("3", text ="STAFF INFORMATION")
        trv.configure(xscrollcommand = verscrlbar.set)
        cursor.execute("select * from staff")
        result= cursor.fetchall()
        for x in result:
            trv.insert("",'end',text="",values=(x[0],x[1],x[2]))
        '''
	
    def fetchMgmtDetails(self):
        pass
        '''
        
        D_F= Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        D_F.place(x=300,y=200,width=850,height=600)

        M_title=Label(D_F,text="MANAGEMENT DETAILS  ",font=("times new roman",20,"bold"),bg="crimson",fg='white')
        M_title.grid(row=0,padx= 15,pady=15)

        Tbl_Frame=Frame(D_F,bd=4,relief=RIDGE,bg="crimson")
        Tbl_Frame.place(x=5,y=60,width=760,height=500)
        
      
        trv=ttk.Treeview(Tbl_Frame,selectmode='browse')
        trv.pack(side='top')
        verscrlbar = ttk.Scrollbar(Tbl_Frame,orient ="vertical",command = trv.yview)
        verscrlbar.pack(side ='right', fill ='x')
        trv.configure(xscrollcommand = verscrlbar.set)
        trv["columns"] = ("1", "2", "3")
        trv['show'] = 'headings'
        trv.column("1", width = 100, anchor ='c')
        trv.column("2", width = 150, anchor ='c')
        trv.column("3", width = 300, anchor ='c')
        trv.heading("1", text ="STAFF ID")
        trv.heading("2", text ="MANAGEMENT TYPE")
        trv.heading("3", text ="MANAGEMENT INFORMATION")
        trv.configure(xscrollcommand = verscrlbar.set)
        cursor.execute("select * from staff_mgmt")
        result= cursor.fetchall()
        for x in result:
            #print(x)
            trv.insert("",'end',text="",values=(x[0],x[1],x[2]))
        
        '''
        
    def fetchAcadDetails(self):
        pass
        '''
        D_F= Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        D_F.place(x=300,y=200,width=850,height=600)
        M_title=Label(D_F,text="ACADEMIC DETAILS  ",font=("times new roman",20,"bold"),bg="crimson",fg='white')
        M_title.grid(row=0,padx= 15,pady=15)

        Tbl_Frame=Frame(D_F,bd=4,relief=RIDGE,bg="crimson")
        Tbl_Frame.place(x=5,y=60,width=760,height=500)
                
        trv=ttk.Treeview(Tbl_Frame,selectmode='browse')
        trv.pack(side='top')
        verscrlbar = ttk.Scrollbar(Tbl_Frame,orient ="vertical",command = trv.yview)
        verscrlbar.pack(side ='right', fill ='x')
        trv.configure(xscrollcommand = verscrlbar.set)
        trv["columns"] = ("1", "2", "3")
        trv['show'] = 'headings'
        trv.column("1", width = 100, anchor ='c')
        trv.column("2", width = 150, anchor ='c')
        trv.column("3", width = 300, anchor ='c')
        trv.heading("1", text ="STAFF ID")
        trv.heading("2", text ="ACADEIC TYPE")
        trv.heading("3", text ="ACADEMIC INFORMATION")
        trv.configure(xscrollcommand = verscrlbar.set)
        cursor.execute("select * from staff_academic")
        result= cursor.fetchall()
        for x in result:
            trv.insert("",'end',text="",values=(x[0],x[1],x[2]))
        '''
       

        
    def fetch_Studentdata(self):
        
        cursor.execute("select * from register")
        result= cursor.fetchall()
        
        for x in result:

            print(x[0],x[1])  

        #return x

        
        db.commit()        
    
                           

                



def logintodb(user, passw):
     
    # If paswword is enetered by the
    # user
    if user=="" and passw =="":
        lble = tk.Label(root,bg='green',fg="red", text ="Username & Password Should not be empty",font=("times new roman",15,"bold"))
        lble.place(x = 500, y = 380)
    #s = requests.Session()
    x=[]
    #s.auth = ('user', 'passw')
    #print(s[0])
    if passw:
        cursor.execute("select * from register where username=%s and password = %s",(user,passw))
        #print("select * from register where username=%s and password = %s",(user,passw))

        try:
            #cursor.execute(savequery)
            myresult = cursor.fetchall()

            # Printing the result of the
            # query
            print(myresult)
            for x in myresult:
                print(x)

                if(x!=None):
                    #lble.destroy()
                    lbls = tk.Label(root, text ="Logined successfully")
                    lbls.place(x = 350, y = 250)
                    obj=dashBoard(root,x)
                    print("Query Excecuted successfully")
            if(len(myresult)==0):
                #lbls.destroy()
                lble = tk.Label(root,bg='green',fg="yellow", text ="Incorrect Username/Password",font=("times new roman",15,"bold"))
                lble.place(x = 500, y = 380)
                
         
        except:
            db.rollback()
            print("Error occured")
         
    # If no password is enetered by the
    # user
    else:
        
        print("LOGIN FAILURE")

'''
def Showall():
    root = tk.Tk()
    root.title("Student Details Page")
    root.geometry("900x900")
    photo = PhotoImage(file='Registration.png')
    label12 = Label(root, image=photo).grid(row=0, column=0)
    #root.title("Overview Page")
    
'''

root = tk.Tk()
root.geometry("1350x700+0+0")
bg = PhotoImage(file = "bg.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
root.title("LIQR SHOP SYS-APP ")
root.config(background="coral")
#root.

#print(user)
title=Label(root,text="LIQUOR SHOP",font=("times new roman",28,"bold"),bg="#f3fbfe",fg='#2f8fdd')
title.pack(side=TOP,fill=X)
 
 
# Definging the first row
lblfrstrow = tk.Label(root, text ="USER NAME: -", bg="#f3fbfe",fg="#2f8fdd")
lblfrstrow.place(x = 400, y = 250,width = 100,height=30)
 
Username = tk.Entry(root,fg='crimson', width = 100,font=("times new roman",14,"bold"))
Username.place(x = 500, y = 250, width = 250,height=30)
  
lblsecrow = tk.Label(root, text ="PASSWORD: -",bg="#f3fbfe",fg="#2f8fdd")
lblsecrow.place(x = 400, y = 300,width = 100,height=30)
 
password = tk.Entry(root,fg='crimson', show='*',width = 100,font=("times new roman",14,"bold"))
password.place(x = 500, y = 300, width = 250,height=30)


#photo = PhotoImage(file='login.png')

submitbtn = tk.Button(root, text ="LOGIN",font=("times new roman",12,"bold"),
                      bg ='#2f8fdd',fg='white', command = submitact)
submitbtn.place(x =540, y = 340, width = 80,height=35)
 
exitbtn = tk.Button(root, text ="EXIT",font=("times new roman",12,"bold"),	
                      bg ='#2f8fdd',fg='white' ,command = exitact)
exitbtn.place(x = 640, y = 340, width = 80,height=35)

# Python program to create a table


root.mainloop()
