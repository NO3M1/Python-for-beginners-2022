#FUNCTIONS

def say_hello(name, age):
    print("hello! " + name)
    print("you are " + age + " years old")


print("start")
say_hello("joe", "33")#call the function
say_hello("noe", "30")
print("end")


#return statements

def add_two_numbers(num1, num2):
    return  num1 + num2
print(add_two_numbers(7, 5)) #or x = add_two_numbers(7,5) print(x)

#EX1 Create a function called showEmployee() such that it should accept an employee name and salary and print both of them out.
#Employee Sam salary is: 9000

def showEmployee(name, salary):
    print("Employee", name, "salary is:", salary)
showEmployee("sam",9000)


