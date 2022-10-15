qtde = 0
soma = 0
for i in range (6):
  valor = float(input())
  if (valor > 0):
    qtde = qtde + 1
    soma = soma + valor
media = soma / qtde
print('{} valores positivos'.format(qtde))
print('{:.1f}'.format(media))
