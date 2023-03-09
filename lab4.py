conta = 0

while conta != "0":
    calc = input()
    l = calc.split(" ",2)
    conta=l[0]
    x=l[1]
    y=l[2]

    if conta=="+":
        resultado=int(x)+int(y)
        print(resultado)
    elif conta=="-":
        resultado=int(x)-int(y)
        print(resultado)
    elif conta=="*":
        resultado=int(x)*int(y)
        print(resultado)
    elif conta=="/":
        resultado=int(x)//int(y)
        resto=int(x)%int(y)
        print(resultado, resto)
    elif conta==";":
        k = []
        j = 1
        if int(x)==int(y):
            print("0")
        else:
            if int(x)>int(y):
                i = int(x)-int(y)
            else:
                i = int(y)-int(x)                
            while j<=i :
                if i%j == 0:
                    k.append(int(j))
                j+=1
            for i in range(len(k)):
                if i==len(k)-1:
                    print(k[i])
                else:
                    print(k[i], end =" ")
            