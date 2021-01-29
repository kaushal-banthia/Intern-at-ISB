# importing libraries
import fnmatch
from pathlib import Path
import csv
import os
import fnmatch
# libraries imported

# Note: Need to convert the excel file to a csv file first. Can be done via online converters!

#list of files that have been downloaded
list_of_files = []
list_of_files_checked = []
prev_string1 = ""
prev_string2 = ""


# for accessing the full names of all the files. 
# Note that def14 files should be in a folder named as 'Files', which in turn should in the same folder as this program
for path,dirs,files in os.walk('.'):
    for file in files:

        # checks for all the files that have a .txt extension
        if fnmatch.fnmatch(file,'*.txt'):

            # gives the fullname of the .txt file
            fullname = os.path.join(path,file)

            # splits the file name into a list, with the delimiter as \
            list_of_fullname = fullname.split("\\")

            # concatenates file's id with its year of download
            list_of_fullname = list_of_fullname[2]

            # appends the name to the list of files that have been downlaoded
            list_of_files.append(list_of_fullname)
            list_of_files = list(dict.fromkeys(list_of_files))

# opening the input file, which is in the same folder as this program
with open("list.csv", "r") as file:
    reader = csv.reader(file, delimiter = ",")

    # opening the output file
    with open("S&P500 list of companies.csv", "w", newline = '') as filewriter:
        writer = csv.writer(filewriter)

        # writes the heading of the file
        writer.writerow(["GVKEY", "Company Name", "Ticker", "CIK", "Is the folder present?"])

        # Note: DELETE THE 2nd row that comes in the output file

        # iterating through the rows in the csv file
        for row in reader:
            string1 = row[2]
            string2 = row[3]

            if prev_string1 == string1 or prev_string2 == string2:
                continue

            if string1 in list_of_files:
                writer.writerow([row[0], row[1], row[2], row[3], "Yes"])
                list_of_files_checked.append(string1)
                prev_string1 = string1
                prev_string2 = string2
            elif string2 in list_of_files:
                writer.writerow([row[0], row[1], row[2], row[3], "Yes"])
                prev_string2 = string2
                prev_string1 = string1
            else:
                writer.writerow([row[0], row[1], row[2], row[3], "No"])
                prev_string2 = string2
                prev_string1 = string1