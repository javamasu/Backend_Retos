# EJERCICIO 6
# ingresar numeros hasta que ese numero sea adivinado
# numero_adivinar = 10
# 5 => 'el numero es mayor que ese'
# 13 => 'el numero es menor que ese'
# 10 => 'felicidades adivinaste el numero'

numero=int(input("Digite el numero"));
numero_adivinar =10;

if numero < numero_adivinar:
    print("el numero es mayor que ese")
elif numero == numero_adivinar:
    print("felicidades adivinaste el numero")
else:
    print("el numero es menor que ese")
