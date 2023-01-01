import os

listaPrimos = []
num = 2

while(num <= 250):
    aux = []
    for i in range(1,num+1):
        if num%1==0 and num%i==0:
            aux.append(i)
    if len(aux)==2:
        listaPrimos.append(num)
    num += 1

archivo = open("results.txt", "w")
archivo.write(str(listaPrimos))
archivo.close()