#Getter and setters EMPLOYEE
#Getter and setters EMPLOYEE


class Employees:
    def __init__(self, first_name, last_name, employee_id, date_of_employment, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.date_of_employment = date_of_employment
        self.salary = salary
        self.department = department

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Date of Employment: {self.date_of_employment}, Salary: {self.salary}, Department: {self.department}"
    # Getter and setter methods
    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_employee_id(self):
        return self.employee_id
    
    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_date_of_employment(self):
        return self.date_of_employment
    
    def set_date_of_employment(self, date_of_employment):
        self.date_of_employment = date_of_employment

    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary):
        self.salary = salary

    def get_department(self):
        return self.department
    
    def set_department(self, department):
        self.department = department