import csv

CUSTFILE = "customers.csv"
CUSTCOUNTRY = "customer_country"

infile = open(CUSTFILE, 'r', newline ='')
outfile = open(CUSTCOUNTRY, 'w', newline='')

reader = csv.reader(infile)
writer = csv.writer(outfile, delimiter = ',')

for row in reader:
    first_name = row[1]
    last_name = row[2]
    country = row[3]
    writer.writerow((first_name, last_name, country))
  
infile.close()
outfile.close()

