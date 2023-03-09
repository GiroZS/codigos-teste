###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Gabriel Pavani Giro 
# RA: 247114
###################################################
n=1
estoque=0
vendas=0

# leitura da sequência de compras e vendas
while n!=0:
    n=int(input())
    if n<0 and (n*-1)<=estoque:
        vendas+=1
        estoque+=n
    elif n<0 and (n*-1)>estoque:
        print("Quantidade indisponível para a venda de "+str(n*-1)+" unidades.")
    else:
        estoque+=n    

# impressão da saída
print("Quantidade de vendas realizadas: "+str(vendas))
print("Quantidade em estoque: "+str(estoque))