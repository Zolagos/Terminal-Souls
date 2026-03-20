import random

def turno_jugador():
    accion = input("¿Que desea hacer?:\n 1.Atacar\n 2.Curar\n 3.Habilidad especial")
    accion = accion.lower().strip()
    if accion == "atacar":
        daño = generar_daño(10, 25)
    elif accion == "curar":
        curar = 20
        if pociones > 0:
            hp_h = hp_h + curar
        else:
            print("No te puedes curar, no hay pociones disponibles")
            turno_jugador() 
    elif accion == "habilidad especial":
        daño = generar_daño(30,50)
        if random.random() >= 0.5:
            daño = 0
            

def turno_enemigo():
    daño = generar_daño(15, 20)
    
    

def verificar_ganador(hp_h, hp_e):
    if (hp_h <= 0) or (hp_e <= 0):
        return True
    else:
        return False

def generar_daño(min, max):
    daño = random.randint(min, max)
    return daño

def mostrar_estado(nombre_h, hp_h, nombre_e, hp_e):