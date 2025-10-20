# 1. Import the csv module
import csv

# 2. Prepare the data we want to write
header = ['EmployeeID', 'Name', 'Department']
data_rows = [
    [101, 'Alice', 'Engineering'],
    [102, 'Bob', 'Marketing'],
    [103, 'Charlie', 'Sales']
]

# 3. Open the file in write mode ('w')
#    REMEMBER: newline='' is essential to prevent extra blank rows.
with open('employees.csv', mode='w', newline='') as file:
    # 4. Create a writer object
    employee_writer = csv.writer(file)
    
    # 5. Write the header row to the file
    employee_writer.writerow(header)
    
    # 6. Write all the data rows to the file
    employee_writer.writerows(data_rows)

print("'employees.csv' has been created successfully!")