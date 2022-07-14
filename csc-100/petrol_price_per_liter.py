def petrol(ltr = input('Enter how many liter? ')):
    per_ltr = float(69.5)
    for i in range(1, int(ltr)):
        p = per_ltr * i
        print('The price of ' + str(i) + ' liter of petrol is $' + str(p) + ' kb')

petrol()
