import os
import fnmatch

file_path = r"D:\Utilities"
file_name = r"Appeal Decision Summary Report by Service Type.xml"
dest_file = r"report_to_views.txt"
# def write_to_file (file_name,views) :


with open(os.path.join(file_path,file_name), 'r') as f_src:
    lines = []        
    for line in f_src:
        if 'V_MODEL' in line :
            for words in line.split() :
                if 'V_MODEL' in words :
                    if words not in lines:
                        lines.append(words)

    with open(os.path.join(file_path,dest_file), 'a+') as df:
        print (file_name[:-4], file = df, end='\n')
        print ("=" * 80, file = df, end='\n')
        for words in lines :
            print (words, file = df, end ='\n')
