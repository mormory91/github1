num1=input('insert first number: ')
fnc=input('insert function: ')
num2=input('insert second number: ')
if fnc == '+':
    rslt=float(num1)+float(num2)
    print(rslt)
elif fnc == '-':
    rslt=float(num1)-float(num2)
    print(rslt)
elif fnc == '*':
    rslt=float(num1)*float(num2)
    print(rslt)
elif fnc == '/':
    rslt=float(num1)/float(num2)
    print(rslt)
elif fnc == '**':
    rslt=float(num1)**float(num2)
    print(rslt)
else:
    print('error')
