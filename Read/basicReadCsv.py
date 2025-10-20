import csv

with open('data.csv', mode='r') as file:
    # Create a csv reader object
    csv_reader = csv.reader(file)
    
    # The reader object is an iterator. We can loop over it.
    for row in csv_reader:
        print(row)