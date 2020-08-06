
"""
File name : copyfile.py
Author's name : Seol Cheon
Student Number : 301113120
file description : This script will copy the contents of one file into another file
"""


'''prompt the user to enter the source file name'''
source=input("enter the source filename : ")

'''prompt the user to enter the destination file name''' 
destination=input("enter the destination filename : ")

'''open source file in read mode'''
source=open(source,"r")

'''open destination file in write mode'''
destination=open(destination,"w+")

'''read the content of source file and assign that as a content'''
texts=source.read()

'''write content to destination file'''
destination.write(texts)
