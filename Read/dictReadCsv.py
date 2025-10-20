import csv

with open('../data.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    headers = csv_reader.fieldnames
    print(",".join(headers))
    
    for i, row in enumerate(csv_reader):

        for header in headers:
            value = row[header]
            print(value,end=",")
        print()