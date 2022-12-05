numeroIf = 5
numeroWhile = 0
numeroFor = 0
estacion = "OTOÑO"

if numeroIf == 0:
    print("NumeroIf es 0")
elif numeroIf > 0:
    print("NumeroIf es positivo")
else:
    print("NumeroIf es negativo")

while numeroWhile < 3:
    print(numeroWhile)
    numeroWhile += 1

for i in range(numeroFor,4):
    print(i)

match estacion:
    case "VERANO":
        print("Estamos en verano")
    case "INVIERNO":
        print("Estamos en invierno")
    case "PRIMAVERA":
        print("Estamos en primavera")
    case "OTOÑO":
        print("Estamos en otoño")
    case _:
        print("No es una estación válida") 