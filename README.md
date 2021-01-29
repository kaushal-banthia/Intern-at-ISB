# Intern at ISB
 Winter Intern at ISB

Created a program that found out clusters of keywords located in the DEF 14A files of S&P 500 companies.
Then compared the paragraphs (found via the clustering algorithm used) to a set of keywords that hinted the CEO's compensation being based on socio - economic factors.

Finally made a dataset that contained the name of each of the 5000+ files and the number of time the keywords appear in them.

This repository has the following files and folders:

Extra: Did as an extra work for helping out another teammate.
Files: This folder contains the DEF14A files for 3 companies. Due to space constraint, others could not be added here.
Output: Contains 2 files.
        Output.csv: Contains the final dataset created in .csv format.
        these_files_are_not_present.txt: Contains a list of those files that did not have the words "executive compensation" or         "executive remuneration" in them.

first_iteration.py: Contains the first version of the python code
second_iteration.py: Contains the second version of the python code with major updates and improvements
final_iteration.py: Contains the final and refined version of the python code that is being used for the research work.
