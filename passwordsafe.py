def tiene_longitud_maxima (contraseña, minimo = 12 ):
    longitud_maxima = False
    if len(contraseña) >= minimo: 
        longitud_maxima = True

    return longitud_maxima

def tiene_una_mayuscula (contraseña):
    tiene_mayuscula = False

    if any(caracter.isupper() for caracter in contraseña):
        tiene_mayuscula = True

    return tiene_mayuscula

def tiene_un_numero (contraseña):
    tiene_numero = False
    if any(caracter.isdigit() for caracter in contraseña):
        tiene_numero = True

    return tiene_numero


def tiene_un_simbolo (contraseña):

    tiene_simbolo = False
    simbolos = '.,@#?!>;:-_'

    if any(caracter in simbolos for caracter in contraseña):
        tiene_simbolo = True

    return tiene_simbolo


def comprobar_num_intentos(num_intentos, intentos_maximos):

    return num_intentos < intentos_maximos



def sumar_num_intentos ():
    global num_intentos
    num_intentos = num_intentos +  1

    return num_intentos

def comprobar_password_valida ():
    passwordvalida = False

    if tiene_longitud_maxima(password) and tiene_una_mayuscula(password) and tiene_un_numero(password) and tiene_un_simbolo(password):
        passwordvalida = True

    return passwordvalida

password = str(input("Password:"))
intentos_maximos = 3
num_intentos = 0

while comprobar_num_intentos(num_intentos,intentos_maximos):

    if tiene_longitud_maxima(password):

        if tiene_una_mayuscula(password) == False:
            
            print("Compruebe si su contraseña cumple los requisitos de tener una mayuscula")

        elif tiene_un_numero(password) == False:
           
            print("Compruebe si su contraseña cumple los requisitos de tener un número")

        elif tiene_un_simbolo(password) == False:
            
            print("Compruebe si su contraseña cumple los requisitos de tener un símbolo")


        if comprobar_password_valida():
            break


        sumar_num_intentos()

        if comprobar_num_intentos(num_intentos, intentos_maximos):
            password = str(input("Password:"))
        else:
            print("Has superado el número de intentos posibles. Vuelve a intentarlo más tarde")

    else:
       

        print("Compruebe si su contraseña cumple los requisitos de 12 caracteres")
        sumar_num_intentos()

        if comprobar_num_intentos(num_intentos, intentos_maximos):
            password = str(input("Password:"))
        else:
            print("Has superado el número de intentos posibles. Vuelve a intentarlo más tarde")

if (comprobar_password_valida()):
    print ("La contraseña introducida es válida")
