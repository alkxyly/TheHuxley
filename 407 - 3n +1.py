faixas = []
ciclos = []
while(True):
    try:
        faixas = input().split(' ')
        for i in range(int(faixas[0]),(int(faixas[1]) + 1)):
           
           aux = i
           operacoes = 0
           if(aux == 1):
               ciclos.append(i)
               operacoes = operacoes + 1
           else:
                while(aux != 1):
                    if((aux % 2) == 0):
                        aux = aux/2
                        operacoes = operacoes + 1
                    else:
                        aux = (aux * 3) + 1
                        operacoes = operacoes + 1
                 
                ciclos.append(int(operacoes + 1))
        #print(ciclos)
        print("{} {} {}".format(int(faixas[0]),int(faixas[1]),max(ciclos)))
        ciclos = []
    except EOFError:
        break