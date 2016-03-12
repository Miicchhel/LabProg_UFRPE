#Autor: Mi Chel
import sys
#abrindo os arquivos
arqent=open("E2.txt","r")
arqsaida=open("E2saida.txt","w")

#lendo os arquivos
a=arqent.read()
a=a.split("\n")

#retornando os retangulos 1 e 2 
for i in range(len(a)):
    ret1=a[i]
    ret2=a[i+1]
    break
ret1=ret1.split(' ')
ret2=ret2.split(' ')

#retornando os pontos ret1
#ponto 1: p1
px1=ret1[0]
py1=ret1[1]
#ponto 2: p2
px2=ret1[2]
py2=ret1[3]

#retornando os pontos ret2
#ponto 1: p3
px3=ret2[0]
py3=ret2[1]
#ponto 2: p4
px4=ret2[2]
py4=ret2[3]


