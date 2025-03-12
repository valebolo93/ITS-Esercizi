'''Write a program to create a function show_employee() using the following conditions.

    It should accept the employee’s name and salary and display both.
    If the salary is missing in the function call then assign default value 9000 to salary'''

def show_employees(name:str, salary:int=9000) -> None:
    return f"Employees's name: {name},the salary is: {salary}"

print(show_employees("Valentina"))
print(show_employees("Valentina",10000))