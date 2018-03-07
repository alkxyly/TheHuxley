entrada = input().split(" ") # recupera entrada em string
lista = [] # lista vazia
for i in range(int(entrada[0])):
    a = input()
    if(a[-1] == entrada[1]): # a[-1] ultima posição da string
        lista.append(int(a))
lista.sort()
tamanho = len(lista)
for i in range(5 - len(lista)): # recupera a diferença
    lista.append(-1) # adiciona -1 a lista 
lista.sort() # ordena a lista

for i in range(-5,0):
    print(lista[i])

#Outra forma de fazer 
#entrada = input().split(" ")
#nums = [input() for j in range(int(entrada[0]))]
#lista = [int(i) if entrada[1] == i[-1] else -1 for i in nums]
#lista.sort()
#[print(lista[i]) for i in range(-5,0)]
