def utskrift(lista):
    """
    Testar utskrift med print före rekursion
    """

    if len(lista) > 0:
        print(lista[0])
        utskrift(lista[1:])

def utskrift2(lista):
    """
    Testar utskrift med print efter rekursion
    """
     
    if len(lista) > 0:
        utskrift2(lista[1:])
        print(lista[0])

lista = [1,2,3,4,5]
utskrift(lista)
print()
lista = [1,2,3,4,5]
utskrift2(lista)
