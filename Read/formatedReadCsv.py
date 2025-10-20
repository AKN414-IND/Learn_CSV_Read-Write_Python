import csv

# The 'with' statement is a great way to open files. It makes sure the file
# is automatically closed when you're done, even if something goes wrong.
# We're opening 'data.csv' in 'r' (read) mode.
with open('../data.csv', mode='r') as file:
    # This creates a 'reader' object. Think of it like a pointer that starts
    # at the first line of the file and reads one row at a time.
    csv_reader = csv.reader(file)
    
    # We use 'next()' to read the very first row and move the pointer down.
    # Since the first row is the header, we'll store it in the 'header' variable.
    header = next(csv_reader)
    num_of_headers = len(header)

    # To make our table look nice, we need a top border. I chose a cell width of 20
    # characters plus 1 for the '|' border, so we print 21 underscores for each column.
    print("_" * 21 * num_of_headers)
    
    # Start the header line with a vertical bar.
    print(end="|")
    # Loop through each column name in our 'header' list.
    for item in header:
        # This is the trick for clean columns:
        # 1. Take the item (e.g., 'StudentID').
        # 2. Add the right number of spaces so the text + spaces = 20 characters.
        # 3. Use 'end="|"' to print a vertical bar instead of starting a new line.
        print(item + " " * (20 - len(item)), end="|")
    
    # After the loop prints all the headers, we need to move to the next line.
    print()
    # Print a separator line between the header and the data.
    print("_" * 21 * num_of_headers)
    
    # Now, we loop through the rest of the rows. The pointer for 'csv_reader' is already
    # at the first data row because we used 'next()' on the header.
    for row in csv_reader:
        # Start each data row with a vertical bar.
        print(end="|")
        # Loop through each piece of data (each cell) in the current row.
        for item in row:
            # We apply the exact same formatting logic to keep the columns aligned.
            print(item + " " * (20 - len(item)), end="|")
        # After printing all the items in the row, we jump to the next line.
        print()
        
    # Finally, print the bottom border to close the table.
    print("_" * 21 * num_of_headers)