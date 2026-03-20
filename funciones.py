import random

HP_HEROE_INICIAL   = 100
HP_CURACION_HEROE  = 20
POCIONES_INICIALES = 3
HP_ENEMIGO_INICIAL = 120
"""



HP_CURACION_ENEMIGO = 25   # curación de la IA enemiga
PROB_CRITICO       = 0.10  # 10 % de crítico
UMBRAL_CURACION_IA = 0.20

"""


def turno_jugador():
    accion = input("¿Que desea hacer?:\n 1.Atacar\n 2.Curar\n 3.Habilidad especial\n")
    accion = accion.lower().strip()
    if accion == "atacar":
        daño = generar_daño(10, 25)
        HP_ENEMIGO_INICIAL -= daño
        print(f"El heroe golpea por {daño} de daño")
    elif accion == "curar":
        if HP_CURACION_HEROE == 100:
            print("No se puede curar, la vida esta completa")
            turno_jugador()
        else:
            if POCIONES_INICIALES > 0:
                HP_HEROE_INICIAL = HP_HEROE_INICIAL + HP_CURACION_HEROE
                print()
            else:
                print("No te puedes curar, no hay pociones disponibles")
                turno_jugador() 
    elif accion == "habilidad especial":
        daño = generar_daño(30,50)
        if random.random() >= 0.5:
            daño = 0
    
    

                

def turno_enemigo():
    daño = generar_daño(15, 20)
    HP_HEROE_INICIAL -= daño
    

def verificar_ganador(HP_HEROE_INICIAL, HP_ENEMIGO_INICIAL):
    if (HP_HEROE_INICIAL <= 0) or (HP_ENEMIGO_INICIAL <= 0):
        return True
    else:
        return False

def generar_daño(min, max):
    daño = random.randint(min, max)
    return daño

#def mostrar_estado(nombre_h, HP_HEROE_INICIAL, nombre_e, HP_ENEMIGO_INICIAL):