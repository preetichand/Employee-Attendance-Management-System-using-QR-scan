import re
import datetime

from datetime import date
from datetime import timedelta
import time


class Check_emp_data:

    def check_empty(self,variable):
        return False if variable == "" else True

    def check_id_in_list(self,ID,repo):
        
        return repo.check_ID_in_db(ID)


    def check_number(self,number):
         if re.match(r"\d{10}", str(number)) is None: 
             return False 
         else:
              return True



