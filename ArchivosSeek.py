# Opening "GfG.txt" text file
archivo = open("Archivo.txt", "w+t")
 
# Second parameter is by default 0
# sets Reference point to twentieth
# index position from the beginning

archivo.write("1,Agustin\n")
archivo.write("2,Pedro\n")
archivo.write("3,Juan\n")
archivo.write("1,Diego\n")
archivo.write("1,Martin\n")
archivo.write("1,Gabi\n")
archivo.seek(0)
print(archivo.tell())
linea=archivo.readline()
print(archivo.tell())
while linea:
    legajo, nombre=linea.split(",")
    nombre.rstrip('\n')
    print(archivo.tell())
    print(legajo,nombre, end="")
    if(legajo=="1"):
        archivo.write("1,Agustina\n")
        print(archivo.tell())
        
        
    
    
    
    linea=archivo.readline()

 
# prints current position
print(archivo.tell())
 

archivo.close()