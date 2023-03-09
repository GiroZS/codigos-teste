##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Gabriel Pavani Giro 
# RA:247114
##################################################
horas_trabalhadas=0
horas_extras=0
# Leitura do valor da hora
V = int(input())

# Leitura do numero de dias trabalhados na semana
D = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia
for n in range(D):
    periodos=int(input())
    v=0
    for m in range(periodos):
        inicio=int(input())
        fim = int(input())
        v+=fim-inicio
    if v<=8:
        horas_trabalhadas+=v
    else:
        horas_trabalhadas+=v
        horas_extras+=v-8
if horas_trabalhadas>44+horas_extras:
    horas_extras+=horas_trabalhadas-(44+horas_extras)


# Calculo do valor devido ao funcionário
valor=(horas_trabalhadas*V)+(V/2*horas_extras)


# Impressão da saída
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))