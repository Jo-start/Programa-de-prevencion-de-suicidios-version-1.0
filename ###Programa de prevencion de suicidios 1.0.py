###Programa de prevencion de suicidios 1.0###
###Creador Jo-start###
def saludo():
    nombre = input("Como te llamas amigo")
    print(f"Hola {nombre}, yo me llamo sep")
    return nombre
def revisar_animo(nombre):
    estado_animo = input(f"Bueno {nombre}, dime como te sientes hoy, bien, excelente, mal, triste, otra cosa")
    if estado_animo == "bien":
        print("Me da mucho gusto que te sientas espero que te la estes pasando bien este dia :)")
    elif estado_animo == "excelente":
        print("Uff que maravilloso ojala y haya sido uno de tus mejores dias sigue con tu onda :)")
    elif estado_animo == "mal":
        print("Tranquilo nos pasa a todos un dia hize un examen y reprobe por 1 decima nada mas :)")
    elif estado_animo == "triste":
        print("Si lo se hay cosas que nos puedan hacer sentir mal pero hay que afrontarlas para seguir con onda")
    elif estado_animo == "otra cosa":
        print("Sea lo que sea piensa en lo que vas hacer y si afectaras a alguien")
    else:
        print(f"Elige algo valido porfavor {nombre}")
    return estado_animo

nombre = saludo()
estado_animo = revisar_animo(nombre)
def menu_emergencias():
    print("MENU DE EMERGENCIAS")
    print("\n1. Necesito ayuda ahora \n2. Hablar con alguien de confianza \n3. Linea de ayuda")
    eleccion = input("Si necesitas alguna de estas opciones porfavor elige el numero que necesitas:")
    if eleccion == "1":
        print("Si estas en peligro ahora porfavor pidele ayuda a un adulto de confianza cerca de ti si no porfavor llama a los servicios de emergencia de tu zona")
    elif eleccion == "2":
        print("Porfavor habla con alguna de estas personas:")
        print("\n1. Padres \n2. Algun familiar \n3. Profesor \n4. Algun adulto de confianza")
    elif eleccion == "3":
        print("Porfavor llama a este numero: 8009112000 #Atencion gratuita")

if estado_animo == "mal" or estado_animo == "triste" or estado_animo == "otra cosa":
    menu_emergencias()




