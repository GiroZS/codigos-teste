###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Gabriel Pavani Giro 
# RA: 247114
###################################################

# Leitura da palavra
palavra = input()
word=[]
word.extend(palavra)
teste=False
# Leitura dos palpites e impressão do resultado para cada palpite
for i in range(6):
    palpite=[]
    proof=[]
    palpite.extend(input())
    for n in range(len(word)):
        if word[n]==palpite[n]:
            proof.append(palpite[n].upper())
        else:
            try: 
                if word.index(word[n]) != palpite.index(word[n]):
                    proof.append(palpite[n].lower())
                    print(word.index(word[n]), palpite.index(word[n]))
            except:
                proof.append("_")
    if palpite == word:
        teste=True
        print(*proof, sep="")
        break
    else:
        print(*proof, sep="")
        




# Impressão da linha final
# ...
if teste:    
    print("Resposta correta")
else:
    print("Palavra correta:", palavra)
