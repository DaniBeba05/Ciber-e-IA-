password = str(input("Password:"))
passwordvalida = False
simbolos = '.,@#?!>;:-_'
num_intentos = 0
intentos_maximos = 3

while num_intentos < intentos_maximos:

    if len(password) >= 12:
        tiene_numero = False
        tiene_mayuscula = False
        tiene_simbolo = False

        for letter in password:

            if letter.isdigit():
                tiene_numero = True

            if letter.isupper():
                tiene_mayuscula = True

            if letter in simbolos:
                tiene_simbolo = True

        if tiene_numero == False:
            passwordvalida = False
            print("Compruebe si su contraseña cumple los requisitos de tener un numero")

        elif tiene_mayuscula == False:
            passwordvalida = False
            print("Compruebe si su contraseña cumple los requisitos de una mayúscula")

        elif tiene_simbolo == False:
            passwordvalida = False
            print("Compruebe si su contraseña cumple los requisitos de tener un símbolo")

        else:
            passwordvalida = True

        if passwordvalida == True:
            break

        num_intentos += 1

        if num_intentos < intentos_maximos:
            password = str(input("Password:"))
        else:
            print("Has superado el número de intentos posibles. Vuelve a intentarlo más tarde")

    else:
        passwordvalida = False

        print("Compruebe si su contraseña cumple los requisitos de 12 caracteres")
        num_intentos += 1

        if num_intentos < intentos_maximos:
            password = str(input("Password:"))
        else:
            print("Has superado el número de intentos posibles. Vuelve a intentarlo más tarde")

if (passwordvalida):
    print ("La contraseña introducida es válida")
