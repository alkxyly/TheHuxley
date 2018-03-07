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
