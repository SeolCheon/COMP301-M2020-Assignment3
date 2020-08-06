#HEADER COMMENT
"""
File name : payroll.py
Author's name : Seol Cheon
Student Number : 301113120
file description : This script will reads the data.txt file and outputs
the wages paid to each employee in tabular format to the console
"""

fileName = input("Enter file name : ")
dataFile = open(fileName,"r")


records = dataFile.readlines()
print("Employ Number |    Employee Name    | Hours Worked ")
print("---------------------------------------------")
for record in records:
    empDetail = record.split(",")
    empNumber = empDetail[0]
    empName = empDetail[1]+" "+empDetail[2]
    hourWorked = empDetail[3]
    
    print("%13s | %19s | %8s " %(empNumber,empName,hourWorked))
