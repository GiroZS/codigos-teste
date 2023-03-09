###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Gabriel Pavani Giro
# RA: 247114
###################################################

def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))

def expansao(imagem_original):
    

def retracao(imagem_original):
    

# leitura da imagem
_ = input() #P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()]

_ = input() #255 - linha a ser ignorada

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

# leitura do tipo de redimensionamento

# impressão da imagem final
imprimir_imagem(imagem)