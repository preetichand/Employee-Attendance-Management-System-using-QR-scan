import mysql.connector
import datetime;

class Database:
    

    def create_Db(self):    #Initialise the database 
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07")
         mycursor=mydb.cursor()
         mycursor.execute("create database if not exists Project")
         mycursor.execute("use Project")
         mycursor.execute("create table if not exists Employee(EmpId varchar(255) Primary key,Name varchar(255),Designation varchar(255),Email varchar(255),Contact varchar(10),DOJ varchar(255),Bloodgp varchar(10),Dep varchar(255) )")
         mycursor.execute("create table if not exists Report(EmpId varchar(255) ,Name varchar(255),Dept varchar(255),Date date,InTime varchar(255),status varchar(255),OutTime varchar(255))")
         mydb.commit()
         mydb.close()
         db_exist=True


    def new_User(self,id,name,email,desig_tn,contact,doj,bloodgp,dep):   #Add employee's detail in database
        
        self.create_Db()
        
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Project")
        mycursor=mydb.cursor()
        query="insert into Employee values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(query,(id,name,desig_tn,email,contact,doj,bloodgp,dep))
        mydb.commit()
        mydb.close()

    
    def mark_Attendance(self,id,date,Time,Exit):       # Mark the attendance of employee
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Project")
         mycursor=mydb.cursor()
         if Exit==True:
            mycursor.execute("update report set OutTime=%s where EmpId=%s",(Time,id))
            mydb.commit()
            mydb.close()

         else:
            query="select Name,Dep from Employee where EmpId =%s"
            mycursor.execute(query,(id,))
            row=mycursor.fetchone()
            dept=row[1]
            name=row[0]
            value=None
            query="insert into Report values(%s,%s,%s,%s,%s,%s,%s)" 
            mycursor.execute(query,(id,name,dept,date,Time,"Present",value))
            mydb.commit()
            mydb.close()


    def view_Report(self,id,fromDate,ToDate):             #view Attendance report of the dates lying in particular range
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Project")
        mycursor=mydb.cursor()
        query="select * from Report where Date >= %s and Date <= %s and EmpId=%s"
        mycursor.execute(query,(fromDate,ToDate,id))
        rows=mycursor.fetchall()
        mydb.close()
        return rows

    def view_complete_Report(self):             
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Project")
        mycursor=mydb.cursor()
        query="select * from Report order by Date"
        mycursor.execute(query)
        rows=mycursor.fetchall()
        mydb.close()
        return rows

    def get_stats(self,EmpId,fromDate,toDate):           #get the statistics of the attendance of any employee
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Project")
        mycursor=mydb.cursor()
        mycursor.execute("select count(EmpId)from Report where EmpId=%s and Date >= %s and Date <= %s",(EmpId,fromDate,toDate))
        row=mycursor.fetchone()
        mydb.close()
        totalPresent=row[0]
        toDate=datetime.datetime.strptime(toDate, '%Y-%m-%d')
        fromDate=datetime.datetime.strptime(fromDate, '%Y-%m-%d')

        totalDays=(toDate-fromDate).days
        totalAbsent=totalDays-totalPresent

        List= [totalPresent,totalDays,totalAbsent]
        return List

    def get_report_employee(self,EmpId):    #get details  of the employee whose attendance statistics has to be displayed
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Project")
        mycursor=mydb.cursor()
        mycursor.execute("select * from Employee where EmpId=%s",(EmpId,))
        row=mycursor.fetchone()
        mydb.close()
        return row

    def del_employee(self,id):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Project")
        mycursor=mydb.cursor()
        mycursor.execute(" delete from Employee where EmpId=%s",(id,))
        mydb.commit()
        mydb.close()
    
    def check_ID_in_db(self,id):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Project")
        mycursor=mydb.cursor()
        mycursor.execute(" select name from Employee where EmpId=%s",(id,))
        row=mycursor.fetchone()
        mydb.close()
        if(row==None):
         return False
        else:
         return True

        
        


    
    # def update_employee_details(self,EmpId,name,desig_tn,email,contact,doj,bloodgp,dep):    #update details of an employee
    #     mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Project")
    #     mycursor=mydb.cursor()
    #     mycursor.execute("update Employee set Name=%s,Designation=%s,Email=%s,Contact=%s,DOJ=%s,Bloodgp=%s,Dep=%s where EmpId=%s",(name,desig_tn,email,contact,doj,bloodgp,dep,EmpId))
    #     mydb.commit()
    #     mydb.close()   

    # def search_employee(self,EmpId):    #search employee using the EmpId
    #     mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Project")
    #     mycursor=mydb.cursor()
    #     mycursor.execute("select * from Employee where EmpId=%s",EmpId)
    #     row=mycursor.fetchone()
    #     mydb.close()
    #     return row

    




    
  


        