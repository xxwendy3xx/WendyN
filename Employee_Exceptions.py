# my exceptions handeling
class Employee_Exceptions(Exception):
    def __init__(self, employee_id):
        self.employee_id = employee_id
        super().__init__(f"Employee with ID {employee_id} not found.")
    