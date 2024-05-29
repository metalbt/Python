nt = int(input()) #numero total de figurinhas
nc = int(input()) #numero comprado de figurinhas
lif = [] #lista de figurinhas compradas

for i in range(nc):
    nf = int(input()) #numero da figurinha comprada
    for e in lif:
        if nf == e:
            lif.remove(nf)
    lif.append(nf)

qtd = len(lif) #quantidade de figurinhas unicas

qtf = nt - qtd #quantidade de figurinhas faltando

if(qtf<0):
    print(0)
else:
     print(qtf)
