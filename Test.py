print ("Hello World")
print (3)
print (4)
print ("***")

num_of_apples = 3
print(num_of_apples)
print(type(num_of_apples)) #printing out the typo of the variable

#converting between data types
float_number = 4.56
int_number = 3
print((int(float_number)))   #4
print((float(int_number)))  #3.0

# string concatenation
first_name = "Jenny"
last_name = "Noemi"
#or message = first_name + " " + last_name + "!"
#print(message)
print (first_name + " " + last_name + "!")

age = 30
print("my age is" + " " + str(age))

#indexes
message = "hello world"
print(message[6])  #w
print(message[0])  #h
print(message[-1])  #d

#lenght
print(len(message))  #11
print(message.find("h")) #=0
#-1 input means that the letter s in our case is not in the string

#replace
print(message.replace("hello" , "bye"))

print(message.capitalize())

#working with numbers
print(2+3*7/2)
print(round(4.56))
print(round(4.56825 , 3))  #round 3 decimal
print(abs(-4)) #4
print(pow(2,4)) #16 2 a 4iken


#input function
name = input("what is your name?")  #will print this to the user
age = input("what is your age?")
print ("hi" + name + "!")
print ("hi " + name + "!" + " you are " + age + " years old")


#EX1Write a Python program that inputs two integers and prints out the sum of the integers.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)

#EX2Write a Python program that inputs a user's first and last name and prints them in reverse order with a space in between.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)


#EX3 A farmer has three species:
# Chickens = 2 legs
# Cows = 4 legs
# Pigs = 4 legs
#Write a Python program that takes in the number of chickens, cows, and pigs (respectively) a farmer has. Print out the sum of the legs across all animals.

chickens = int(input("Enter the number of chickens: "))
cows = int(input("Enter the number of cows: "))
pigs = int(input("Enter the number of pigs: "))
total_legs = chickens * 2 + cows * 4 + pigs * 4
print("The total number of legs is", total_legs)

print(4 + 3 * 4 / 2 + 1)



