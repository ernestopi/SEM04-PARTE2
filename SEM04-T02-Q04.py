def minutos_para_hora(quant_minutos):
    horas = quant_minutos//60
    minutos = quant_minutos%60
    return f'{horas}:{minutos}'
minutos = int(input())
horas = minutos_para_hora(minutos)
print(f'{horas}')
