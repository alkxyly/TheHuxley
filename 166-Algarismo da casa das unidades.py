numero = int(input())

if(numero < 0):
    numero =  numero * (-1)
    print((numero%10) * (-1))
else:
    print(numero%10)