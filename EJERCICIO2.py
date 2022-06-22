# EJERCICIO 2
# Escribir el codigo que el usuario le ingrese el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****             5 = 2*2 +1   = 2*3-1
#      *******            7 = 2*3 +1   = 2*4-1
#     *********           9 = 2*4 +1   = 2*5-1 
#    ***********         11 = 2*5 +1   = 2*6-1
#   *************        13 = 2*6 +1       
#   *************        13    .
#   *************        13    .
#   *************        13    .
#   *************        13
#    ***********         11
#     *********           9
#      *******            7
#       *****             5

grosor= int(input("Digite el grosor"));
grosorAuxiliar1=grosor;
grosorAuxiliar2=grosor;
contador2=0;

#arriba

for i in range (1,grosor):
    print(" "*(grosorAuxiliar1-1),"*"*(grosorAuxiliar2));
    grosorAuxiliar1 -=1;
    grosorAuxiliar2 +=2;
    
    if grosorAuxiliar1 < 0:
        break;

#medio (5)
for i in range(1,grosor+1):
    print("","*"*(2*(grosor+1)+1))

#abajo
grosorAuxiliar1=1;
grosorAuxiliar2=grosor;
for i in range (1,grosor):
    print(" "*(grosorAuxiliar1),"*"*(2*grosorAuxiliar2+1));
    grosorAuxiliar2 -=1;
    grosorAuxiliar1 +=1;
    
    if grosorAuxiliar2 < 0:
        break;