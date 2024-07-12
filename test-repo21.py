# fibonacci in python
# fibonacci using if, else, statement and for loop
number = int(input("Enter any number: "))
first, second = 0, 1
next = 0

print("The Fibonacci series")
# number is less than equal to zero
if number <= 0:
    print("Please enter number greater than zero")
else:
    for i in range(0,number):
        print(next, end=" ")
        first = second
        second = next
        next = first + second