v=int(input())
v2 = v
n100=0
n50=0
n20=0
n10=0
n5=0
n2=0
n1=0

while(True):
    n100+=int(v/100)
    v=v%100       
    if(v<100):
        break

while(True):
    n50+=int(v/50)
    v=v%50       
    if(v<50):
        break

while(True):
    n20+=int(v/20)
    v=v%20       
    if(v<20):
        break
    
while(True):
    n10+=int(v/10)
    v=v%10       
    if(v<10):
        break
    
while(True):
    n5+=int(v/5)
    v=v%5       
    if(v<5):
        break

while(True):
    n2+=int(v/2)
    v=v%2       
    if(v<2):
        break
    
while(True):
    n1+=int(v/1)
    v=v%1       
    if(v<1):
        break
    

     
print(v2)
print("{} nota(s) de R$ 100,00".format(n100))
print("{} nota(s) de R$ 50,00".format(n50))
print("{} nota(s) de R$ 20,00".format(n20))
print("{} nota(s) de R$ 10,00".format(n10))
print("{} nota(s) de R$ 5,00".format(n5))
print("{} nota(s) de R$ 2,00".format(n2))
print("{} nota(s) de R$ 1,00".format(n1)) 
