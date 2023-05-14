#Write a program that takes three integers as input: low, high, and x. The program
#then outputs the number of multiples of x between low and high inclusive.
#Ex: If the input is:
#1
#10
#2
#The output is:
#5
#Hint: Use the % operator to determine if a number is a multiple of x. Use a for
#loop to test each number
#between low and high.

#My code was this but wasn't the output? Anyone Help me solve this?
#my Code will be below
low=int(input("Enter a low value number: "))
high=int(input("Enter a high value number: "))
x =int(input("Enter a number: "))

total = 0
for num in range(low, high):
  if num % x == 0:
    total += 1
    print(num)
