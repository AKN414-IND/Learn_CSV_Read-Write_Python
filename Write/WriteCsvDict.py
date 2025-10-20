# 1. Import the csv module
import csv

# 2. Prepare the data as a list of dictionaries
data_rows_dict = [
    {'EmployeeID': 101, 'Name': 'Alice', 'Department': 'Engineering'},
    {'EmployeeID': 102, 'Name': 'Bob', 'Department': 'Marketing'},
    {'EmployeeID': 103, 'Name': 'Charlie', 'Department': 'Sales'}
]

# 3. Define the column headers (fieldnames). This is required!
#    The order here dictates the column order in the CSV.
fieldnames = ['EmployeeID', 'Name', 'Department']

# 4. Open the file in write mode ('w') with newline=''
with open('employees_dict.csv', mode='w', newline='') as file:
    # 5. Create a DictWriter object
    #    You MUST provide the fieldnames.
    employee_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # 6. Write the header row to the file
    employee_writer.writeheader()
    
    # 7. Write the dictionary data to the file
    employee_writer.writerows(data_rows_dict)

print("'employees_dict.csv' has been created successfully!")