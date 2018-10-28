from tratamentoClass import Tratamento
from operator import itemgetter

tratamento = Tratamento()
arq = open("base.txt","r")
a = arq.readlines()
arq.close()
vet = []
vetor = []
i = 0
for x in a:
    x = x.split("$w$m$f$")
    #print(x)
    x = tratamento.remover_acentos(x[0])
    y = x.split()
    for aux in y:
        aux = aux.lower()
        aux = aux.strip()
        if(aux!=""):
            if(aux not in vet):
                vet.append(aux)
                vetor.append([aux,1])
            else:
                alvo = vet.index(aux)
                cont = vetor[alvo][1]
                cont = cont + 1
                vetor[alvo][1]= cont

lista = vetor              
lista =  sorted(lista, key=itemgetter(0),reverse=False)
lista =  sorted(lista, key=itemgetter(1),reverse=True)

for x in lista:
    print(x)


    
