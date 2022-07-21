# Working with variables

# print() function to print the text in console
print("Hello World!")
print('print("What is your message")')
print("Hello World! \nHello World! \nHello World!")

# ICE - Printing
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


# String Manipulation
print("Hello" + " " + "Afsheen")

# String Concatenation
# String should be enclosed within double or single quotes
print("5" + "3")
print("Hello " + "Afsheen")

# ICE - Debugging
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# input() function - to take the input from user
input("What is your name? ")
print("Hello " + input("What is your name? "))

# len() function - to count the number of characters
print(len(input("What is your name? ")))

# ICE - Input function
print(len(input("What is your name? ")))


# variable - can be changed or varied
name = input("What is your name? ")
name = "Jack"
print(name)

# ICE - Variable (Swapping the values)
a = input("a: ")
b = input("b: ")

# swapping logic
c = a
a = b
b = c

print(a)
print(b)