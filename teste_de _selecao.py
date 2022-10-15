todos = input().split(" ")
a = int(todos[0])
b = int(todos[1])
c = int(todos[2])
d = int(todos[3])
if(b>c) and (d>a) and (c+d>a+b) and (c>0) and (d>0) and (a%2==0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
