from datetime import datetime
import calendar
import pandas as pd
from  QReader import qrGenerate 
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from check_data import *
from repository import Database
from reports import Reports
import matplotlib.pyplot as plt
#**********************************************************************************************************


class MainUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Attendance system - main screen")
        self.master.geometry("800x400+50+50")
        self.IDenter = StringVar()
        self.password = StringVar()

        self.label1 = Label(master, text="Employee attendance", font=("Arial", 16, "bold"), fg="RoyalBlue4") \
            .grid(row=0, column=0, sticky=W, pady=10)
        self.date = Label(master, text= date.today(), font=("Arial", 12, "bold"), fg="RoyalBlue4") \
            .grid(row=0, column=3, sticky=W, pady=10)
        self.clock = Label(master, text=time.strftime('%H:%M'), font=("Arial", 12, "bold"), fg="RoyalBlue4") \
            .grid(row=0, column=4, sticky=W, pady=10)
        self.label2 = Label(master, text="Take Attendance",
                            fg="RoyalBlue4").grid(row=1, column=0, columnspan=4, sticky=W, pady=10)
        
        self.BotEnt = Button(master, text="Enter working", bg="DarkOliveGreen1", width="20",
                             command=lambda: self.add_attendance_log("Enter")) \
            .grid(row=3, column=1)
        self.BotEx = Button(master, text="Exit working", bg="SkyBlue1", width="20",
                            command=lambda: self.add_attendance_log2("Exit")) \
            .grid(row=3, column=2)
        self.Admin_enter = Label(master, text="For admin functions please enter password:", fg="gray") \
            .grid(row=8, column=0, pady=80)
        self.entry1 = Entry(self.master, width="20", textvariable=self.password) \
            .grid(row=8, column=1, pady=80, padx=10)
        self.button1 = Button(master, text="Enter admin. functions", width="20", bg="gray", fg="white",
                              command=self.check_password).grid(row=8, column=2, pady=80, padx=10)
        self.exlabel = Button(master, text="Exit", command=self.exit, width=10).grid(row=9, column=4, pady=10)

    def check_password(self):
        password = self.password.get()
        if password == "":
            tkinter.messagebox.showerror("Error", "Please type password")
            return
        if password == "1234":
            self.open_mng_screen()
            self.password.set("")
        else:
            tkinter.messagebox.showerror("password Error", "The password is wrong, please type again")

    def open_mng_screen(self):
        rootAddManualy = Toplevel(self.master)
        MngScreen(rootAddManualy)

    def add_attendance_log(self, inout):
       
        ID=""
        q=qrGenerate()
        ID=ID.join(q.scan())

        now = datetime.now()

        formatted_date = now.strftime('%Y-%m-%d')

        repo=Database()
        repeat= repo.mark_Attendance(ID,formatted_date,time.strftime('%H:%M'),False)

        if(repeat is True):
             tkinter.messagebox.showinfo("Warning","Enter Time already marked")
        
        else:
      
             tkinter.messagebox.showinfo("Login successful", "Emp No. %s %s at %s/%s/%s %s:%s"
                                        % (ID, inout, now.day, now.month, now.year, now.hour, now.minute))

        
    def add_attendance_log2(self, out):
       
            ID=""
            q=qrGenerate()
            ID=ID.join(q.scan())

            now = datetime.datetime.now()

            formatted_date = now.strftime('%Y-%m-%d')

            repo=Database()
            repeat=repo.mark_Attendance(ID,formatted_date,time.strftime('%H:%M'),True)
        
            if(repeat is True):
             tkinter.messagebox.showinfo("Warning"," Exit Time already marked")
        
            else:
      
             tkinter.messagebox.showinfo("Login successful", "Emp No. %s %s at %s/%s/%s %s:%s"
                                        % (ID, out, now.day, now.month, now.year, now.hour, now.minute))
        
       

    def exit(self):
        qexit = tkinter.messagebox.askyesno("Exit", "Do you want to exit the System?")
        if qexit > 0:
            root.destroy()


# ****************************************************************************************************************

