nota1 = int(input("Ingresa una nota: "))
nota2 = int(input("Ingresa una nota: "))
nota3 = int(input("Ingresa una nota: "))

nota_media = (nota1 + nota2 + nota3) / 3
if nota_media >= 5:
    nota_final = "Aprobado"
else :  
        nota_final = "Suspendido"

print(nota_final)