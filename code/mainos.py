import time

name = input("You Name: ")
password = input("You password: ")
detectDev = input("You are a dev? y/n: ")

if detectDev == "y":
    nameofdev = name
    print(f"Ok {nameofdev}")

elif detectDev == "n":
    nameofperson = name
    print(f"Ok {nameofperson} you not are dev")

time.sleep(3)
print("loading name")
time.sleep(1)
print("loading data")
time.sleep(1)
print("loading language")
time.sleep(1)
print("error: language not defined" \
" wait me 5 seconds")
time.sleep(5)

nameNormal = name
language = input(f"OK {nameNormal} Time to choose your language/ hora de elegir tu lenguaje esp/ing: ")

if language == "esp":
    print(f"haci esta mejor {nameNormal}?")
    si = input("mejor? s/n: ")
    if si == "s":
        print("genial! ya elegimos tu lenguaje!")
    if si == "n":
            print("ok elegimos otro")
            si2 = input("ing:")
            if si2 == "ing":
                print(f"let's go {nameNormal}")
if language == "ing":
    print(f"It's better this way. {nameNormal}?")
    si = input("better? y/n: ")
    if si == "y":
        print("Great! We've chosen your language!")
    if si == "n":
            print("Okay, let's pick another one.")
            si2 = input("esp:")
            if si2 == "esp":
                print(f"genial! {nameNormal}")

if language == "ing":
    calquestion = input(f"@{nameNormal}: c Open a calculator")

if language == "esp":
    calquestion = input(f"@{nameNormal}: c Abre una calculadora")

if calquestion == "c":
    print("Loading calculator %1")
    time.sleep(1)
    print("Loading calculator %5")
    time.sleep(1)
    print("Loading calculator %15")
    time.sleep(1)
    print("Loading calculator %25")
    time.sleep(1)
    print("Loading calculator %50")
    time.sleep(1)
    print("Loading calculator %79")
    time.sleep(1)
    print("Loading calculator %100")
    time.sleep(1)
    print("El lenguaje elegido no hacido posible cargarlo por el idioma default")
    print("====Bienvenido a====")
    print("====CalcuPy Beta V1====")
    print("© 2026  juandiegosoto33548")
    #si lo vas a modificar asegurese de cambiar juandiegosoto33548 por el suyo

    while True:
        # 1. Preguntar primero la operación
        opera = input("¿Suma, Resta, Multiplicar, Dividir o Salir?: ")

        # 2. Verificar si el usuario quiere terminar
        if opera == "Salir":
            print("¡Hasta luego!")
            break

        # 3. Pedir los números solo si va a realizar un cálculo
        if opera == "Suma" or opera == "Resta" or opera == "Multiplicar" or opera == "Dividir":
            num1 = float(input("Número 1: "))
            num2 = float(input("Número 2: "))

            if opera == "Suma":
                resultado = num1 + num2
                print(f"Resultado: {resultado}\n")
            elif opera == "Resta":
                resultado = num1 - num2
                print(f"Resultado: {resultado}\n")
            elif opera == "Multiplicar":
                resultado = num1 * num2
                print(f"Resultado: {resultado}\n")
            elif opera == "Dividir":
                # Validación para evitar el error de división por cero
                if num2 == 0:
                    print("Error: No se puede dividir entre cero.\n")
            else:
                resultado = num1 / num2
                print(f"Resultado: {resultado}\n")
        else:
            print("Operación no válida. Intenta de nuevo.\n")

print("Gracias probar la beta la terminare en algunos dias / Thanks for trying the beta; I'll finish it in a few days.")