class MngScreen(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Management screen")
        self.master.geometry("900x300+100+100")

        self.add_manual = Button(master, width=30, text="Add Employee manually", command=self.open_add_screen,
                                 bg="SkyBlue1") \
            .grid(row=0, column=0, pady=10)
       
        self.del_manual = Button(master, width=30, text="Delete Employee", command=self.open_del_screen, bg="coral1") \
            .grid(row=0, column=1, pady=10, padx=40)
       
        self.report_by_emp = Button(master, width=34, text="Attendance Report",
                                    command=self.employees_report, bg="Ivory3") \
            .grid(row=0, column=2, pady=10, padx=40)
        self.report_by_emp = Button(master, width=34, text="Attendance report by employee",
                                    command=self.attendance_report_by_emp, bg="Ivory3") \
            .grid(row=1, column=2, pady=10, padx=40)
       
        self.back = Button(master, text="Back", command=lambda: self.closeScreen(master)) \
            .grid(row=4, column=4, pady=10)

    def open_add_screen(self):
        rootAddManualy = Toplevel(self.master)
        AddManuallyUI(rootAddManualy)

   

    def open_del_screen(self):
        rootAddManualy = Toplevel(self.master)
        DelManuallyUI(rootAddManualy)

   
    def employees_report(self):
        repo=Database()
        rows=repo.view_complete_Report()

        report = Reports(rows , "report_employees.csv",
                         ["Employee ID", "Name", "Department", "Date", "InTime", "Status", "OutTime"])
        report.prepare_emp_report()
        tkinter.messagebox.showinfo("report ready",
                                                   "The report is ready, please open the \"report_employees.csv\" file")

    def attendance_report_by_emp(self):
        rootAddManualy = Toplevel(self.master)
        AttendanceReportByEmp(rootAddManualy)

  
    def closeScreen(self, w):
        w.destroy()

#*****************************************************************************************


class AddManuallyUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Add employee")
        self.master.geometry("700x400+150+150")

       

       
        self.name = StringVar()
        self.department = StringVar()
        self.bloodgp = StringVar()
        self.DOJ = StringVar()
        self.email = StringVar()
        self.number = StringVar()
        self.designation = StringVar()    
         

        self.label11 = Label(self.master, text="Name :").grid(row=0, column=0, sticky=E, pady=5)
        self.entry11 = Entry(self.master, textvariable=self.name).grid(row=0, column=1, pady=5)
        self.label12 = Label(self.master, text="Department:").grid(row=1, column=0, sticky=E, pady=5)
        self.entry12 = Entry(self.master, textvariable=self.department).grid(row=1, column=1, pady=5)
        self.label13 = Label(self.master, text="Blood Group:").grid(row=2, column=0, sticky=E, pady=5)
        self.entry13 = Entry(self.master, textvariable=self.bloodgp).grid(row=2, column=1, pady=5)
        self.label14 = Label(self.master, text="DOJ  ").grid(row=3, column=0, sticky=E, pady=5)
        self.entry14 = Entry(self.master, textvariable=self.DOJ).grid(row=3, column=1, pady=5)
        self.label15 = Label(self.master, text="Email :").grid(row=3, column=3, sticky=E, pady=5)
        self.entry15 = Entry(self.master, textvariable=self.email).grid(row=3, column=4, pady=5)
        self.label16 = Label(self.master, text="Phone number (digits only):").grid(row=4, column=0, sticky=E, pady=5)
        self.entry16 = Entry(self.master, textvariable=self.number).grid(row=4, column=1, pady=5)
        self.label17 = Label(self.master, text="Designation :").grid(row=4, column=3, sticky=E, pady=5)
        self.entry17 = Entry(self.master, textvariable=self.designation).grid(row=4, column=4, pady=5)
     
        self.back = Button(self.master, text="Back", command=lambda: self.closeScreen(master)) \
            .grid(row=10, column=6, pady=10)
        self.add_button = Button(self.master, text="Add Employee to the list", bg="green", fg="white", width="40",
                                 command=self.get_data).grid(row=7, column=1, columnspan=3, pady=5)

    def get_data(self):
        
        q=qrGenerate()
        self.ID=q.generate()
        ID=self.ID
        name = self.name.get()
        department = self.department.get()
        bloodgp = self.bloodgp.get()
        DOJ = self.DOJ.get()
        email =self.email.get()
        number = self.number.get()
        designation =self.designation.get()
        emp_data = [ID, name, department,bloodgp, DOJ, email, number, designation]
        
        obj=Check_emp_data()

        for i in emp_data:
            if obj.check_empty(i) is False:
                tkinter.messagebox.showerror("Error", "There is one or more missing values")
                return

        if obj.check_number(number) is False:
            tkinter.messagebox.showerror("Error", "The Phone number should have 6-12 digits only , please try again")
            return

        repo=Database()
        repo.new_User(ID,name,email,designation,number,DOJ,bloodgp,department)
    
        more_or_close = tkinter.messagebox.askyesno("Employee added",
                                                    "The employee added to the Database. Do you wand to add another employee?")
        self.master.destroy() if more_or_close == 0 else self.clean_screen()
               



    def clean_screen (self):
        self.name.set("")
        self.department.set("")
        self.bloodgp.set("")
        self.DOJ.set("")
        self.email.set("")
        self.number.set("")
        self.designation.set("")
    

    def closeScreen(self, w):
        w.destroy()
# ********************************************************************************************************************
          
#****************************************************************************************************************


class DelManuallyUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Remove employee")
        self.master.geometry("700x100+200+200")

        self.ID_to_del = StringVar()
 
        self.label1 = Label(self.master, width=20, text="Emp ID to remove:").grid(row=0, column=0, sticky=E, pady=5)
        self.entry1 = Entry(self.master, width=30, textvariable=self.ID_to_del).grid(row=0, column=1, pady=5)
        self.back = Button(self.master, text="Back", command=lambda: self.closeScreen(master)) \
            .grid(row=10, column=6, pady=10, padx=10)
        self.del_button = Button(self.master, width=20, text="Remove Employee", bg="red", command=self.del_emp) \
            .grid(row=0, column=2, pady=5, padx=10)

    def del_emp(self):
        ID = self.ID_to_del.get()
        obj=Check_emp_data()
        repo=Database()
        if obj.check_id_in_list(ID,repo) is False:
            tkinter.messagebox.showerror("Error", "The employee is not in the list")
            self.ID_to_del.set("")
            return

        
        repo.del_employee(ID)
        more_or_close = tkinter.messagebox.askyesno("Employee removed",
                                                    "Employee No %s removed from the list."
                                                    "Do you want to remove another employee?" % ID)
        self.master.destroy() if more_or_close == 0 else self.ID_to_del.set("")

    def closeScreen(self, w):
        w.destroy()

# ********************************************************************************************************************

#*****************************************************************************************************************


class AttendanceReportByEmp(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Attendance report by employee")
        self.master.geometry("700x300+200+200")

        self.ID = StringVar()
        self.from_month = StringVar()
        self.from_year = StringVar()
        self.until_month = StringVar()
        self.until_year = StringVar()
        self.from_date = StringVar()
        self.to_date = StringVar()

        self.label11 = Label(self.master, text="Emp ID (6 digits):").grid(row=0, column=0, sticky=E, pady=5)
        self.entry12 = Entry(self.master, textvariable=self.ID).grid(row=0, column=1, pady=5)
        self.label13 = Label(self.master, text="From").grid(row=1, column=0, sticky=E, pady=5)
        self.label14 = Label(self.master, text="Month:").grid(row=1, column=1, sticky=E, pady=5)
        self.entry15 = Entry(self.master, textvariable=self.from_month).grid(row=1, column=2, pady=5)
        self.label16 = Label(self.master, text="Year:").grid(row=1, column=3, sticky=E, pady=5)
        self.entry17 = Entry(self.master, textvariable=self.from_year).grid(row=1, column=4, pady=5)
        self.label18 = Label(self.master, text="Date:").grid(row=1, column=5, sticky=E, pady=5)
        self.entry19 = Entry(self.master, textvariable=self.from_date).grid(row=1, column=6, pady=5)
        self.label20 = Label(self.master, text="Until").grid(row=2, column=0, sticky=E, pady=5)
        self.label21 = Label(self.master, text="Month:").grid(row=2, column=1, sticky=E, pady=5)
        self.entry22 = Entry(self.master, textvariable=self.until_month).grid(row=2, column=2, pady=5)
        self.label23 = Label(self.master, text="Year:").grid(row=2, column=3, sticky=E, pady=5)
        self.entry24 = Entry(self.master, textvariable=self.until_year).grid(row=2, column=4, pady=5)
        self.label25 = Label(self.master, text="Date:").grid(row=2, column=5, sticky=E, pady=5)
        self.entry26 = Entry(self.master, textvariable=self.to_date).grid(row=2, column=6, pady=5)

        self.report_by_emp = Button(master, width=30, text="Make attendance report",
                                    command=self.make_report, bg="Ivory3").grid(row=4, column=2,  columnspan = 3, pady=20)

        self.back = Button(master, text="Back", command=lambda: self.closeScreen(master)) \
            .grid(row=4, column=6, pady=10)

    def make_report(self):
        ID = self.ID.get()
        from_month = self.from_month.get()
        from_year = self.from_year.get()
        until_month = self.until_month.get()
        until_year = self.until_year.get()
        from_date = self.from_date.get()
        to_date = self.to_date.get()

        if ID=="" or from_month == "" or from_year == "" or until_month == "" or until_year == "":
            tkinter.messagebox.showerror("Missing data", "please make sure you fill all the parameters")
            return
        if from_month.isalpha() or from_year.isalpha() or until_year.isalpha() or until_month.isalpha() :
            tkinter.messagebox.showerror("Error", "The parameters should be digits only, please check again")
            return
       
        if 1 > int(from_month) > 12 or 1 > int(until_month) > 12:
            tkinter.messagebox.showerror("Error", "Month should be between 1-12")
            return
        if int(from_year) < 2021:
            tkinter.messagebox.showerror("Error", "From year should take no long than 5 years")
            return
        if int(until_year) < int(from_year):
            tkinter.messagebox.showerror("Error", "From year should be  earlier or same as until year")
            return
       
        fromDate=pd.to_datetime(from_year+from_month+from_date,format='%Y%m%d').strftime('%Y-%m-%d')
        toDate=pd.to_datetime(until_year+until_month+to_date,format='%Y%m%d').strftime('%Y-%m-%d')
       
        repo=Database()
        obj=Check_emp_data()

        if obj.check_id_in_list(ID,repo) is True:   
            rows=repo.get_report_employee(ID)
            
            self.label11 = Label(self.master, text="Name :").grid(row=7, column=0, sticky=E,pady=5)
            self.label12 = Label(self.master, text=rows[1]).grid(row=7, column=1, sticky=E,pady=5)
            self.label13 = Label(self.master, text="Department :").grid(row=7, column=2, sticky=E,pady=5)
            self.label14 = Label(self.master, text=rows[7]).grid(row=7, column=3, sticky=E,pady=5)
            self.label15 = Label(self.master, text="Email :").grid(row=7, column=4, sticky=E,pady=5)
            self.label16 = Label(self.master, text=rows[3],fg='blue').grid(row=7, column=5, sticky=E,pady=5)
            self.label17 = Label(self.master, text="Blood Group :").grid(row=8, column=0, sticky=E,pady=5)
            self.label18 = Label(self.master, text=rows[6]).grid(row=8, column=1, sticky=E,pady=5 )
            self.label19 = Label(self.master, text="Designation :").grid(row=8, column=2, sticky=E)
            self.label20 = Label(self.master, text=rows[2]).grid(row=8, column=3, sticky=E,pady=5)
            self.label21 = Label(self.master, text="Contact :").grid(row=8, column=4, sticky=E,pady=5)
            self.label22 = Label(self.master, text=rows[4],fg='blue').grid(row=8, column=5, sticky=E,pady=5)
            self.label23 = Label(self.master).grid(row=9, column=0, sticky=E,pady=5)

        emp_fields = ["Emloyee ID","Name","Department","Date", "InTime","Status","OutTime"]
    
        rows=repo.view_Report(ID,fromDate,toDate)
        if(len(rows)==0):
             tkinter.messagebox.showinfo("warning",
                                                   "No record Found")
             return
        else:  
            for val in range(len(emp_fields)):
                self.label30 = Label(self.master, text=emp_fields[val],fg='green').grid(row=14, column=val)
            i=15
            for data in rows: 
                for j in range(len(data)):
                    e = Entry(self.master, width=13, fg='navy blue') 
                    e.grid(row=i, column=j) 
                    e.insert(END, data[j])
                i=i+1
        
    def closeScreen(self, w):
        w.destroy()


# *******************************************************************************************************************
if __name__ == "__main__":
    root = Tk()
    sys = MainUI(root)
    root.mainloop()
