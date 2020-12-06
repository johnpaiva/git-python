import shutil
import glob
import subprocess
from review_comments_report_chk import review_comm_chk
from datetime import date


processed_file_folder = r"D:\Utilities\Previous_Code_Review_Reports"
log_file_name = r"D:\Utilities\code_review_comments_report_check_log.txt"
file_name = '-'

file_object  = open(log_file_name, "a+")
file_object.write("\n\n Process Run Date : {}\n".format(date.today()))
file_object.close()

for file_name in glob.glob(r"C:\Users\jjacob\Downloads\Comment_info_zeomega_JIVA_DB_AND_REPORTS*.xls") :
    review_comm_chk (file_name, log_file_name)
    shutil.move(file_name, processed_file_folder)


if file_name == '-' :
    file_object  = open(log_file_name, "a+")
    file_object.write("\n File not found")
    file_object.close()

subprocess.call(['notepad.exe', r"D:\Utilities\code_review_comments_report_check_log.txt"])