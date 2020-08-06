#HEADER COMMENT
"""
File name : copyfile.py
Author's name : Seol Cheon
Student Number : 301113120
file description : This script will copy the contents of one file into another file
"""


#prompt the user to enter the source file name
source=input("enter the source filename with extension: ")

#prompt the user to enter the destination file name 
destination=input("enter the destination filename with extension: ")

#open source file in read mode
source=open(source,"r")

#open destination file in write mode
destination=open(destination,"w+")

#read the content of source file and assign that as a content
content=source.read()

#write content to destination file
destination.write(content)
