img=input().split(" ",2)
l=int(img[0])
a=int(img[1])
n=int(input())
m=[]
sel=[0]
def espelhamento(csex,csey,o,y,z):
    if o=="h":
        for i in range(csex,y):
            for j in range(csey,z//2): 
                m[i][j],m[i][(z-1)-j]=m[i][(z-1)-j],m[i][j]
    else:
        for i in range(y//2):
            for j in range(z-1,-1,-1): 
                m[i][j],m[y-1-i][j]=m[y-1-i][j],m[i][j]
def copia(csex,csey):
    for i,v in zip(range(csex,csex+len(sel)),range(len(sel))):
        for j,w in zip(range(csey,csey+len(sel[0])),range(len(sel[0]))):
            m[i][j]=sel[v][w]
for i in range(a):
    j=input().split()
    m.append(j)
for x in range(n):
    op=input().split()
    if op[0]=="rotacao":
        if sel==[0]:
            mt = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
            m=mt
            espelhamento(0,0,"h",len(m),len(m[0]))
        else:
            mt = [[sel[j][i] for j in range(len(sel))] for i in range(len(sel[0]))]
            sel=mt
            espelhamento(xsel,ysel,"h",len(sel),len(sel[0]))
    elif op[0]=="selecao":
        sel=[]
        xsel=int(op[1])
        ysel=int(op[2])
        for i in range(ysel,int(op[4])+ysel):
            s=[]
            for j in range(xsel,int(op[3])+xsel):
                s.append(m[i][j])
            sel.append(s)
    elif op[0]=="recorte":
        for i in range(xsel,len(m)):
            for j in range(ysel,len(sel[0])):
                m[i][j]="000"
        copia(int(op[2]),int(op[1]))
    elif op[0]=="copia":
        copia(int(op[2]),int(op[1]))   
    elif op[0]=="espelhamento":
        if sel==0:   
            espelhamento(0,0,op[1],a,l)
        else:
            espelhamento(xsel,ysel,op[1],len(sel),len(sel[0]))

for i in range(len(m)):
    for j in range(len(m[0])):
        if j==len(m[0])-1:
            print(m[i][j])
        else:
            print(m[i][j],end=" ")