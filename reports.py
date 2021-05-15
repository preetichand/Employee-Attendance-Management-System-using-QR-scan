from datetime import datetime
import datetime
from datetime import date
import csv


class Reports:
    def __init__(self, source_data, report_file_name, headers):
        self.source_data = source_data
        self.headers = headers
        self.report_file_name = report_file_name

    def prepare_emp_report(self):
        with open(self.report_file_name, "w", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(self.headers)
            for i in self.source_data:
                csv_writer.writerow(i)
       
   