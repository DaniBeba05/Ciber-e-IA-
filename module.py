def tiene_longitud_maxima (contraseña, minimo = 12 ):
    longitud_maxima = False
    if len(contraseña) >= minimo: 
        longitud_maxima = True

    return longitud_maxima



def tiene_una_mayuscula (contraseña):
    
    return any(caracter.isupper() for caracter in contraseña)



def tiene_un_numero (contraseña):
   
    return any (caracter.isdigit() for caracter in contraseña)




def tiene_un_simbolo (contraseña):

    simbolos = '.,@#?!>;:-_'

    return any(caracter in simbolos for caracter in contraseña)




def comprobar_num_intentos(num_intentos, intentos_maximos):

    return num_intentos < intentos_maximos



def sumar_num_intentos (num_intentos):

    return num_intentos + 1



def comprobar_password_valida(password):

 return (tiene_longitud_maxima(password) and tiene_una_mayuscula(password) and tiene_un_numero(password) and tiene_un_simbolo(password))


def mensajedepasswordvalida():
         
    return "La contraseña introducida es valida"




def mensajedesuperaciondeintentos():

    return "Has superado el número de intentos posibles. Vuelve a intentarlo más tarde"




def mensajerequisitomayuscula():

    return "Compruebe si su contraseña cumple los requisitos de tener al menos una mayúscula"



def mensajerequisitonumero():

    return "Compruebe si su contraseña cumple los requisitos de tener al menos un número"



def mensajerequisitosimbolo():

    return "Compruebe si su contraseña cumple los requisitos de tener al menos un simbolo"



def mensajerequisitonumcaracteres():

    return "Compruebe si su contraseña cumple los requisitos de tener al menos 12 carácteres"



def introducirpassword():

    password = str (input("Password:"))

    return password

