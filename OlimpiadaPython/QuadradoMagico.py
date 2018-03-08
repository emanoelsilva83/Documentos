listaQ = []
lista = []
for i in range(4):
        entrada = input().split(" ")
        listaQ.append([int(index)for index in entrada])

for index,valor in enumerate(listaQ):
    soma = 0
    soma2 = 0
    for i in valor:#somando as linhas
        soma += i
    lista.append(soma)
    for i in range(len(listaQ)):#somando as colunas
        soma2 += listaQ[i][index]
    lista.append(soma2)
if lista[0] == lista[1] == lista[2] == lista[3] == lista[4] == lista[5] == lista[6] == lista[7]:
    print("magic")
else:
    print("not magic")
