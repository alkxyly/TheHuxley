n1 = input()

lista =  list(map(int,n1.split(' ')))
lista.sort()
n1 = lista[0]
n2 = lista[1]
print(n1, end=" ")
print(n2)

