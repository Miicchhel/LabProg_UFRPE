#Autor: Mi Chel
import sys 

#retirando o hardcode (usando a biblioteca sys)
arqent=open(sys.argv[1],"r")
arqsaida=open(sys.argv[2],"w")

#laco para ler o arquivo de entrada
l=[]
while True:
    linha = arqent.readline()
    if linha == "":
        break    
    l.append(int(linha))
#calculo com os arquivos da entrada
def funcao(x):
    m=1
    for i in x:
        m=m*i
    return m

#executando a fucao e vendo o resultado        
resultado=funcao(l)
print("resultado = "+str(resultado))

#escrevendo o resultado em um arquivo de saida
arqsaida.write("O resultado da entrada e: "+str(resultado))

arqent.close()
arqsaida.close()