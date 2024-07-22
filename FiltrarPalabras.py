#Funciones

def filtrarPalabras(frase, n):
    palabras = frase.split()
    palabrasFiltradas = list(filter(lambda palabra: len(palabra) >= n, palabras))
    fraseFiltrada = ' '.join(palabrasFiltradas)
    return fraseFiltrada

# Programa Principal
frase = input("Ingrese una frase: ")
n = int(input("Ingrese la cantidad de caracteres: "))
resultado = filtrarPalabras(frase, n)
print(resultado)