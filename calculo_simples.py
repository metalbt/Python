codigo, quantidade1, valor1 = input().split(" ")
codigo2, quantidade2, valor2 = input().split(" ")

print("VALOR A PAGAR: R$ {:.2f}".format((int(quantidade1)*float(valor1)) + (int(quantidade2)*float(valor2))))
