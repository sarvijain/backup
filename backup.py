import os
import shutil

source= input("Enter the folder name which you want to backup : ")
destination=input("Enter the folder name where you want to backup : ")

source= source+"/"
destination= destination+"/"

list_of_files = os.listdir(source)
# print(list_of_files)

for file in list_of_files:
    shutil.copy((source+file),destination)