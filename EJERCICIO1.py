# EJERCICIO 1
# Escriba el codigo que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****

altura=int(input("Digite la altura"));
ancho=int(input("Digite el ancho"));
contador=0;

while contador < altura:
    print("*"*ancho);
    contador +=1;
