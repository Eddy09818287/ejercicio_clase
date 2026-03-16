def si_puede_votar (edad):
    if edad >= 18 :
        return("si puedes votar.")
    elif edad< 18 :
        return("no puede votar.")
nombre = input("ingrese su nombre:")
while True:
    try:
        edad = int(input("ingrese su edad:"))
        resultado = si_puede_votar(edad)
        break
    except ValueError:
        print("MAL,ingrese un valor numerico")
print(resultado)