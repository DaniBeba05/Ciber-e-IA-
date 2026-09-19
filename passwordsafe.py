import module

intentos_maximos = 3
num_intentos = 0



while module.comprobar_num_intentos(num_intentos,intentos_maximos):

    password = module.introducirpassword()

    if module.tiene_longitud_maxima(password):

        if not module.tiene_una_mayuscula(password):

            print(module.mensajerequisitomayuscula())

        elif not module.tiene_un_numero(password):

            print(module.mensajerequisitonumero())

        elif not module.tiene_un_simbolo(password):

            print(module.mensajerequisitosimbolo())


        if module.comprobar_password_valida(password):
            break


        num_intentos = module.sumar_num_intentos(num_intentos)

        if not module.comprobar_num_intentos(num_intentos,intentos_maximos):
            print(module.mensajedesuperaciondeintentos())

    else:


        print(module.mensajerequisitonumcaracteres())
        num_intentos = module.sumar_num_intentos(num_intentos)

        if not module.comprobar_num_intentos(num_intentos,intentos_maximos):
            print(module.mensajedesuperaciondeintentos())


if (module.comprobar_password_valida(password)):
    print (module.mensajedepasswordvalida())
