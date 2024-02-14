students = [
    {'name': 'Akihito Ryo', 'Namecode': 'Alpha', 'Role': 'Assist / Spy'},
    {'name': 'Akihito Hanabi', 'Namecode': 'Alice', 'Role': 'Assist / Plan Maker'},
    {'name': 'Akihito HIkari', 'Namecode': 'Beta', 'Role': 'Spy / Weapon Seller'},
]

def print_members():
    print("List Member of Hexagon Enterprise")
    for member in students:
        print("\nName", member["name"], "\nCode Name : ", member["Namecode"], "\nRole : ", member["Role"])

def add_new_member():
    print("\nMasukan member baru")
    new_name = input("\nMasukan Nama : ")
    new_code = input("\nMasukan Code Name : ")
    new_role = input("\nMasukan Role : ")

    new_member = {
        'name': new_name,
        'Namecode': new_code,
        'Role': new_role
    }

    students.append(new_member)

# Initial display
print_members()

while True:
    option = input("\nDo you want to add another member? (yes/not): ").lower()
    
    if option != 'yes':
        break

    add_new_member()
    print_members()

print("\nCode Name List:")
print_members()
