#-------------------------------------------------------------------------------
# Name:        Screen2Excel_v1
# Purpose:
#
# Author:      saurabhk
#
# Created:     19/09/2014
# Copyright:   (c) saurabhk 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""Module for importing key value pairs of BFTC screen from given or default
   location

   Usage: python Screen2Excel_v1 Folder_Adress(Opt)  Name_of_output_file(Opt)

   Dependencies : xlsxwriter module
"""


import os,xlsxwriter,sys


def main():
    path = r'D:\Bundles\bftcMessages' # Default Path if no value provided
    #path = r'D:\Bundles\test'

    Name = "Output_file_v2.xlsx" # Default Output file name if no value provided

    # calling function for creating Excel File
    screen2excel(path,Name)


def screen2excel(path,Name):
    """Export list of key value pairs drom all files available at given address

       Argv: path = Address of the folder which Have BFTC screen
             Name = Name of output file

       Functionality: Write Excel file having Screen Name, Key and value with
       provide Name
    """
    row=1
    column=0

    if(len(sys.argv)>2):
        Name = sys.argv[2]+'.xlsx'
        path = sys.argv[1]

    if(len(sys.argv)>1):
        path = sys.argv[1]

    # Creating New Excel file
    workbook = xlsxwriter.Workbook(Name)
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:D', 25)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Writing File Headers
    worksheet.write('A1', 'DisplayName', bold)
    worksheet.write('B1', 'DisplayName', bold)
    worksheet.write('C1', 'Key', bold)
    worksheet.write('D1', 'Value', bold)

    for dir_entry in os.listdir(path):
        dir_entry_path = os.path.join(path, dir_entry)
        if os.path.isfile(dir_entry_path):
            with open(dir_entry_path, 'r') as my_file:
                data_cs = my_file.readlines()
                full_data = "".join(data_cs)
                f_data = full_data.split("\n")

                #For extracting Display Name
                start = f_data[0].find("DisplayName")+12
                end = start + f_data[0][start:].find(" ")

                if(end-start != -1):
                    dispName = f_data[0][start:end]
                else:
                    dispName = f_data[0][start:]
                # Checking whther displayName is empty
                if(dispName==""):

                    # Some file name starts with - so remove it
                    if(dir_entry[0]=='-'):
                        dispName = str(dir_entry[1:])
                        dir_entry = dispName
                    else:
                        dispName = str(dir_entry)

                for i in range(1,len(f_data)):

                    kv = f_data[i].split("=")
                    if(len(kv)==2):
                        worksheet.write(row,column,dir_entry)
                        worksheet.write(row,column+1,dispName)
                        worksheet.write(row,column+2,kv[0])
                        worksheet.write(row,column+3,kv[1])
                        row = row+1

    workbook.close()


if __name__ == '__main__':
    main()
