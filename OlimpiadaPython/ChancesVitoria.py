t = int(input())
g = int(input())
listaG = []
lista = []
v,e,d = 3,1,0
for i in range(g):
    n = input().split(" ")
    listaG.append([int(index) for index in n])

for index in range(4):
    soma = 0
    for x in range(len(listaG)):
        if listaG[x][0] == (index+1):
            soma += listaG[x][2]
        elif listaG[x][1] == (index+1):
            soma += listaG[x][3]
    lista.append(soma)

quantJogos = 6 - len(listaG)
cont = 1
for i in range(4):
    if lista[i] > lista[t-1] and i != 2:
        dif = lista[i] - lista[t-1]
        if dif > 0:
            if e < dif:
                if 2*e < dif:
                    if 3*e > dif:
                        cont += 1
                        break
            elif v < dif:
                if 2*v < dif:
                    if 3*v > dif:
                        cont += 1
                        break
            elif e + v < dif:
                if 2*e + v < dif:
                    if 3*e + v < dif:
                        if 3*e + 2*v < dif:
                            if 3*e + 3*v > dif:
                                cont += 1
                                break
            elif 2*v+e < dif:
                if 3*v+e < dif:
                    if 3*v+2*e>dif:
                        cont += 1
                        break
            cont += 1
if cont == 4:
    print(3 ** (6-g))
else:
    print(0)
