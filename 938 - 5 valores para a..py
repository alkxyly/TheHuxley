nums = [float(input("Digite um valor:\n")) for j in range(5)]
valor = []
[valor.append(i) if i < 0 else 0 for i in nums]
print("Foram digitados {} numeros negativos".format(len(valor)))
