x = 5; y = 10

print('The value of x is {} \nThe value of y is {} ' .format(x,y))

# The {} in the above print statement are placeholder of 'x' and 'y' respectively since the index number is not include, but if an index number is include in the curly brace, the order of variable in the .format(x,y) doesn't matter E.g

print()

print('The value of x is {1} \nThe value of y is {0} ' .format(y,x))
