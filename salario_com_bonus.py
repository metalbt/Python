nome = input()
salario = float(input())
vendas_em_dinheiro = float(input())
comissao = vendas_em_dinheiro * 0.15
total = salario + comissao
print('TOTAL = R$ {:.2f}'.format (total ))
