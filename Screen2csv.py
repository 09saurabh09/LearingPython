#-------------------------------------------------------------------------------
# Name:        Screen2csv
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

   Usage: python Screen2csv Folder_Adress(Opt)  Name_of_output_file(Opt)

   Dependencies : Null
"""


import os,csv,sys


def main():
    path = r'D:\Bundles\bftcMessages' # Default Path if no value provided
    #path = r'D:\Bundles\test'

    Name = "Output_file.csv" # Default Output file name if no value provided

    # calling function for creating Excel File
    screen2csv(path,Name)


def screen2csv(path,Name):
    """Export list of key value pairs drom all files available at given address

       Argv: path = Address of the folder which Have BFTC screen
             Name = Name of output file

       Functionality: Write CSV file having Screen Name, Key and value with
       provide Name
    """
    #Checking Python version to avoid extra new line while writing
    if(sys.version_info.major<3):
        f = csv.writer(open(Name, "wb")) # csv file for storing data
    else:
        f = csv.writer(open(Name, "w",newline='')) # csv file for storing data

    # Writing Header for file
    f.writerow(["File Name".upper(),"Display Name".upper(), "Key".upper(), "Value".upper()])

    # If both arguments are given
    if(len(sys.argv)>2):
        Name = sys.argv[2]+'.csv'
        path = sys.argv[1]

    # If only path is given, default name will be used
    if(len(sys.argv)>1):
        path = sys.argv[1]

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
                        f.writerow([dir_entry,dispName, kv[0], kv[1]])


if __name__ == '__main__':
    main()
