k = int(input())
codigo = input().upper()
soma = ""
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(len(codigo)):#codigo decodificador
    S = (3 * (i+1) + k)
    S = (alfabeto.index(codigo[i])-S)
    soma += alfabeto[S]
print(soma)
"""
for i in range(len(codigo)): #codigo codificador
    S = 3 * (i+1) + 3 #
    S = (S+ alfabeto.index(codigo[i])+1)
    if S > 26:
        S -= 26
soma += alfabeto[S-1]"""
