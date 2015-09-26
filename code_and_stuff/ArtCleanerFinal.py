import csv

#Open our input and output files
csvfile = open('./data/cleanme.csv', 'r')
outfile = open('./data/cleaned_final.csv', 'w')

#Now a DictReader and DictWriter
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

#write headers
writer.writeheader()

#Clean and write the data to output
for row in reader:
    row['first_name'] = row['first_name'].upper()
    row['city'] = row['city'].replace("&nbsp;", " ")
    row['zip'] = row['zip'].zfill(5)
    row['amount'] = int(row['amount'])
    if row['amount'] >= 1000:
        writer.writerow(row)