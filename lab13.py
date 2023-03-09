###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome: Gabriel Pavani Giro
# RA: 247114
###################################################

# Leitura de dados
brancos=0
nulos=0
quant=1
contagem=[]
candidatos=[]
voto=input()
while voto!="0":
    if voto=="Branco":
        brancos+=1
    elif voto=="Nulo":
        nulos+=1
    elif voto in candidatos:
        quant+=1
    else:
        candidatos.append(voto)
        contagem.append(quant)
        quant=1
    voto=input()
contagem.append(quant)
contagem.pop(0)
# Saída de dados

for i in range(len(candidatos)):
    max=0
    pos=0
    for j in range(len(contagem)):
        if contagem[j]>max:
            max=contagem[j]
            pos=j
    print(candidatos[pos],contagem[pos])
    contagem[pos]=0
print("Brancos",brancos)
print("Nulos", nulos)