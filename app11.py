#Diccionarios--> Almacen a pares clave-valor
mi_diccionario = {'nombre':'Elsa Choquetarqui', 'edad':24, 'ciudad':'La Paz'}
print(mi_diccionario)
#Acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['ciudad'])

#Agregar elementos
mi_diccionario['profesion']= 'Ingeniera'
print(mi_diccionario)

#Eliminar un elemento
del mi_diccionario['ciudad']
print(mi_diccionario)

#Obtener claves del diccionario 
print(mi_diccionario.keys())

#Obtener valores del diccionario
print(mi_diccionario.values())

#verificar si una clave existe
if 'edad' in mi_diccionario:
    print("clave encontrada")
    
if 'ciudad' in mi_diccionario:
    print("clave encontrada")
    
#Recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("{clave: ]",clave,"[valor:] ",valor)
