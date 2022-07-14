def average(*args):
    l = 0
    for i in args:
        l = l + i
    n = l / len(args)
    print('The average number of ', args, 'is "' + str(int(n)) + '"')

average(1,2,3,4,5)

def time_to_second(min = input('Input minute: ')):
    mul = int(min) * 60
    print(str(min) + ' minutes in seconds is ' + str(mul) + ' seconds!')

time_to_second()

def ask(a = input('Put number ')):
    while int(a) <= 10:
        a = input(str(a) + ' is not allowed ')
    print('Ok,', str(a), 'is well now!')

ask(6)