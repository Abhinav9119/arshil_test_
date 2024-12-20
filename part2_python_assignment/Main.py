from EmployeeDatabase import EmployeeDatabase


db = EmployeeDatabase("localhost", "root", "ABHINAV", "arshil_test")

flag=1

while flag!=0:
    
    try:
        choice = int(input("enter a choice:\n1) Add employee\n2) update salary\n3) delete employee\n4) display all records \n5)exit: \nChoice: "))

        match (choice):
            case 1:
                db.add_employee(input("enter first name: "),input("enter last name: "),input("enter email: "),input("enter department: "),input("enter joining date (YYYY-MM-DD): "),float(input("enter salary: ")))
            case 2:
                db.update_salary(int(input("enter employee_id: ")),float(input("enter new salary: ")))
            case 3:
                db.delete_employee(int(input("enter employee_id: ")))
            case 4:
                db.display_employees()
            case 5:
                print("exiting program: ")
            case _:
                print("invalid choice.")
    except Exception as e:
        print(f" error occurred: {e}")
    