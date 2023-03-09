#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome: Gabriel Pavani Giro
# RA:247114
#####################################################


'''
Dica: A criação das seguintes funções pode facilitar o desenvolvimento
do laboratório:
1) Uma função para rotacionar a peça em 90 graus para direita.
2) Uma função para verificar se é possível encaixar a peça a partir de
uma determinada linha e coluna do tabuleiro.
'''
possibilidades=[]
def rotacao(mat):
  mat=list(zip(*mat[::-1]))
  mat= [list(ele) for ele in mat]
  return mat
def verifica(tab,piece):
  possib=0
  for g in range(len(tab)-(len(piece)-1)):
    for h in range(len(tab[0])-(len(piece[0])-1)):
      erro=False
      for i in range(len(piece)):
        for j in range(len(piece[0])):
          if tab[i+g][j+h]=="X" and piece[i][j]=="X":
            erro=True
            break
      if not erro:
        possib+=1
  return possib

# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for _ in range(T):
  tabuleiro.append(input().split())

# Leitura da peça
P = int(input())
peca = []
for _ in range(P):
  peca.append(input().split())

# Processamento
for k in range(4):
  possibilidades.append(verifica(tabuleiro,peca))
  peca=rotacao(peca)

# Impressão do resultado
print(','.join(map(str,possibilidades)))