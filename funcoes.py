def rendimento(carteira,porcentagem):
    lucro = carteira * (porcentagem/100)
    return lucro
        
def taxanxt(lucro, taxa):
    desconto =lucro * (taxa/100)
    return desconto

def lucroliqui(lucrobruto, taxa):
    lucroliquido = lucrobruto - taxa
    return lucroliquido

def afterretirada(a,b,c):
    saldobruto = a + b - c
    return saldobruto

def beforeretirada(a,b):
    retirada = a - b
    return retirada
