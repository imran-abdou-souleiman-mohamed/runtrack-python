def calcule(num1,operator, num2):
    if operator == '+':
        print(num1+num2)
    elif operator == '-':
        print(num1-num2)
    elif operator == '*':
        print(num1*num2)
    elif operator == '/':
        print(num1/num2)
    elif operator =='%':
        print(num1%num2)
    return print

print(calcule(13,"+",5))
print(calcule(11,"-",4))
print(calcule(10,"*",6))
print(calcule(6,"/",7))
print(calcule(2,"%",8))