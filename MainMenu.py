# my imports
import pandas as pd
from tabulate import tabulate
from Editing_Employees import Editing_Employees
from FileMethods import read_csv, write_csv
from Employees import Employees
from colorama import init, Fore, Style
#from Employee_Exceptions import Employee_Exceptions



init(autoreset=True)

def __int__(self):

    pass


def Menu():
    print(Fore.LIGHTMAGENTA_EX+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("          Welcome to The Employee Management System for JUMP! ")
    print(Fore.LIGHTMAGENTA_EX+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    ## Enter file diplay here :


    print(Fore.LIGHTYELLOW_EX+
        "                      WOULD YOU LIKE TO: \n")
    print("                          1: ADD NEW EMPLOYEES\n")
    print("                          2: UPDATE EMPLOYEE INFO\n")
    print("                          3: REMOVE EMPLOYEES\n")
    print("                          4: LIST EMPLOYEE INFO \n")
    print("                          5: EXIT\n")
    print(Fore.LIGHTMAGENTA_EX+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#____________________________________________________________________________


def main():
    
    
    #editing=Editing_Employees()
    employee_data = read_csv('Employee_Data - Sheet1.csv')
    editing = Editing_Employees(employee_data)

    while True:
        Menu()
        choice=input("Enter Your Choice: ") 
        if choice=='1':
            print("YOU ARE ADDING AN EMPLOYEE")
            employee_id = len(employee_data) + 1
        

            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            date_of_employment = input("Enter Date of Employment (YYYY-MM-DD): ")
            salary = input("Enter Salary: ")
            department = input("Enter Department: ")
            new_employee = Employees(first_name, last_name, employee_id, date_of_employment, salary, department)
            editing.add_employee(new_employee)
            employee_data = read_csv('Employee_Data - Sheet1.csv')  # Update employee_data after adding
            editing.listing_employee()
            


        elif choice=='2':
            print("YOU ARE UPDATING AN EMPLOYEE INFO")

            employee_id=input("Enter the Employee ID you would like to update: ")
            first_name=input("Enter New First Name: ")
            last_name =input("Enter New Last Name: ")
            date_of_employment =input("Enter New Date of Employment (YYYY-MM-DD): ")
            salary=input("Enter New Salary: ")
            department=input("Enter New Department: ")

            updated_employee=Employees( first_name, last_name, employee_id, date_of_employment, salary, department)

            editing.updating_employee(employee_id,updated_employee)
            employee_data = read_csv('Employee_Data - Sheet1.csv')  # Update employee_data after updating
           
            editing.listing_employee()

        elif choice=='3':
            print("YOU ARE REMOVING AN EMPLOYEE")
            employee_id = input("Enter an Employee ID you would like to remove: ")
            if editing.remove_employee(employee_id):
        # Update employee_data after successful removal
              employee_data = read_csv('Employee_Data - Sheet1.csv')
            else:
                print("Failed to remove employee.")
            editing.listing_employee()

        elif choice=='4':
            print("LIST OF EMPLOYEE INFO")
            editing.listing_employee()

        elif choice=='5':
            write_csv(employee_data,'Employee_Data - Sheet1.csv')
            print("GOODBYE!")
            break
        else:
            print(Fore.LIGHTRED_EX+"CHOOSE A NUMBER FROM 1 - 5")

if __name__ == "__main__":
    main()