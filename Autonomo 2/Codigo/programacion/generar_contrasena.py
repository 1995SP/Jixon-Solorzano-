import random
import string

def generar_contrasena():
    print("________________________________________")
    print("    GENERADOR SEGURO DE CONTRASEÑAS      ")
    print("________________________________________")
    
    # Se repite infinitamente hasta que el usuario ingrese un número válido (>= 8).
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))
            if longitud >= 8:
                break  # Rompe el bucle si la condición se cumple exitosamente
            else:
                print("Error: Por seguridad, la longitud debe ser mayor o igual a 8.\n")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.\n")

    print("\n--- Configuración de Seguridad ---")
    incluir_mayus = input("¿Desea incluir letras mayúsculas? (S/N): ").strip().upper()
    incluir_num = input("¿Desea incluir números? (S/N): ").strip().upper()
    incluir_sym = input("¿Desea incluir símbolos especiales? (S/N): ").strip().upper()

    # Base por defecto: la contraseña siempre tendrá letras minúsculas
    banco_caracteres = string.ascii_lowercase
    # Si el usuario responde 'S', se concatenan los nuevos grupos de caracteres.
    if incluir_mayus == "S":
        banco_caracteres += string.ascii_uppercase

    if incluir_num == "S":
        banco_caracteres += string.digits

    if incluir_sym == "S":
        banco_caracteres += string.punctuation

    #Construcción de la contraseña segura, un segundo bucle selecciona caracteres al azar del banco definitivo
    contrasena_generada = ""
    for _ in range(longitud):
        caracter_aleatorio = random.choice(banco_caracteres)
        contrasena_generada += caracter_aleatorio

    print("\n________________________________________")
    print(f"Su contraseña segura generada es: {contrasena_generada}")
    print("________________________________________")


if __name__ == "__main__":
    generar_contrasena()