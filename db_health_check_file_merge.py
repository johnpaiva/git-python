import os
import shutil
import glob
from datetime import date
import subprocess

path = r"D:\Utilities\Previous_DB_Health_Audit_Reports"
file_dest_object = "Audit_results_" + format(date.today()) + ".txt"

file_name1 = file_name2 = file_name3 = ''
line1 = line2 = line3 = ''

for file_name in glob.glob(r"C:\Users\jjacob\Downloads\audit_result_*.txt") :
    if '61' in file_name :
        file_name1 = file_name
        file_source_object1 = open(file_name, 'r')
    if '63' in file_name :
        file_name2 = file_name
        file_source_object2 = open(file_name, 'r')
    if '64' in file_name :
        file_name3 = file_name
        file_source_object3 = open(file_name, 'r')
   
with open(os.path.join(path,file_dest_object ), 'a+') as fp: 
    print ("Description" + ' ' * 104 + "Label", file = fp)
    print ("=" * 121, file = fp)
    while True:
        if os.path.exists(file_name1) :
            line1 = file_source_object1.readline()
            clean_line1 = line1.replace('\00','')
            if 'Count' in clean_line1 and 'Label' not in clean_line1 :
                fp.write("\n")    
                fp.write(clean_line1)
        if os.path.exists(file_name2) :
            line2 = file_source_object2.readline()
            clean_line2 = line2.replace('\00','')
            if 'Count' in clean_line2 and 'Label' not in clean_line2:
                fp.write(clean_line2)
        if os.path.exists(file_name3) :
            line3 = file_source_object3.readline()
            clean_line3 = line3.replace('\00','')
            if 'Count' in clean_line3 and 'Label' not in clean_line3:
                fp.write(clean_line3)

        if not line1:
            if not line2:
                if not line3:   
                    break

if os.path.exists(file_name1) :
    file_source_object1.close() 
if os.path.exists(file_name2) :
    file_source_object2.close()
if os.path.exists(file_name3) :
    file_source_object3.close() 

for file_name in glob.glob(r"C:\Users\jjacob\Downloads\audit_result_*.txt") :
    old_name = file_name[26:]
    new_name = file_name[26:-4] + "_" + format(date.today()) + ".txt"
    shutil.move(file_name, path)
    os.rename(os.path.join(path, old_name), os.path.join(path, new_name))

subprocess.call(['notepad.exe', os.path.join(path,file_dest_object)])