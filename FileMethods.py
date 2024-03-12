import pandas as pd

# make two methods one to read n the other to write


#read
def read_csv(filePath):
    data = pd.read_csv(filePath, index_col='Employee ID')
    data.columns = data.columns.str.strip()
    pd.set_option('display.max_colwidth', None)
    print(data.to_string(index=True, header=True))
    return data

#write
def write_csv(data, filePath):
    data.to_csv(filePath,index=False)

file_path = 'Employee_Data - Sheet1.csv'
employee_data = read_csv(file_path)
employee_ids = employee_data.index
print("Employee IDs:", employee_ids)

#file_path2= 'Department_Sheet.csv'
#epartment_data= read_csv(file_path2)
#type_of_departments= department_data.index
#print("Departments: " ,type_of_departments)