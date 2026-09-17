password = str(input("Password:"))
passwordvalida = False
simbolos = '.,@#?!>;:-_'
num_intentos = 0
intentos_maximos = 3

while num_intentos < intentos_maximos:

    if len(password) >= 12: #Validación de si la contraseña tiene 12 carácteres

        passwordvalida = True

        for letter in password: #for para comprobar el resto de condiciones mientras el número de carácteres es 12.

            if letter.isdigit(): #comprobación de si tiene un número

                passwordvalida = True

            else: 
                passwordvalida = False

                print ("Compruebe si su contraseña cumple los requisitos de tener 12 caracteres")

                num_intentos+=1 

                if num_intentos < intentos_maximos:

                    password = str(input("Password:"))
                else: 
                    print ("Has superado el número de intentos posibles. Vuelve a intentarlo más tarde")
                    break


            if letter.isupper(): #comprobación de si tiene una mayúscula

                passwordvalida = True

            else:
                passwordvalida = False

                print ("Compruebe si su contraseña cumple los requisitos de una mayúscula")

                num_intentos+=1 

                if num_intentos < intentos_maximos:

                    password = str(input("Password:"))
                else: 
                    print ("Has superado el número de intentos posibles. Vuelve a intentarlo más tarde")
                    break    
                
               
            if any (letra in simbolos for letra in password): #comprobación de si tiene un simbolo

                passwordvalida = True

            else: 
                passwordvalida = False

                print ("Compruebe si su contraseña cumple los requisitos de 12 caracteres, una mayuscula y un símbolo")

                num_intentos+=1 

                if num_intentos < intentos_maximos:

                    password = str(input("Password:"))
                else: 
                    print ("Has superado el número de intentos posibles. Vuelve a intentarlo más tarde")
                    break


        if passwordvalida == True: 
            break
    else:
        passwordvalida = False 
        if num_intentos == 3: 
            print ("Has superado el numero de intentos máximos permitidos")

        print ("Compruebe si su contraseña cumple los requisitos de 12 caracteres, una mayuscula y un símbolo")
        num_intentos+=1 
        if num_intentos < intentos_maximos:
            password = str(input("Password:"))
        if num_intentos == 3: 
            print ("Has superado el numero de intentos máximos permitidos")


if passwordvalida == True:
    print ("Password valida")
