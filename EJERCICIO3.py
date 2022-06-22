# EJERCICIO 3
# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *

altura = int(input("Digite una altura")); #4
while altura > 0 :
    print("*"*altura);
    altura -=1;
