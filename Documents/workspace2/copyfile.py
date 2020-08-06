#File name : copyfile.py
#Author's name : Seol Cheon
#Student Number : 301113120
#file description : This script will copy the contents of one file into another file

source=input("enter the source filename with extension: ")
destination=input("enter the destination filename with extension: ")
source=open(source,"r")
destination=open(destination,"w+")
content=source.read()
destination.write(content)
