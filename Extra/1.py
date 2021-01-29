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

            # completes the year, since only the last 2 digits were mentioned in the file name
            year = list_of_fullname[-1][-13:-11]
            if int(year) > 21:
                year = "19" + year
            else:
                year = "20" + year

            # concatenates file's id with its year of download
            list_of_fullname = list_of_fullname[2] + '+' + year

            # appends the name to the list of files that have been downlaoded
            list_of_files.append(list_of_fullname)

# opening the input file, which is in the same folder as this program
with open("list.csv", "r") as file:
    reader = csv.reader(file, delimiter = ",")

    # opening the output file
    with open("S&P500 list of companies.csv", "w", newline = '') as filewriter:
        writer = csv.writer(filewriter)

        # writes the heading of the file
        writer.writerow(["GVKEY", "Company Name", "Ticker", "CIK", "Year", "DEF 14A Downloaded?"])

        # Note: DELETE THE 2nd row that comes in the output file

        # iterating through the rows in the csv file
        for row in reader:

            # concatenating the Ticker with the year for an easier search
            string1 = row[2] + '+' + row[4]

            # concatenating the CIK with the year for an easier search
            string2 = row[3] + '+' + row[4]

            # if either of string1 or string2 is present in the list of downloaded files, print yes in the output csv file
            if string1 in list_of_files or string2 in list_of_files:
                writer.writerow([row[0], row[1], row[2], row[3], row[4], "Yes"])

            # if both string1 and string2 are not present in the list of downloaded files, print no in the output csv file
            else:
                writer.writerow([row[0], row[1], row[2], row[3], row[4], "No"])