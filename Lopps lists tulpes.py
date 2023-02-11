i = 1
while i <= 5:
   print(i)
   i = i + 1
print("done with loop")

#ex1 build a guessing game that gives the user 3 tries to guess a number between 1 and 10

secret_number = 5
guess = 0
tries = 0

while tries < 3 and guess != secret_number:
    guess = int(input("guess the number between 1 and 10 : "))
    tries = tries + 1
if guess == secret_number:
   print("you won")
else:
   print("you lost")


#LISTS
fruits = ["apple" , "mango" , "banana", "pear"]
print(fruits[0]) #prints the first element of the list, not the first character
fruits[0] = "kiwi"  #changes the element
print(len(fruits)) #4
(fruits[1;3]) #prints all te elements one and 3
fruits.append("blueberry") #adding elements to the llist
fruits.clear()
fruits.count("apple") #1
fruits.index("apple") #gives the index of the element from the list
fruits.insert(1,"banana") #insert to the index one
fruits.pop(3) #deletes the element on the index 3
fruits.remove("banana")
fruits.reverse()
fruits.sort()



numbers = [1,2,3,4,5]
print(numbers)

booleans = [True, False]
print(booleans)

mixed_list = [True, 1, "apple"]
print(mixed_list)


#LOOPS

fruits = ["apple" , "mango", "banana", "pear"]
name = "mike"
for item in fruits:
    print(item)  #printing out all the items

for i in name:
    print(i)

for i in range(6):#prints 0 1 2 3 4 5
    print(i)

for i in range(3,7): # prins from 3 to 6 (not including 7)
        print(i)

grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(grid[0][1]) #2

#ex1 Write a program that inputs a number n and prints the sum of all of the numbers from 1 to n:

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("The sum of all the numbers from 1 to", n, "is", sum)

#ex2 Write a for loop that prints out the following multiples of 2:
2 4 6 8 10 12 14 16 18 20.

for i in range(2, 22, 2):\
    print(i)

# ex3 Write a while loop that prints out the following multiples of 2:2 4 6 8 10 12 14 16 18 20

i = 2
while i <= 20:
    print(i)
    i = i + 2

#ex4 Write a program that creates a list with the following integers: 3, 5, 9, 3, 2, 9, 10.
# The program should iterate through the values in the list and print out each of the integers on separate lines.
numbers = [3, 5, 9, 3, 2, 9, 10]
for num in numbers:
    print(num)

#ex5 Write a program that creates a tuple with the following strings: "one", "two", "three", "four", "five".
# The program should print out the length of each string in the tuple on different lines.

strings = ("one", "two", "three", "four", "five")
for string in strings:
    print(len(string))


