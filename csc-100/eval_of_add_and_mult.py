#  A program in python that will receive two input from user and perform addition and multiplication, the output should be in positive integer value, regardless of whatever value the user entered.

num1 = eval(input('Enter a first number: '))
num2 = eval(input('Enter a second number: '))

add = num1 + num2
mult = num1 * num2

print('The addition of the numbers is: ', abs(add))
print('The multiplication of the numbers is: ', abs(mult))