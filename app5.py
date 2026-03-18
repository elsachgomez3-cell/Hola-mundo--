#sentencias
#temperatura = 18
temperatura = int(input("Indica la temperatura: "))

if temperatura > 28:
    print("Esta hacinedo calor")
else:
    print("hace frio")
if temperatura > 28:
    print("Esta haciendo calor")
elif temperatura > 20:
    print("Es un dia agradable")
elif temperatura > 10:
    print("hace un poco de frio")
else:
    print("hace frio, brrrr")

print("Proceso concluido")