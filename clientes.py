import sys

#Josiane Igor, Marcos Zero, Sylei Pastor, Rose do Marco.

def buscaindice(nomeinformado):
    tabela = ["Adelmo", 5723.48, 22, "Marcos", 32890.27, 20, "Cilso", 71468.74, 3, "Aline", 2000, 20, "Airan",
    36403.07, 20, "Josiane" , 26917.05, 19, "Siley", 16036.34, 27, "Rose", 31785, 24,
    "Jonatas Evangelista", 8538.20, 2, "Jéssica", 11000, 20, "Ana Caroline", 1000, 18, "Adélia", 5000, 18, "Joarbson", 6000, 17, "Clemente", 20000, 20]
    if nomeinformado in tabela:
        client = tabela.index(nomeinformado)
        aplicacao = tabela[client+1]
        dia = tabela[client+2]
        return aplicacao, dia
    else:
        print("Nome incorreto!")
        print("Verifique a lista e rode o programa novamente!")
        sys.exit()