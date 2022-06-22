# EJERCICIO 7
# dado los siguientes numeros:
# numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
# indicar cuantos de ellos son multiplos de 3 y de 5 , ademas si hay un multiplo de 3 y de 5 no contabilizarlos
# multiplos de 3: 3 , multiplos de 5: 1

numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
cantidadMultiplo3=0;
cantidadMultiplo5=0;
cantidadMultiplo3_5=0;

for numero in numeros:
    if numero % 15 == 0:
        cantidadMultiplo3_5 +=1;
    if numero % 3 == 0:
        cantidadMultiplo3 +=1;
    if numero % 5 == 0:
        cantidadMultiplo5 +=1;

print("""La cantidad de multiplos de 3 es {}, 
la cantidad de multiplos de 5 es {},
la cantidad de multiplos de 15 es {}""".format(cantidadMultiplo3, cantidadMultiplo5,cantidadMultiplo3_5))

    