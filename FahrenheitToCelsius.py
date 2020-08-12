fahrenheit_val = input('What is the temperature in fahrenheit?')
if fahrenheit_val.isnumeric() == False:
    print('Input is not number.')
    exit()
print('Temperature in celsius is',int((int(fahrenheit_val)-32)*5/9))