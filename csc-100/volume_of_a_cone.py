def cone():
  
  pi = float(3.142)

  ask_r = input('Input your radius type "float" or "int" : ')
  while ask_r != 'int' and ask_r != 'float':
    
    #if the input type of radius is not float or integer, but radius input is empty, this will run!
      if ask_r == '':
        ask_r = input('Radius field can not be empty, please input "float" or "int" : ')
        
      #if the input type of height is not float or integer, but something different, this will run!
      else:
        ask_r = input('"' + ask_r + '" can not be as radius type, input either "int" or "float" for radius value type: ')

  ask_h = input('Input your height type "float" or "int" : ')
  while ask_h != 'int' and ask_h != 'float':
    
    #if the input type of height is not float or integer, but height input is empty, this will run!
    if ask_h == '':
      ask_h = input('Height field can not be empty, please input "float" or "int" : ')
      
    #if the input type of height is not float or integer, but something different, this will run!
    else:
      ask_h = input('"' + ask_h + '" can not be as height type, input either "float" or "int" for height value type: ')

  rad = input('Radius number: ')
  
  #if the input type of radius is integer, but radius input is empty, this will run!
  if ask_r == 'int':
    while rad == '':
      rad = input('Radius number can not be empty, it must be in "int" ')

  #if the input type of radius is float, but radius input is empty, this will run!
  else:
    while rad == '':
      rad = input('Radius number can not be empty, it must be in "float" ')
    
  h = input('Height number: ')
  
  #if the input type of height is integer, but height input is empty, this will run!
  if ask_h == 'int':
    while h == '':
      h = input('Height number can not be empty, it must be "int" ')
  
  #if the input type of height is float, but height input is empty, this will run!
  else:
    while h == '':
      h = input('Height number can not be empty, it must be "float" ')
      
  #if the input of the radius and input of height is all float, it will run this!
  if ask_r == 'float':
    if ask_h == 'float':
      r = float(rad) ** 2
      b = 1 * pi * r * float(h)
      z = b/3
      print(z)
      
    #if the input of the radius and input of height is float and integer respectively, it will run this!
    else:
      r = float(rad) ** 2
      b = 1 * pi * r * int(h)
      z = b/3
      print(z)
      
  #if the input of the radius and input of height is integer and float respectively, it will run this!
  else:
    if ask_h == 'int':
      r = int(rad) ** 2
      b = 1 * pi * r * int(h)
      z = b/3
      print('Your result is >>>',z)
      
    #if the input of the radius and input of height is all integer, it will run this!
    else:
      r = int(rad) ** 2
      b = 1 * pi * r * float(h)
      z = b/3
      print('Your result is >>>',z)
      
cone()