senha = 2002
while(True):
  tentativa = int(input())
  if(tentativa!=senha):
    print('Senha Invalida')
  else:
    print('Acesso Permitido')
    break
