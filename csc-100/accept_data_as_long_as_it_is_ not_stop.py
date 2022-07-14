def func(data = input('Enter a data: ')):
   
   while data != 'stop':
     
     print(data, 'is not accepted!')
     data = input('Enter a data: ')
     
   print('Yes now you input', data)
   
   #  The above function will keep on asking you to enter a data as long as you don't enter the word 'stop' and it is case sensitive, if you enter 'Stop' with capital letter or any of the word alphabet letter e.g 's', 't', 'o', or 'p' it will keep on asking you, but if you enter all letters in small letter then it will print "Yes now you input stop"
func()