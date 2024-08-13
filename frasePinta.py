def fraseCuadrado(frase):
    for i in range(10):
        print(frase)

def fraseVertical(frase):
    for i in range(len(frase)):
        print(frase[i])

def fraseTrianguloYo(frase):
    for i in range(len(frase)):
        for j in range(i):
            print(frase[j], end="")
        print()
        

def fraseTrianguloP(frase):
    for i in range(len(frase)):
        print(frase[i] * (i + 1))
        
#progtama principal
frase = input("Introduce una frase: ")
fraseCuadrado(frase)
print("\n\n")
fraseVertical(frase)
fraseTrianguloYo(frase)
fraseTrianguloP(frase)
