
def primo(x):
    if x<=1:
        return False
    else:
        for n in range(2,int(x**0.5)+1):
            if x%n==0:
                return False
        return True
    

print([i if primo(i) else 0 for i in range(4)])
