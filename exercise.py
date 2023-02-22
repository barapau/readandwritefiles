#Read the file – EmployeePay.csv using the CSV module in Python. Using the data in this file, 
# print out details for each employee along with total pay which should include their bonus (has to be calculated). 
#The program should also pause after each employee until the user hits a key
import csv

infile = open('EmployeePay.csv', 'r')
reader = csv.reader(infile)
fields = next(reader)

for row in reader:
    customer_id = row[0]
    name = row[1]
    last_name = row[2]
    salary = int(row[3])
    bonus = float(row[4])
    total = format(1 +(salary * bonus), '.2f')
    print(customer_id, name, last_name, total)
    input()

    


