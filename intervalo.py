x = float(input())
if (x>100) or (x<0):
    print('Fora de intervalo')
elif (x<=25.00):
    print ('Intervalo [0,25]')
elif (x<=50.00):
    print ('Intervalo (25,50]')
elif (x<=75.00):
    print ('Intervalo (50,75]')
else:
    print('Intervalo (75,100]')
