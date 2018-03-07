dia = int(input())
km  = int(input())

resul = float((dia * 90))
if(km > (dia *100)):
    resul += ((km-(100*dia))*12)

print("{}0".format(resul))