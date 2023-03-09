###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome:Gabriel Pavani GIro
# RA:247114
###################################################

# Leitura das tropas de defesa
defesa=[]
n=int(input())
for i in range(n):
    defesa.append(int(input()))


# Leitura das tropas de ataque
ataque=[]
m=int(input())
for i in range(m):
    ataque.append(int(input()))


# Processamento da guerra
for i in range(n-m): 
    vitorias=0
    empates=0
    for j in range(m):
        if defesa[i+j]-ataque[j]<0:
            vitorias+=1
        elif defesa[i+j]-ataque[j]==0:
            empates+=1
    if vitorias>0 and vitorias+empates>(m//2):
        check=True
        posicao=i+1
        break
    check=False


# Saída de dados
# ...
if check:
    print('Vitória posicionando as tropas a partir da posição', posicao)
else:
    print('Derrota')
