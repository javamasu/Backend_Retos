# EJERCICIO 5
# si el texto de ingreso es:
# texto = "hola alumnos buenas noches ya se viene el break"
# entonces el texto resultado debera ser:
# resultado_final = ["Hola", "Alumnos", "Buenas", "Noches", "Ya", "Se"]
# Hacer el codigo para ello

texto = "hola alumnos buenas noches ya se viene el break"

cantidadEspacio=0;
resultado_final=[];
textoTemporal="";

for caracter in texto:
    if caracter != " ":
        textoTemporal +=caracter;
    else:
        resultado_final.append(textoTemporal);
        textoTemporal = "";
resultado_final.append(textoTemporal);
print(resultado_final)