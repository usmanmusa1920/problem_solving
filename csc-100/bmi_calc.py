def bmi_calc():
    
    name = input('Enter your name: ')
    height_m = eval(input('Enter the height value: '))
    weight_kg = eval(input('Enter the weight value : '))

    bmi = weight_kg / (height_m ** 2)
    print(name, 'BMI is: ', bmi)
	
bmi_calc()
