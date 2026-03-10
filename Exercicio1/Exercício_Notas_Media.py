import statistics
import statistics as st
def notas():
    n1 = float(input("Digite sua N1: "))
    n2 = float(input("Digite sua n2: "))
    n3 = float(input("Digite sua n3: "))
    
    entradas = (n1, n2, n3)

    media = statistics.mean(list(entradas))

    if media <5:
        print("\nO estudante está em recuperação, pois sua  média é igual a ", media)
    else:
        print("\nO estudante foi aprovado com média ", media)
    
notas()





