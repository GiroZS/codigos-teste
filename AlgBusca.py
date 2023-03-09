#Algoritmos de sort

def Bubble(l,conta):

    for i in range(len(l) - 1):
        trocou = False
        for j in range(len(l)-1,i,-1):
            if l[j-1]>l[j]:
                l[j-1], l[j] = l[j], l[j-1]
                conta=conta+2
                print(conta)
                trocou = True
        if not trocou:
            break

def Insert(l,conta):
    for i in range(1, len(l)):       
        aux = l[i]
        j=i
        while j > 0 and l[j-1] > aux:
            l[j] = l[j-1]
            conta=conta+1
            print(conta)
            j-=1
        l[j]=aux
        

def Selection(l):
    for i in range(len(l) - 1):
        m=i
        for j in range(i+1, len(l)):
            if l[m] > l[j]:
                m=j
        l[m], l[i] = l[i], l[m]
        conta+=2

def busca_binaria(l,x):
    global y
    e = 0 
    d = len(l) - 1
    while e <=d:
        m = (e+d)// 2
        y=y+1
        print(y)
        if l[m] ==x:
            
            return m
        elif l[m] < x:
            e = m+1
        else:
            d=m-1
    return -1
