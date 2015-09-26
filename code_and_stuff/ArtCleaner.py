import csv

#Open our input and output files
csvfile = open('./data/cleanme.csv', 'r')
#outfile = open('./data/cleaned.csv', 'w')

#Now a DictReader and DictWriter
reader = csv.DictReader(csvfile)
#writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

#write headers
#writer.writeheader()

#Clean and write the data to output
for row in reader:
    for field in row:
        print type(field)
        print field
#USE dir and find methods or attributes
    #print type(row)
    #if type(row) == str:
        #print row = row.upper()
    #row['first_name'] = row['first_name'].upper()
    #row['city'] = row['city'].replace("&nbsp;", " ")
    #row['zip'] = row['zip'].zfill(5)
    #if the row is a string the row should be uppercased
    #row['amount'] = int(row['amount'])
    #if row == type(str)
        #row.upper()
    #if row['amount'] <= 1000:
        #print row['amount']
        #writer.writerow(row)