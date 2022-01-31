import csv

# filename="annual-enterprise-survey-2020-financial-year-provisional-size-bands-csv.csv"

# fields=[]
# rows=[]

with open('annual-enterprise-survey-2020-financial-year-provisional-size-bands-csv.csv','r') as csvfile:
 csvreader=csv.reader(csvfile)
 fields=next(csvreader)
 for row in csvreader:
    row.append(row)
    print("Total number of rows=%d", csvreader.line_num)
