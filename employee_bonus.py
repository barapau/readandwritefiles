import csv

infile = open("EmployeePay.csv", 'r', newline ='')
reader = csv.reader(infile)

for row in reader:
    print(format(row[0],'4'),format(row[1], '15'), format(row[2], '15'), format(row[3], '10'), format(row[4], '10'))
 