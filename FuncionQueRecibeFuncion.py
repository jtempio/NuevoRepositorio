def funcion (x):
    return x(2)

la=lambda x : 2**x
la1=lambda y : y/2

print(funcion(x=la))
print(funcion(x=la1))
print(funcion(x=lambda y : y*y))
      
      