'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
def code():
  times = int(input("How many times do you want to print hunter?: "))
  i = 0
  while i < times:
    print("Hunter")
    i += 1