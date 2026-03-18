#Funciones - Son bloques de codigo que realiza una tarea especifica que son reutilizables

#funcion sin parametros ni devolucion de valor
def saludar():
    print("Hola, bienvenidos al curso de python ")
   
saludar() 

#funcion con parametros
def saludo(nombre):
    print("Hola " +nombre+"  bienvenido a clases")
    
#llamada a la funcion 
saludo("Elsa Choquetarqui")
saludo("Gonzalo Cahuaya")

#funcion que devuelve valores
def suma(a,b):
    return a + b

#llamada a la funcion
resultado = suma(10,4)
print("la suma es: ", resultado)

#Estblecer valores por defecto para los parametros de una funcion 
def bienvenida(nombre="Estudiante"):
    print("Bienvenido ", nombre)
    
#llamada a la funcion 
bienvenida()
bienvenida("Elsa")

#funcion con argumentos variados 
def sumador(*args):
    return sum(args)
#llamada a la funcion 
print(sumador(1,2,3,4,5))
print(sumador(4,5,6))