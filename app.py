from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import Database
from QRCode import QRCode 
import datetime
class Employee:
	def __init__(self,root):
		self.root=root
		self.root.title("Employee Attendance")
		self.root.geometry("1550x800+0+0")

		self.EmployeeID=""

		self.name_var=StringVar()
		self.dob_var=StringVar()
		self.gender_var=StringVar()
		self.dpmnt_var=StringVar()
		self.phone_var=StringVar()
		self.email_var=StringVar()

		self.search_by=StringVar()
		self.search_text=StringVar()

		title=Label(self.root,text="Employee Attendance Management System",font=("times new roman",30,"bold"),fg="#242536",bg="#44AF69",bd=4)
		title.pack(side=TOP,fill=X)


		#Manage Frame
		Manage_frame= Frame(self.root,bd=4,relief=RIDGE,bg="#44AF69")
		Manage_frame.place(x=10,y=60,width=550,height=640)

		#Manage Title
		M_title= Label(Manage_frame,text="Manage Employees",font=("times new roman",20,"bold"),fg="#F5F5F7",bg="#242536",bd=4,relief=RAISED)
		M_title.grid(row=0,columnspan=2,padx=10,pady=10)

		#labels
		lbl_name=Label(Manage_frame,text="Name",font=("times new roman",20,"bold"),fg="#242536",bg="#44AF69",bd=4)
		lbl_name.grid(row=1,column=0,padx=20,pady=10,sticky=W)

		lbl_dob=Label(Manage_frame,text="DOB",font=("times new roman",20,"bold"),fg="#242536",bg="#44AF69",bd=4)
		lbl_dob.grid(row=2,column=0,padx=20,pady=10,sticky=W)

		lbl_gender=Label(Manage_frame,text="Gender",font=("times new roman",20,"bold"),fg="#242536",bg="#44AF69",bd=4)
		lbl_gender.grid(row=3,column=0,padx=20,pady=10,sticky=W)

		lbl_dpmnt=Label(Manage_frame,text="Department",font=("times new roman",20,"bold"),fg="#242536",bg="#44AF69",bd=4)
		lbl_dpmnt.grid(row=4,column=0,padx=20,pady=10,sticky=W)

		lbl_phone=Label(Manage_frame,text="Phone Number",font=("times new roman",20,"bold"),fg="#242536",bg="#44AF69",bd=4)
		lbl_phone.grid(row=5,column=0,padx=20,pady=10,sticky=W)

		lbl_email=Label(Manage_frame,text="Email",font=("times new roman",20,"bold"),fg="#242536",bg="#44AF69",bd=4)
		lbl_email.grid(row=6,column=0,padx=20,pady=10,sticky=W)

		lbl_address=Label(Manage_frame,text="Address",font=("times new roman",20,"bold"),fg="#242536",bg="#44AF69",bd=4)
		lbl_address.grid(row=7,column=0,padx=20,pady=10,sticky=W)



		name_entry=ttk.Entry(Manage_frame,textvariable=self.name_var,font=("times new roman",20,"bold"))
		name_entry.grid(row=1,column=1,padx=20,pady=10,sticky=W)

		dob_entry=ttk.Entry(Manage_frame,textvariable=self.dob_var,font=("times new roman",20,"bold"))
		dob_entry.grid(row=2,column=1,padx=20,pady=10,sticky=W)

		combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,width=19,font=("times new roman",20,"bold"),state="readonly")
		combo_gender["values"]=("Male","Female","Other")
		combo_gender.grid(row=3,column=1,padx=20,pady=10,sticky=W)


		dpmnt_entry=ttk.Entry(Manage_frame,textvariable=self.dpmnt_var,font=("times new roman",20,"bold"))
		dpmnt_entry.grid(row=4,column=1,padx=20,pady=10,sticky=W)

		phone_entry=ttk.Entry(Manage_frame,textvariable=self.phone_var,font=("times new roman",20,"bold"))
		phone_entry.grid(row=5,column=1,padx=20,pady=10,sticky=W)

		email_entry=ttk.Entry(Manage_frame,textvariable=self.email_var,font=("times new roman",20,"bold"))
		email_entry.grid(row=6,column=1,padx=20,pady=10,sticky=W)

		self.address_text=Text(Manage_frame,width=20,height=2,font=("times new roman",20,"bold"))
		self.address_text.grid(row=7,column=1,padx=20,pady=10,sticky=W)


		#First Buttons Frame
		Buttons_frame= Frame(self.root,bd=2,relief=RIDGE,bg="#44AF69")
		Buttons_frame.place(x=25,y=570,width=520)

		add_btn=Button(Buttons_frame,text="ADD",width=10,height=1,fg="White",bg="#242536",command=self.add_employee)
		add_btn.grid(row=0,column=0,padx=10,pady=10,sticky=W)

		update_btn=Button(Buttons_frame,text="UPDATE",width=10,height=1,fg="White",bg="#242536",command=self.update)
		update_btn.grid(row=0,column=1,padx=10,pady=10)

		delete_btn=Button(Buttons_frame,text="DELETE",width=10,height=1,fg="White",bg="#242536",command=self.delete)
		delete_btn.grid(row=0,column=2,padx=10,pady=10)

		clear_btn=Button(Buttons_frame,text="CLEAR",width=10,height=1,fg="White",bg="#242536",command=self.clear)
		clear_btn.grid(row=0,column=3,padx=10,pady=10)

		#Second Buttons Frame
		Buttons_frame2= Frame(self.root,bd=2,relief=RIDGE,bg="#44AF69")
		Buttons_frame2.place(x=25,y=630,width=520)

		attendance_btn1=Button(Buttons_frame2,text="ATTENDANCE IN",width=15,height=1,fg="White",bg="#242536",command=self.mark_attendance_In)
		attendance_btn1.grid(row=1,column=0,padx=10,pady=10)

		attendance_btn2=Button(Buttons_frame2,text="ATTENDANCE OUT",width=15,height=1,fg="White",bg="#242536",command=self.mark_attendance_Out)
		attendance_btn2.grid(row=1,column=1,padx=10,pady=10)

		report_btn=Button(Buttons_frame2,text="REPORT",width=15,height=1,fg="White",bg="#242536",command=self.generate_report)
		report_btn.grid(row=1,column=2,padx=10,pady=10)




		#Details Frame
		Details_frame= Frame(self.root,bd=4,relief=RIDGE,bg="#44AF69")
		Details_frame.place(x=570,y=60,width=780,height=640)

		search_lb1=Label(Details_frame,text="Search By",font=("times new roman",15,"bold"),fg="#242536",bg="#44AF69")
		search_lb1.grid(row=1,column=0,padx=20,pady=10,sticky=W)

		search_combo=ttk.Combobox(Details_frame,textvariable=self.search_by,width=15,font=("times new roman",15,"bold"),state="readonly")
		search_combo["values"]=("Select Option","name","EmpID","phone")
		search_combo.grid(row=1,column=1,padx=20,pady=10,sticky=W)

		search_entry=ttk.Entry(Details_frame,textvariable=self.search_text,font=("times new roman",15,"bold"))
		search_entry.grid(row=1,column=2,padx=20,pady=10,sticky=E)

		search_btn=Button(Details_frame,text="SEARCH",width=6,height=1,fg="White",bg="#242536",command=self.search_data)
		search_btn.grid(row=1,column=3,padx=10,pady=10)

		showall_btn=Button(Details_frame,text="SHOWALL",width=6,height=1,fg="White",bg="#242536",command=self.fetch_all_data)
		showall_btn.grid(row=1,column=4,padx=10,pady=10)

		#Table Frame
		Table_frame= Frame(Details_frame,bd=4,relief=RIDGE,bg="powder blue")
		Table_frame.place(x=10,y=70,width=750,height=550)

		scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

		self.employee_table=ttk.Treeview(Table_frame,column=("EmpID","name","dob","gender","dpmnt","phone","email","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.employee_table.xview)
		scroll_y.config(command=self.employee_table.yview)
		
		self.employee_table.heading("EmpID",text="Employee ID")
		self.employee_table.heading("name",text="Name")
		self.employee_table.heading("dob",text="DOB")
		self.employee_table.heading("gender",text="Gender")
		self.employee_table.heading("dpmnt",text="Department")
		self.employee_table.heading("phone",text="Phone")
		self.employee_table.heading("email",text="Email")
		self.employee_table.heading("address",text="Address")

		self.employee_table.column("EmpID",width=120)
		self.employee_table.column("name",width=150)
		self.employee_table.column("dob",width=120)
		self.employee_table.column("gender",width=100)
		self.employee_table.column("dpmnt",width=100)
		self.employee_table.column("phone",width=120)
		self.employee_table.column("email",width=150)
		self.employee_table.column("address",width=150)


		self.employee_table["show"]="headings"
		self.employee_table.pack(fill=BOTH,expand=1)

		self.employee_table.bind("<ButtonRelease-1>",self.get_cursor)
		#self.employee_table.bind("<ButtonRelease-1>",self.get_ID)
		self.fetch_all_data()

	def add_employee(self):
		db=Database()
		EmpId=QRCode()
		db.new_User(EmpId.generate(),
			self.name_var.get(),
			self.dob_var.get(),
			self.gender_var.get(),
			self.dpmnt_var.get(),
			self.phone_var.get(),
			self.email_var.get(),
			self.address_text.get("1.0",END))

		self.fetch_all_data()

	def update(self):
		db=Database()
		db.update(self.EmployeeID,
			self.name_var.get(),
			self.dob_var.get(),
			self.gender_var.get(),
			self.dpmnt_var.get(),
			self.phone_var.get(),
			self.email_var.get(),
			self.address_text.get("1.0",END))

		self.fetch_all_data()

	def delete(self):
		db=Database()
		db.delete(self.EmployeeID)

		self.fetch_all_data()

	def fetch_all_data(self):
		db=Database()
		rows=db.fetch_all_data()
		if len(rows)!=0:
			self.employee_table.delete(*self.employee_table.get_children())
			for i in rows:
				self.employee_table.insert("",END,values=i)


	def search_data(self):
		db=Database()
		rows=db.search(self.search_by.get(),self.search_text.get())
		if len(rows)!=0:
			self.employee_table.delete(*self.employee_table.get_children())
			for i in rows:
				self.employee_table.insert("",END,values=i)



	def get_cursor(self,event=""):
		cursor_row=self.employee_table.focus()
		content=self.employee_table.item(cursor_row)
		row=content["values"]
		self.name_var.set(row[1])
		self.dob_var.set(row[2])
		self.gender_var.set(row[3])
		self.dpmnt_var.set(row[4])
		self.phone_var.set(row[5])
		self.email_var.set(row[6])
		self.address_text.delete("1.0",END)
		self.address_text.insert(END,row[7])
		self.EmployeeID=row[0]


	def mark_attendance_In(self):
		mark=QRCode()
		ID=mark.scan()
		ID=ID[0]

		now = datetime.datetime.now()
		formatted_date=now.strftime('%Y-%m-%d')

		db=Database()
		repeat= db.mark_attendance_in(ID,formatted_date,now.strftime('%H:%M'),False)

		if(repeat is True):
			messagebox.showwarning("Warning","Enter Time already marked")
        
		else:
			messagebox.showinfo("Attendance Successfully Marked", "Employee No. %s at %s/%s/%s %s:%s"
                                        % (ID, now.day, now.month, now.year, now.hour, now.minute))

	def mark_attendance_Out(self):
		mark=QRCode()
		ID=mark.scan()
		ID=ID[0]

		now = datetime.datetime.now()

		db=Database()
		repeat= db.mark_attendance_out(ID,now.strftime('%H:%M'))

		if(repeat is True):
			messagebox.showwarning("Warning","Exit Time already marked")
		else:
			messagebox.showinfo("Attendance Successfully Marked", "Employee No. %s at %s/%s/%s %s:%s"
                                        % (ID, now.day, now.month, now.year, now.hour, now.minute))


	def generate_report(self):
		db=Database()
		db.generate_Report()

	def clear(self):
			self.name_var.set(""),
			self.dob_var.set(""),
			self.gender_var.set(""),
			self.dpmnt_var.set(""),
			self.phone_var.set(""),
			self.email_var.set(""),
			self.address_texts.delete("1.0",END)

root=Tk()
ob=Employee(root)
root.mainloop()