dia = int(input())
km  = int(input())

resul = float((dia * 30) + (km*0.01))

resul = resul - (resul * (10/100))
print("{0:.2f}".format(resul))