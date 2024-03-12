from Employees import Employees
from Employee_Exceptions import Employee_Exceptions

class Editing_Employees:
    def __init__(self, employees_data):
      self.employees = [Employees(row['First Name'], row['Last Name'], index, row['Date of Employment'], row['Salary'], row['Department']) for index, row in employees_data.iterrows()]




    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee added successfully.")
        print("Employee IDs in the list:", [employee.employee_id for employee in self.employees])
        print(employee)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def remove_employee(self, employee_id):
        employee_id = int(employee_id)  # Convert input to integer
        print("Trying to remove employee with ID:", employee_id)
        print("Employee IDs in the list:", [employee.employee_id 
                                            for employee in self.employees])
        for i, employee in enumerate(self.employees):
          if employee.employee_id == employee_id:
            del self.employees[i]
            print("Employee removed successfully.")
            return True
      
        raise Employee_Exceptions(employee_id)
        

      
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updating_employee(self, employee_id, updated_employee):
       try:
            for i, emp in enumerate(self.employees):
             if str(emp.employee_id) == employee_id:
                self.employees[i] = updated_employee
                return True
            raise Employee_Exceptions(employee_id)
       except Employee_Exceptions as e:
          print(e)
    
    


    
    def listing_employee(self):
        for employee in self.employees:
           print(employee)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~