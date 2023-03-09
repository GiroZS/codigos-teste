###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Gabriel Pavani Giro
# RA: 247114
###################################################

# Leitura de dados
estoque = {}
comando=input()
C={}
V={}
# Processamento
while comando!="FIM":
    comando=comando.split(" : ",2)
    N=comando[0]
    E=int(comando[1])
    estoque[N]=0
    print(estoque[N])
    if E>0:
        estoque[N]+=E
        C[N]+=1
    elif estoque[N]<(E*(-1)):
        print("Quantidade indisponivel para a venda de " + str(E*(-1)) + " unidade(s) do produto " + N + ".")
    else:
        estoque[N]-=E
        V[N]+=1
# Impressão da saída
for key, value in estoque.items():
    print("Produto: " + key)
    print("Quantidade em Estoque: " + estoque[key])
    print("Pedidos de Compra: " + C[key])
    print("Pedidos de Venda: " + V[key])