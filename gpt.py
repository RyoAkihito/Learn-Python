# List with pre-filled information
employee_list = [
    {'Name': 'John Doe', 'Name Code': 'JD001', 'Role': 'Software Engineer'},
    {'Name': 'Jane Smith', 'Name Code': 'JS002', 'Role': 'Data Scientist'},
    {'Name': 'Bob Johnson', 'Name Code': 'BJ003', 'Role': 'Product Manager'}
]

# Function to input additional employee details
def input_employee():
    name = input("Enter name: ")
    name_code = input("Enter name code: ")
    role = input("Enter role: ")
    
    # Creating a dictionary to store employee information
    employee_info = {
        'Name': name,
        'Name Code': name_code,
        'Role': role
    }
    
    # Appending the dictionary to the list
    employee_list.append(employee_info)

# Displaying the pre-filled list
print("Pre-filled Employee List:")
for employee in employee_list:
    print(f"Name: {employee['Name']}, Name Code: {employee['Name Code']}, Role: {employee['Role']}")

# Input additional data into the list
input_employee()

# Displaying the updated list
print("\nUpdated Employee List:")
for employee in employee_list:
    print(f"Name: {employee['Name']}, Name Code: {employee['Name Code']}, Role: {employee['Role']}")
