qtd=0 #quantidade de acertos
aps = input().split() #AO RECEBER ELEMENTOS COM .SPLIT() EM UMA UNICA VARIAVEL ELA VIRA UMA LISTA
for e in range(len(aps)): #DEPOIS PODE SER FAZER UM FOR I IN RANGE EM SEU LEN() CASO QUEIRA POR EXEMPLO TRANSFORMAR SEUS ELEMENTOS EM INTEIROS
    aps[e] = int(aps[e]) #O I DEVE SER O INT(I)

sor = input().split() #numeros sorteados
for e in range(len(sor)):
    sor[e] = int(sor[e])

for i,e in enumerate(aps): #PODE SE FAZER UM FOR I IN "NOME DA LISTA" COM UM FOR I IN "NOME DA LISTA 2" DENTRO DELE PARA COMPARAR OS ELEMENTOS DESSAS DUAS LISTAS.
     for i,f in enumerate(sor):
          if(e==f):
               qtd+=1
       

if(qtd<3):
     print("azar")
elif(qtd==3):
     print("terno")
elif(qtd==4):
     print("quadra")
elif(qtd==5):
     print("quina")
elif(qtd==6):
     print("sena")
