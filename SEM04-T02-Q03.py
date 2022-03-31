def percentual(valor,porcentagem):
    return valor * (porcentagem/100)
preco=float(input())
valor_percentual=float(input())
preco_acrescido=preco+percentual(preco,valor_percentual)
preco_desconto=preco-percentual(preco,valor_percentual)
print(f'%.2f'%preco_acrescido)
print(f'%.2f'%preco_desconto)

