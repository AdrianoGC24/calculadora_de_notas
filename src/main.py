print("############################")
print("### CALCULADORA DE NOTAS ###")
print("############################")


contador = 0
suma = 0

while True:
    notas = float(input("ingresa una nota (para dar el resulado coloque el numero 0) "))

    

    if notas == 0:
        break

    suma += notas
    contador += 1
    
if contador > 1:
    promedio = suma / contador
    print("¡Listo! se ha generado tu promedio de notas")
    print(f"La cantidad de notas que tienes son {contador} y tienes un promedio de {promedio}")
else:
    print("Ingresa minimo 2 notas para sacar un promedio")