turno=2
checa=False
sarah = input().split(" ",2)
clone = input().split(" ",2)
hpSarah=int(sarah[0])
hpClone=int(clone[0])
atkSarah=int(sarah[1])
atkClone=int(clone[1])
dfcSarah=int(sarah[2])
dfcClone=int(clone[2])
x = int(input())
def par(y):
    if y%2==0:
        return True
    else:
        return False
def altr():
    global x
    x=(7*x+111)%1024
    print("MENSAGEM DEBUG - número gerado: "+str(x))
    return x
def soco(atk,dfc):
    global hpSarah,hpClone
    m=altr()%3
    if dfc>atk:
        dano=0
    else:
        dano=(atk-dfc)*m
    if personagem:
        print("O clone sofreu "+str(dano)+" pontos de dano!")
        hpClone=hpClone-dano 
    else:
        print("Sarah sofreu "+str(dano)+" pontos de dano!")
        hpSarah=hpSarah-dano       
def arremesso_de_facas():
    global hpSarah,hpClone
    m=altr()%6
    dano2=0
    if personagem:
        for i in range(1,m+1):
            dano2=atkSarah//(3**i)+dano2
        print("O clone sofreu "+str(dano2)+" pontos de dano!")
        hpClone=hpClone-dano2
    else:
        for i in range(1,m+1):
            dano2=atkClone//(3**i)+dano2
        print("Sarah sofreu "+str(dano2)+" pontos de dano!")
        hpSarah=hpSarah-dano2
def invocacao_de_fada():
    global hpClone,hpSarah,atkClone,atkSarah,dfcClone,dfcSarah
    p=altr()%100
    q=altr()
    if personagem:
        print("Sarah ganhou "+str(p)+" pontos de vida!")
        hpSarah=hpSarah+p
    else:
        print("O clone ganhou "+str(p)+" pontos de vida!")
        hpClone=hpClone+p
    
    if q<100:
        if par(q):
            if personagem:
                print("Sarah ganhou "+str(q)+" pontos de defesa!")
                dfcSarah=dfcSarah+q
            else:
                print("O clone ganhou "+str(q)+" pontos de defesa!")
                dfcClone=dfcClone+q
        else:
            if personagem:
                print("Sarah ganhou "+str(q)+" pontos de ataque!")
                atkSarah=atkSarah+q
            else:
                print("O clone ganhou "+str(q)+" pontos de ataque!")
                atkClone=atkClone+q
    elif q>=1019:
        if personagem:
            print("O quê? A fada trouxe um monstro gigante com ela!\nO Clone e o castelo foram destruídos,\ne Sarah agora tem um novo pet.\nFINAL SECRETO - PARABENS???")
            exit()
        else:
            print("O quê? A fada trouxe um monstro gigante com ela!\nSarah foi derrotada...")
            exit()
def chk(hp):
    if hp<=0:
        return True
while checa==False:
    personagem=par(turno)
    ataque=input()
    if ataque=="soco":
        if personagem:
            soco(atkSarah,dfcClone)
        else:
            soco(atkClone,dfcSarah)
    if ataque=="facas":
        if personagem:
            arremesso_de_facas()
        else:
            arremesso_de_facas()
    if ataque=="fada":
        invocacao_de_fada()
    if chk(hpSarah):
        print("Sarah foi derrotada...")
        checa=True
    if chk(hpClone):
        print("O clone foi derrotado! Sarah venceu!\nFIM - PARABENS")
        checa=True
    turno+=1



