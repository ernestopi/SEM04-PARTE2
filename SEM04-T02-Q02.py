def area_quadrado (lado):
    return lado * lado
def perimetro_quadrado (lado):
    return lado * 4
valor_do_lado = float(input())
print(f'%10.4f'%area_quadrado(valor_do_lado))
print(f'%10.4f'%perimetro_quadrado(valor_do_lado))
