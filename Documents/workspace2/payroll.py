
"""
File name : payroll.py
Author's name : Seol Cheon
Student Number : 301113120
file description : This script will reads the data.txt file and outputs
the wages paid to each employee in tabular format to the console
"""


fileName = input("Enter file name : ")
'''prompt user to answer displaying texts in input function '''

dataFile = open(fileName,"r")
'''open file that user input in console in readmode '''

records = dataFile.readlines()
'''read the lines in dataFile and assign it as records'''

print("Employ Number |    Employee Name    | Hours Worked ")
'''print these table headers'''

print("---------------------------------------------")
'''print this line'''

for record in records:
    employInfo = record.split(",")
    '''split record by comma and assign those elements in employInfo array'''
    empNumber = employInfo[0]
    empName = employInfo[1]+" "+employInfo[2]
    hourWorked = employInfo[3]
    
    print("%13s | %19s | %8s " %(empNumber,empName,hourWorked))
    '''print data'''
