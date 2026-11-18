import os

FILENAME = "data.txt"

# 1. Load existing data from the text file at startup
def load_data():
    data = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    data.append({
                        "id": parts[0], 
                        "name": parts[1], 
                        "qty_or_grade": parts[2]
                    })
    return data

# 2. Save current data list into the text file for persistence
def save_data(data):
    with open(FILENAME, "w") as file:
        for item in data:
            file.write(f"{item['id']},{item['name']},{item['qty_or_grade']}\n")

# 3. Add a new record to the system
def add_record(data):
    r_id = input("Enter ID: ")
    name = input("Enter Name: ")
    val = input("Enter Quantity or Grade: ")
    
    data.append({
        "id": r_id, 
        "name": name, 
        "qty_or_grade": val
    })
    
    save_data(data)
    print("Record added successfully!")

# 4. Display all current records in a clean format
def view_records(data):
    if not data:
        print("No records found.")
        return
        
    print("\n--- Current Records ---")
    for item in data:
        print(f"ID: {item['id']} | Name: {item['name']} | Value: {item['qty_or_grade']}")
    print("-" * 23)

# 5. Delete a record based on its unique ID
def delete_record(data):
    r_id = input("Enter ID to delete: ")
    for item in data:
        if item['id'] == r_id:
            data.remove(item)
            save_data(data)
            print("Record deleted successfully!")
            return
    print("Record not found.")

# Main Application Execution Loop
if __name__ == "__main__":
    data = load_data()
    
    while True:
        print("\n=== Management System ===")
        print("1. View Records")
        print("2. Add Record")
        print("3. Delete Record")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_records(data)
        elif choice == '2':
            add_record(data)
        elif choice == '3':
            delete_record(data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
