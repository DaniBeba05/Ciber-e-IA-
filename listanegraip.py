def comprobaracceso (lista, ip):
    acceso = False
    for variable in lista: 
        if ip == variable:
            acceso = False
        else: 
            acceso = True

    if (acceso):
        return "El acceso es: ", acceso, " = permitido "
    else: 
        return "El acceso es: ", acceso, " = denegado "

    



lista_negra = ["192.168.1.5", "10.0.0.2", "8.8.8.8", "192.164.5.0"]
print (comprobaracceso(lista_negra,"192.168.1.6"))