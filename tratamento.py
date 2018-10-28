from tratamentoClass import Tratamento
from collections import defaultdict
import csv
from collections import OrderedDict as ordereddict
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from string import punctuation

def popArray(type, word, array):
    if(type and word not in array):
        #array.append([word, 1])
        array.append(word)
    '''elif(type and word in array):
        alvo = array.index(word)
        cont = array[alvo][1]
        cont += 1
        array[alvo][1] = cont'''

def prepResult(title, array):
    arq_base = open("base.txt","r")
    text = arq_base.read().lower().split()

    chrs = (78 - len(title)) / 2
    cont = 0
    enf = ""
    enf2 = "_"
    while cont < chrs:
        enf += "*"
        enf2 += "_"
        cont += 1
    result = ("\n//" + enf + " " + title + " " + enf + "\\\\\n\n"
        "|                   Palavra                    |   |          Frequência           |\n\n")
    frequencia = FreqDist(text)
    frequencia_ord = ordereddict(sorted(frequencia.items(), key = lambda e: (-e[1], e[0])))

    for freq in frequencia_ord:
        if(freq in array):
            lim = 84 / 2
            right = lim / 2 + len(freq)
            chrs = (78 - (len(freq)) + len(str(frequencia_ord[freq]))) / 4
            cont = 0
            enf = ""
            while cont < chrs:
                enf += " "
                cont += 1
            result += "|" + enf + freq + enf + " | " + enf + str(frequencia_ord[freq]) + enf + "|\n"
        

    result += "\n\\\\________________________________________________________________________________//\n\n"
    arq_base.close()
    return result

tratamento = Tratamento()
arq = open("base.txt","r")
arq_results = open("results.txt", "w")
arq_results_csv = open("results.csv", "w")
#arq_links = open("links.txt", "w")
links = []
#arq_rts = open("rts.txt", "w")
rts = []
#arq_mentions = open("mentions.txt", "w")
mentions = []
#arq_verbos = open("verbos.txt", "w")
verbos = []
#arq_stopWords = open("stopWords.txt", "w")
stop_words = []
#arq_expr = open("expr.txt", "w")
exprs = []
tweets = arq.readlines()

stopwords_list = set(stopwords.words('portuguese') + list(punctuation))

print("Preparando Tweets...")

for line in tweets:
    linetr = tratamento.remover_acentos(line).lower()
    words = linetr.lower().split()
    
    ### RTs ###
    isrt = False
    rt = re.findall(r'^rt\s?@\w+:', linetr)
    if(rt):
        rt = rt[0]
        isrt = tratamento.identificaRTs(linetr)
        popArray(isrt, rt, rts)
        words = words[2:]

    for word in words:
        word = word.strip()
        if(word != ""):

            ### Links ###
            islink = tratamento.identificaLinks(word)
            popArray(islink, word, links)

            ### Mentions ###
            ismention = tratamento.identificaMentions(word)
            if(ismention and not rt.__contains__(word)):
                popArray(ismention, word, mentions)

            ### Verbos ###
            isverbo = tratamento.removeChrEspeciais(word)[:-0] == 'r'
            popArray(isverbo, tratamento.removeChrEspeciais(word), verbos)

            ### StopWords ###
            isstopword = tratamento.removeChrEspeciais(word) in stopwords_list
            popArray(isstopword, tratamento.removeChrEspeciais(word), stop_words)

            ### Demais Expressões ###
            if(word not in links and word not in rts and word not in mentions 
                and word not in verbos and tratamento.removeChrEspeciais(word) not in stopwords_list):
                popArray(True, tratamento.removeChrEspeciais(word), exprs)

    #print(links, '\n', rts, '\n', mentions, '\n', verbos, '\n', stop_words, '\n', exprs)
    #break

spamwriter = csv.writer(arq_results_csv, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
print("Preparando arquivo de resultados...")

spamwriter.writerow(("############# Arquivo de Resultados de avaliação dos Tweets #############\n\n"
        "Aluno = Saulo Henrique Gomes Castro\n"
        "Quantidade de Tweets avaliados = " + str(len(tweets)) + "\n\n"))
result = ("############# Arquivo de Resultados de avaliação dos Tweets #############\n\n"
        "Aluno = Saulo Henrique Gomes Castro\n"
        "Quantidade de Tweets avaliados = " + str(len(tweets)) + "\n\n")
result += prepResult("LINKS", links)
#result += prepResult("RETWEETS", rts)

### AVALIANDO RETWEETS ###
arq_base = open("base.txt","r")
text = arq_base.readlines()
freq_rts = defaultdict(int)

for stmt in text:
    words = stmt.lower().split()
    i = 0
    if(stmt[0:2].lower() == 'rt'):
        for word in words:
            if(word == 'rt'):
                word = words[i] + " " + words[i +1]
                if(word in rts):
                    freq_rts[word] += 1
            i += 1
chrs = (78 - len("RETWEETS")) / 2
cont = 0
enf = ""
enf2 = "_"
while cont < chrs:
    enf += "*"
    enf2 += "_"
    cont += 1
result += ("\n//" + enf + " RETWEETS " + enf + "\\\\\n\n"
            "|                   Palavra                    |   |          Frequência           |\n\n")
freq_rts_ord = ordereddict(sorted(freq_rts.items(), key = lambda e: (-e[1], e[0])))
for freq in freq_rts_ord:
    chrs = (78 - (len(freq)) + len(str(freq_rts_ord[freq]))) / 4
    cont = 0
    enf = ""
    while cont < chrs:
        enf += " "
        cont += 1
    result += "|" + enf + freq + enf + " | " + enf + str(freq_rts_ord[freq]) + enf + "|\n"

result += "\n\\\\________________________________________________________________________________//\n\n"
arq_base.close()
### FIM AVALIANDO RETWEETS ###

result += prepResult("MENTIONS", mentions)
result += prepResult("VERBOS", verbos)
result += prepResult("STOP WORDS", stop_words)
result += prepResult("DEMAIS EXPRESSÕES", exprs)


#print(result)
arq_results.write(result)
spamwriter.writerow(result)
arq.close()
arq_results.close()
print("Processamento Finalizado!")