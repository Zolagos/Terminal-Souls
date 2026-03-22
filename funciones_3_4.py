import random
import constantes as const
from funciones import generar_daño,aplicar_critico


def turno_jugador(hp_heroe,hp_enemigo,pociones):
    accion = input("Write the action:\n 1.Attack\n 2.Heal\n 3.Special ability\n")
    accion = accion.lower().strip()
    if accion == "attack":
        daño = generar_daño(10, 25)
        hp_enemigo -= daño
        print(f"¡The hero deals {daño} points of damage!")
    elif accion == "heal":
        if hp_heroe == 100:
            print("Can't heal, the health is complete")
            hp_heroe, hp_enemigo, pociones = turno_jugador(hp_heroe,hp_enemigo,pociones)
        else:
            if pociones > 0:
                hp_heroe += const.HP_CURACION_HEROE
                pociones -=1
                print(f"¡The hero heals {const.HP_CURACION_HEROE}!")
                if hp_heroe > 100:
                    hp_heroe = 100  
            else:
                print("Can't heal, no potions left")
                hp_heroe, hp_enemigo, pociones = turno_jugador(hp_heroe,hp_enemigo,pociones) 
    elif accion == "Special ability":
        daño = generar_daño(30,50)
        if random.random() >= 0.5:
            daño = 0
            print("¡The hero has used the special ability and failed!")

        print(f"¡The hero deals {daño} points of damage!")
        hp_enemigo -= daño
    else:
        print("¡Invalid action!")
        hp_heroe, hp_enemigo, pociones = turno_jugador(hp_heroe,hp_enemigo,pociones) 
        
    return hp_heroe,hp_enemigo,pociones

    
def turno_enemigo(hp_heroe,hp_enemigo):

    if (hp_enemigo/const.HP_ENEMIGO_INICIAL) <= const.UMBRAL_CURACION_IA:
        hp_enemigo += const.HP_CURACION_ENEMIGO
        print(f"¡The enemy heals {const.HP_CURACION_ENEMIGO}!")
    else:
        daño = generar_daño(15, 20)
        print(f"¡The enemy deals {daño} points of damage!")
        hp_heroe -= daño
    return hp_heroe, hp_enemigo
    

def verificar_ganador(HP_HEROE_INICIAL, HP_ENEMIGO_INICIAL):
    if (HP_HEROE_INICIAL <= 0) or (HP_ENEMIGO_INICIAL <= 0):
        return True
    else:
        return False

