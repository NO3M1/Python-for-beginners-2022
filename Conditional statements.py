
#CONDITIONAL STATEMENTS
#if the weather is good ->go to the beach
#othervise if the weather is bad ->stay at home and do homework
#otherwise -go on a walk

good_weather = True
bad_weather = False

if good_weather:
    print("go to the beach")
elif bad_weather:
    print("stay at home")
    print("do homeworks")
else:
    print("go on a walk")

#LOGICAL OPERATORS
#if hungry and thirsty : eat and drink something

is_hungry = True
is_thirsty = True

if is_hungry and is_thirsty:  #and opeartor  so in my case will be executed if this 2 are true
    print(("eat and drink something"))

#if hungry or thirsty
if is_hungry or is_thirsty:  #true + false
    print("eat or drink something")

#if thirst not hungry
is_hungry = False
is_thirsty = True

if is_thirsty and not is_hungry:
    print("drink something but do not eat")


#COMPARISON OPERATORS
#1.write a program that determines if a number is positive, negative or 0

num = 4
if num >0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("0")

#2. write a program that determines if a person is an adult (18over) or a minor

age = 18
if age >= 18:
    print("adult")
else:
    print("minor")

#3 write a program that prints out "great job" if a person`s grade in a course is an A

grade = "A"

if grade == "A":
    #checks if it is equal ==
    # != not equal to
    print("great job")

#4 A student fails the course if their attendance is less than 75%
#inputs: number of classes, number of classes attended
#print out: the students attendance and if they failed the course

total = int(input("how many classes were held"))
attended =int(input("how many classes dod you attend"))

attendance = round(attended/total , 2)
print("attendance: " + str(attendance))

if attendance < 0.75:
    print(("failed the course"))
else:
    print("passed")

#round the decimals


#5 Write a Python program that inputs three integers and calculates and prints out their sum.
#However, if the three numbers are all equal then print out three times their sum.

first_int = int(input("first integer"))
second_int = int(input("second integer"))
third_int = int(input("third integer"))

total = first_int + second_int + third_int
print("the total is " + str(total))

if first_int == second_int == third_int:
    print(total*3)


