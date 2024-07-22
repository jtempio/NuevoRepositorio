# Opening "GfG.txt" text file
archivo = open("alumnos.txt","rt")
linea=archivo.readline()

while linea:
    legajo, nombre=linea.split(";")
    nombre=nombre.strip('\n')  
    #print(legajo,nombre)
    print(f"LU:{legajo:>7} - Nombre:{nombre}") 
    linea=archivo.readline()
    
    """lu, nombre = linea.split(";")
    nombre = nombre.strip('\n')
    print(f"LU:{lu:>7} - Nombre:{nombre}")
    linea = archivo.readline()"""

 
# prints current position

 

archivo.close()