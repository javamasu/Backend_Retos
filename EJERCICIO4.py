# EJERCICIO 4
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12

numero = int(input("Digite un numero"));

while numero <= 1:
    numero = int(input("Digite un numero"));

while numero > 1:
    if numero % 2 == 0:
        numero /= 2;
        print(numero);
    elif numero == 1:
        break;
    elif numero % 2 != 0:
        numero = numero*3+1;
        print(numero);
    else:
        break;
  