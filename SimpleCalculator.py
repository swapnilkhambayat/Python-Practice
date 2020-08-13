print('Simple Calculator!!')

firstnumber = input('First number?')

if firstnumber.isnumeric() == False:
    print('Please input a number.')
    exit()

operation = str(input('Operation?'))

if operation not in ('*','/','+','-','%','**'): 
    print('Operation not recognized.')
    exit()

Secondnumber = input('Second number?')

if Secondnumber.isnumeric() == False:
    print('Please input a number.')
    exit()
    
if operation == '*':
    print('product of ' + str(firstnumber) + operation + str(Secondnumber) + ' equals ' + str(int(firstnumber)*int(Secondnumber)))
if operation == '+':
    print('Sum of ' + str(firstnumber) + operation + str(Secondnumber) + ' equals ' + str(int(firstnumber)+int(Secondnumber)))
if operation == '-':
    print('Difference of ' + str(firstnumber) + operation + str(Secondnumber) + ' equals ' + str(int(firstnumber)-int(Secondnumber)))
if operation == '/':
    print('Quotient of ' + str(firstnumber) + operation + str(Secondnumber) + ' equals ' + str(int(firstnumber)/int(Secondnumber)))
if operation == '%':
    print('Modulus of ' + str(firstnumber) + operation + str(Secondnumber) + ' equals ' + str(int(firstnumber)%int(Secondnumber)))
if operation == '**':
    print('Exponent of ' + str(firstnumber) + operation + str(Secondnumber) + ' equals ' + str(int(firstnumber)**int(Secondnumber)))



 