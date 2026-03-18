#metodos de listas
numeros = [1,2,3,4,5]

#Adicionr elementos a una lista
numeros.append(6)

print(numeros)

#insertar elementos en una posicion determinada 
numeros.insert(0,-1)
print(numeros)

numeros.insert(1,0)
print(numeros)

#eliminar un elemento en su primera aparicion
numeros.remove(3)
print(numeros)

numeros.remove(1)
print(numeros)

#verificar si un elemento se encuentra en la lista
print(3 in numeros)

print(4 in numeros)
#calcular tamaño de la lista
print(len(numeros))

#elimina el contenido de la lista
numeros.clear()
print(numeros)

