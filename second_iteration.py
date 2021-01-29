# importing libraries
import fnmatch
from pathlib import Path
import csv
import os
import fnmatch
# libraries imported

# list of the keywords to look for the in the def14 files
list_of_words = ["responsib", "sustainab", "ethic", "stakeholder", "environment", "polluti", "social", "governance", "philanthrop", "charit", "law", "tax", "wage", "employee", "societ", "compliance", "code of conduct", "transparen", "safety", "diversity", "stakeholders", "corrupt", "strike", "sue", "illegal", "regulat", "government", "woman", "women", "black", "labor union", "labour union", "politic", "investor return", "investors return", "investors' return", "investor's return", "investor value", "investors value", "investor's value", "investors' value", "stockholder return", "stockbroker return", "stockholders return", "stockbrokers return", "stockholders' return", "stockbrokers' return", "stockholder's return", "stockbroker's return", "stockholder value", "stockbroker value", "stockholders value", "stockbrokers value", "stockholders' value", "stockbrokers' value", "stockholder's value", "stockbroker's value", "shareholder return", "shareholders return", "shareholders' return", "shareholder's return", "shareholder value", "shareholders value", "shareholders' value", "shareholder's value"]

# counter to indicate the number of files parsed
no_of_files_parsed = 0

# opening the output file
with open('Output/output.csv', 'w', newline = '') as filewriter:
    writer = csv.writer(filewriter)
    
    # writes the first row
    writer.writerow(["Filename", "Keyword", "Occurences"])

    # for accessing the full names of all the files. 
    # Note that def14 files should be in a folder named as 'Files', which in turn should in the same folder as this program
    for path,dirs,files in os.walk('.'):
        for file in files:
            
            # checks for all the files that have a .txt extension
            if fnmatch.fnmatch(file,'*.txt'):

                # gives the fullname of the .txt file
                fullname = os.path.join(path,file)

                # splits the file name into a list, with the delimiter as \
                fullnamelist = fullname.split("\\")

                # this dictionary stores the number of times each word appears in the .txt file
                word_appeared = {"responsib" : 0, "sustainab" : 0, "ethic" : 0, "stakeholder" : 0, "environment" : 0, "polluti" : 0, "social" : 0, "governance" : 0, "philanthrop" : 0, "charit" : 0, "law" : 0, "tax" : 0, "wage" : 0, "employee" : 0, "societ" : 0, "compliance" : 0, "code of conduct" : 0, "transparen" : 0, "safety" : 0, "diversity" : 0, "stakeholders" : 0, "corrupt" : 0, "strike" : 0, "sue" : 0, "illegal" : 0, "regulat" : 0, "government" : 0, "woman" : 0, "women" : 0, "black" : 0, "labor union" : 0, "labour union" : 0, "politic" : 0, "investor return" : 0, "investors return" : 0, "investors' return" : 0, "investor's return" : 0, "investor value" : 0, "investors value" : 0, "investor's value" : 0, "investors' value" : 0, "stockholder return" : 0, "stockbroker return" : 0, "stockholders return" : 0, "stockbrokers return" : 0, "stockholders' return" : 0, "stockbrokers' return" : 0, "stockholder's return" : 0, "stockbroker's return" : 0, "stockholder value" : 0, "stockbroker value" : 0, "stockholders value" : 0, "stockbrokers value" : 0, "stockholders' value" : 0, "stockbrokers' value" : 0, "stockholder's value" : 0, "stockbroker's value" : 0, "shareholder return" : 0, "shareholders return" : 0, "shareholders' return" : 0, "shareholder's return" : 0, "shareholder value" : 0, "shareholders value" : 0, "shareholders' value" : 0, "shareholder's value" : 0}
                count = 0
                occurences = []
                with open(fullname, "r") as file:
                    for line in file:
                        if "executive compensation" in line.lower() or "executive remuneration" in line.lower():
                            occurences.append(count)
                        count+=1
                
                for i in range(len(occurences)-1):
                    if occurences[i-1] - occurences[i] > 500:
                        occurences.remove(occurences[i])
                if len(occurences) == 0:
                    print("no meaningful word found")
                    continue

                # opening the input .txt file
                with open(fullname, 'r') as file:
                    lines = file.readlines()
                    word_appeared = {"responsib" : 0, "sustainab" : 0, "ethic" : 0, "stakeholder" : 0, "environment" : 0, "polluti" : 0, "social" : 0, "governance" : 0, "philanthrop" : 0, "charit" : 0, "law" : 0, "tax" : 0, "wage" : 0, "employee" : 0, "societ" : 0, "compliance" : 0, "code of conduct" : 0, "transparen" : 0, "safety" : 0, "diversity" : 0, "stakeholders" : 0, "corrupt" : 0, "strike" : 0, "sue" : 0, "illegal" : 0, "regulat" : 0, "government" : 0, "woman" : 0, "women" : 0, "black" : 0, "labor union" : 0, "labour union" : 0, "politic" : 0, "investor return" : 0, "investors return" : 0, "investors' return" : 0, "investor's return" : 0, "investor value" : 0, "investors value" : 0, "investor's value" : 0, "investors' value" : 0, "stockholder return" : 0, "stockbroker return" : 0, "stockholders return" : 0, "stockbrokers return" : 0, "stockholders' return" : 0, "stockbrokers' return" : 0, "stockholder's return" : 0, "stockbroker's return" : 0, "stockholder value" : 0, "stockbroker value" : 0, "stockholders value" : 0, "stockbrokers value" : 0, "stockholders' value" : 0, "stockbrokers' value" : 0, "stockholder's value" : 0, "stockbroker's value" : 0, "shareholder return" : 0, "shareholders return" : 0, "shareholders' return" : 0, "shareholder's return" : 0, "shareholder value" : 0, "shareholders value" : 0, "shareholders' value" : 0, "shareholder's value" : 0}
                    start = (occurences[0] - 500) if ((occurences[0] - 500) > 0) else occurences[0]
                    end = (occurences[-1] + 500) if ((occurences[-1] + 500) < count) else occurences[-1]

                    for i in range(start, end):
                        for word in list_of_words:
                            if word in lines[i]:
                                word_appeared[word] += 1
                            
                    for i in word_appeared.keys():
                        writer.writerow([fullnamelist[2]+'-'+fullnamelist[-1].split('-')[1], i, word_appeared[i]])
                # increments the number of files that have been completely read.
                no_of_files_parsed += 1

                # prints every 50th number, since printing every number will spam the screen
                # This is done to keep a tab on the progress made by the program, while it is running.
                if no_of_files_parsed % 50 == 0:
                    print(no_of_files_parsed)
