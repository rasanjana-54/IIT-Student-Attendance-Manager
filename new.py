
import datetime

# Data storage for students and attendance records
students = {}
attendance_records = {}

# Function to display the main menu (Figure 1)
def main_menu():
    print("IIT Campus")
    print("Main Menu")
    print("1) Enroll a new student")
    print("2) View details of a student")
    print("3) View details of all the students according to the branch")
    print("4) Update student details")
    print("5) Mark attendance")
    print("6) View attendance")
    print("7) Exit")
    return input("Your Choice: ")

# Function to enroll a new student (Figure 2)
def enroll_student():
    print("IIT Campus - Enroll a new student.")
    while True:
        student_id = input("Student ID (9-digit) - ")
        if len(student_id) != 9:
            print("id must be exactly 9 digits.")
        else:
            break
    while True:
          nic = input("NIC (12 characters) - ")
          if len(nic) != 12:
              print("NIC must be exactly 12 characters.")
          else:
              break
    first_name = input("First Name (max 10 chars) - ")
    last_name = input("Last Name (max 15 chars) - ")
    birth_date = input("Birth Date (YYYY-MM-DD) - ")
    address = input("Permanent Address (max 15 characters) - ")
    while True:
          phone_number = input("Phone Number (10 digits) - ")
          if len(phone_number) != 10:
             print("Phone number must be exactly 10 digits.")
          else:
              break
    tutorial_group = input("Tutorial Group - ")
    centre = input("Centre - ")

    students[student_id] = {
        "NIC": nic,
        "First Name": first_name,
        "Last Name": last_name,
        "Birth Date": birth_date,
        "Address": address,
        "Phone Number": phone_number,
        "Tutorial Group": tutorial_group,
        "Centre": centre
    }
    print("Student enrolled successfully.")

# Function to view details of a student (Figure 3)

def view_student_details():
    student_id = input("Enter Student ID - ").strip()  
    if student_id in students:
        student = students[student_id]
        print("Student Details:")
        print(f"NIC: {student.get('NIC', 'N/A')}")
        print(f"Phone Number: {student.get('Phone Number', 'N/A')}")
        print(f"First Name: {student.get('First Name', 'N/A')}")
        print(f"Last Name: {student.get('Last Name', 'N/A')}")
        print(f"Birth Date: {student.get('Birth Date', 'N/A')}")
        print(f"Address: {student.get('Address', 'N/A')}")
        print(f"Tutorial Group: {student.get('Tutorial Group', 'N/A')}")
        print(f"Centre: {student.get('Centre', 'N/A')}")
    else:
        print("Student not found.")
# Funtion to Update student details (Figure 4)
def view_all_students():
   
    print("IIT Campus")
    print("View details of all the students.\n")
    centre_name = input("Centre: ")

    
    print(f"Centre: {centre_name}\n")
    print("NIC           Student ID    First Name    Last Name    Tutorial Group")

    found = False
    for student_id, details in students.items():
        if details['Centre'].lower() == centre_name.lower():
            print(f"{details['NIC']:<13} {student_id:<13} {details['First Name']:<12} {details['Last Name']:<12} {details['Tutorial Group']}")
            found = True

    if not found:
        print("No students found for the specified centre.")

    update = input("\nDo you want to update the details (Yes/No)? ")
    if update.lower() == "yes":
        update_student_details()

    

# Function to update a student’s details (Figure 5)
def update_student_details():
    student_id = input("Enter Student ID to update - ")
    if student_id in students:
        print("Enter new details (leave blank to keep current value):")
        
        # Update NIC
        while True:
              nic = input("NIC (12 characters) - ")
              if nic and len(nic) != 12:
                 print("NIC must be exactly 12 characters.")
              else:
                  break
        students[student_id]['NIC'] = nic or students[student_id]['NIC']
        
        # Update First Name
        first_name = input("First Name (max 10 chars) - ")
        if first_name and len(first_name) > 10:
            print("First Name must not exceed 10 characters.")
            return
        students[student_id]['First Name'] = first_name or students[student_id]['First Name']
        
        # Update Last Name
        last_name = input("Last Name (max 15 chars) - ")
        if last_name and len(last_name) > 15:
            print("Last Name must not exceed 15 characters.")
            return
        students[student_id]['Last Name'] = last_name or students[student_id]['Last Name']
        
        # Update Address
        address = input("Permanent Address (max 15 chars) - ")
        if address and len(address) > 15:
            print("Address must not exceed 15 characters.")
            return
        students[student_id]['Address'] = address or students[student_id]['Address']
        
        # Update Phone Number
        while True:
              phone_number = input("Phone Number (10 digits) - ")
              if phone_number and len(phone_number) != 10:
                  print("Phone number must be exactly 10 digits.")
              else:
                  break
        students[student_id]['Phone Number'] = phone_number or students[student_id]['Phone Number']
        
        # Update Tutorial Group
        tutorial_group = input("Tutorial Group - ")
        students[student_id]['Tutorial Group'] = tutorial_group or students[student_id]['Tutorial Group']
        
        # Update Centre
        centre = input("Centre - ")
        students[student_id]['Centre'] = centre or students[student_id]['Centre']
        
        print("Details updated successfully.")
    else:
        print("Student not found.")

# Function to mark attendance (Figure 6)
def mark_attendance():
    centre = input("Centre - ")
    tutorial_group = input("Tutorial Group - ")
    date = input("Date (YYYY-MM-DD) - ")
    for student_id in students:
        status = input(f"Student ID {student_id} Present/Absent - ")
        if student_id not in attendance_records:
            attendance_records[student_id] = []
        attendance_records[student_id].append({
            "Date": date,
            "Status": status
        })
    print("Attendance marked successfully.")

# Function to view attendance of a student (Figure 7)
def view_attendance():
    student_id = input("Enter Student ID - ")
    from_date = input("From (YYYY-MM-DD) - ")
    to_date = input("To (YYYY-MM-DD) - ")
    # Filter attendance based on date range and display
    if student_id in attendance_records:
        print("Date - Present/Absent")
        for record in attendance_records[student_id]:
            date = datetime.datetime.strptime(record['Date'], "%Y-%m-%d")
            if from_date <= record['Date'] <= to_date:
                print(f"{record['Date']} - {record['Status']}")
    else:
        print("No attendance records found.")

# Main function
def main():
    while True:
        choice = main_menu()
        if choice == "1":
            enroll_student()
        elif choice == "2":
            view_student_details()
        elif choice == "3":
            view_all_students()
        elif choice == "4":
            update_student_details()
        elif choice == "5":
            mark_attendance()             
        elif choice == "6":
            view_attendance()
        elif choice == "7":
       
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
