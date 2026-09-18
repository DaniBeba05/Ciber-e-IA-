def marcar_entrada (lista, nombre):
    cambioentrada = False

    for indicador in lista: 
        if indicador ["nombre"] == nombre:
            indicador["entrada"] = True
            cambioentrada = True
            
        else: 
            cambioentrada = False
            indicador["entrada"] = False

    if (cambioentrada):
        return "El cambio ha sido satisfactorio y la persona se encuentra en nuestra lista"
    else: 
        return "El cambio no se ha podido realizar debido a que la persona no se encuentra en nuestra lista" 


asistentes = [
    {"nombre": "Ana", "entrada": False},
    {"nombre": "Luis", "entrada": False},
    {"nombre": "Jesus", "entrada": False},
]

print (marcar_entrada(asistentes, "Jesus"))