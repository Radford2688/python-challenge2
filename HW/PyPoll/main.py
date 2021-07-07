import os
import csv
csvpath = os.path.join ('Resources', 'budget_data.csv')
with open (csvpath) as csvfile:
    csv_reader = csv.reader (csv_file, delimiter =',')
    print(csv_reader)    
csv_reader = csv.DictReader(open('Resources/budget_data.csv'))    
print(csv_reader)

