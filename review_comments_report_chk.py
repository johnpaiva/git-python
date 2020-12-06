def review_comm_chk(file_name, log_file_name) :
    import xlrd

    wb = xlrd.open_workbook(file_name) 
    sheet = wb.sheet_by_index(0) 
    ctr = sheet.nrows


    i = 1
    status_val = 0
    merged_by_val = 0
    no_comment_val = 0
    rows = []

    for x in range(sheet.ncols) :
        if sheet.cell_value(0,x) in ("Status") :
            status_val = x
        elif sheet.cell_value(0,x) in ("closed_by/merged_by") :
            merged_by_val = x
        elif sheet.cell_value(0,x) in ("No_of_manual_comments") :
            no_comment_val = x


    while i < ctr :
        if (sheet.cell_value(i, no_comment_val)) == 0 and (sheet.cell_value(i, status_val)) in ("merged") :
             rows.append("Row # " + str(i+1) + " | " +  "Merged by : " + (sheet.cell_value(i, merged_by_val)))
        i += 1

    file_object  = open(log_file_name, "a+")
    
    file_object.write("\n\n Processed File Name : {}".format(file_name))

    if rows != [] :
        file_object.write("\n\n Missed Code Review Comments Info :")
        file_object.write("\n {} ".format(rows))
    else : 
        file_object.write("\n\n No Missed Code Review Comment Cases Identified")   
    file_object.close()
