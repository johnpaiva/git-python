import os
import xlwt
from xlwt import Workbook
from pathlib import Path
import configparser

config = configparser.ConfigParser()
config.read_file(open(r"D:\Utilities\report_to_mviews_config.txt"))
rootdir = config.get('Config Section', 'rootdir')
dest_file  = config.get('Config Section', 'dest_file')

wb = Workbook()
reportdir = []
report_folders = []
rep_fldr_with_rep = []


paths = Path(rootdir).glob('**/*.rdl')
for path in paths:
    # because path is object not string
    path_in_str = str(path)
    # Do thing with the path
    for strings in path_in_str.split("\\") :
        reportdir.append(strings)
    rep_fldr_with_rep.append((path_in_str, reportdir[-2], reportdir[-1]))
    if reportdir[-2] not in report_folders :
        report_folders.append(reportdir[-2])

for folder in report_folders :
    
    i = k = l = 0
    j = 1
    
    # print (folder)
    if folder == 'MTM Reports' :
        pass
    else :
        rep_sheet = wb.add_sheet (folder)
        rep_sheet.col(0).width = 256 * 50
        rep_sheet.col(1).width = 256 * 50
        rep_sheet.col(2).width = 256 * 30
        rep_sheet.col(3).width = 256 * 30
        style = xlwt.easyxf('font: bold 1')
        rep_sheet.write(0, 0, 'Report Name', style)
        rep_sheet.write(0, 1, 'Model View Name', style)
        rep_sheet.write(0, 2, 'Procedure Name', style)
        rep_sheet.write(0, 3, 'Function Name', style)
        for rep_file_path, rep_folder, report in rep_fldr_with_rep :
            if folder == rep_folder :
                i = j + 1
                rep_sheet.write(i, 0, report[:-4])
                with open(rep_file_path, 'r') as f_src:
                    lines = []
                    procs = []
                    funcs = []        
                    for line in f_src:
                        if ('V_MODEL' in line) or ('v_model' in line) :
                            for words in line.split() :
                                if ('V_MODEL' in words) or ('v_model' in words) :
                                    if words.upper() not in lines:
                                        lines.append(words.upper())
                        if ('>P_' in line ) or ('>p_' in line) :               
                            for words in line.split('<') :
                                if ('>P_' in words ) or ('>p_' in words) :
                                    for proc in words.split('>') :
                                        if ('P_' in proc) or ('p_' in proc) :
                                            if proc.upper() not in procs:
                                                procs.append(proc.upper())
                        if ('FN_RPT' in line) or ('fn_rpt' in line) :
                            # print(line)
                            for words in line.split('(') :
                                if ('FN_RPT' in words) or ('fn_rpt' in words) :
                                    for func in words.split('.') :
                                        if ('FN_RPT' in func) or ('fn_rpt' in func) :
                                            for func1 in func.split() :
                                                if ('FN_RPT' in func1) or ('fn_rpt' in func1) :
                                                    if func1.upper() not in funcs:
                                                        funcs.append(func1.upper())     

                j = i
                for views in lines :
                    rep_sheet.write(j, 1, views)
                    j += 1
                k = i
                for proc in procs :
                    rep_sheet.write(k, 2, proc)
                    k += 1
                l = i
                for func in funcs :
                    rep_sheet.write(l, 3, func)
                    l += 1                

wb.save(dest_file)


