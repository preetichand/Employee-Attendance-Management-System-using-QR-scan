import mysql.connector
import datetime;

class Database:
    

    def create_Db(self):    #Initialise the database 
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07")
         mycursor=mydb.cursor()
         mycursor.execute("create database if not exists Attendance")
         mycursor.execute("use Attendance")
         mycursor.execute("create table if not exists Employee(EmpId varchar(255) Primary key,Name varchar(255),dob varchar(50),gender varchar(10),dpmnt varchar(10),phone varchar(10),email varchar(30),address varchar(255))")
         mycursor.execute("create table if not exists Records(EmpId varchar(255) ,name varchar(255),dpmnt varchar(255),Date date,InTime varchar(255),status varchar(255),OutTime varchar(255))")
         mydb.commit()
         mydb.close()
         #db_exist=True


    def new_User(self,Empid,name,dob,gender,dpmnt,phone,email,address):   #Add employee's detail in database
        
        self.create_Db()
        
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Attendance")
        mycursor=mydb.cursor()
        query="insert into Employee values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(query,(Empid,name,dob,gender,dpmnt,phone,email,address))
        mydb.commit()
        mydb.close()

    def mark_attendance_in(self,id,date,Time,Exit):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Attendance")
        mycursor=mydb.cursor()
        mycursor.execute("Select EmpId from Records where EmpId=%s and Date =%s",(id,date))
        row=mycursor.fetchone()
        if(row is None):   
            query="select name,dpmnt from Employee where EmpId =%s"
            mycursor.execute(query,(id,))
            row=mycursor.fetchone()
            dept=row[1]
            name=row[0]
            value=None
            query="insert into Records values(%s,%s,%s,%s,%s,%s,%s)" 
            mycursor.execute(query,(id,name,dept,date,Time,"Present",value))
            mydb.commit()
            mydb.close()
        else:
            return True

    def mark_attendance_out(self,id,Time):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Attendance")
        mycursor=mydb.cursor()
        mycursor.execute("Select EmpId from Records where EmpId=%s and OutTime is Null",(id,))
        row=mycursor.fetchone()
        if(row is  None):
                return True
        mycursor.execute("update Records set OutTime=%s where EmpId=%s",(Time,id))
        mydb.commit()
        mydb.close()


    def fetch_all_data(self):
        self.create_Db()   
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Attendance")
        mycursor=mydb.cursor()
        mycursor.execute("select *from Employee")
        rows=mycursor.fetchall()
        mydb.commit()
        mydb.close()
        return rows

    def update(self,Empid,name,dob,gender,dpmnt,phone,email,address):
        self.create_Db()   
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Attendance")
        mycursor=mydb.cursor()
        mycursor.execute("UPDATE Employee SET name=%s,dob=%s,gender=%s,dpmnt=%s,phone=%s,email=%s,address=%s WHERE EmpId=%s",(name,dob,gender,dpmnt,phone,email,address,Empid))
        mydb.commit()
        mydb.close()

    def delete(self,Empid):  
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Attendance")
        mycursor=mydb.cursor()
        mycursor.execute("DELETE FROM Employee WHERE EmpId=%s",(Empid,))
        mydb.commit()
        mydb.close()

    def search(self,first,second):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="preeti_chand@07",database="Attendance")
        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM Employee WHERE "+first+" LIKE '"+second+"%'")
        rows=mycursor.fetchall()
        mydb.commit()
        mydb.close()
        return rows

    

        



# for testing only

#db = Database()
#db.new_User("Vadim","1986","male","idk","678","6","7","8")