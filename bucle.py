import constantes as const
from funciones_3_4 import *
from funciones import *


def main():
        
    nombre_heroe = input("Name of the player:\n")
    nombre_enemigo = input("Name of the enemy:\n")

        
    hp_heroe = const.HP_HEROE_INICIAL
    hp_enemigo = const.HP_ENEMIGO_INICIAL
    pociones = const.POCIONES_INICIALES


    while not verificar_ganador(hp_heroe, hp_enemigo):
        
        mostrar_estado(nombre_heroe,hp_heroe,nombre_enemigo,hp_enemigo,pociones)
        
        hp_heroe, hp_enemigo, pociones = turno_jugador(hp_heroe,hp_enemigo,pociones)
        
        mostrar_estado(nombre_heroe,hp_heroe,nombre_enemigo,hp_enemigo,pociones)
        
        if hp_enemigo <= 0:
            print("\n¡VICTORY! The enemy has fallen.")
        else:
            hp_heroe, hp_enemigo = turno_enemigo(hp_heroe,hp_enemigo)
        
        if hp_heroe <= 0:
            print("\n¡YOU DIED!. \nGame Over.")
            



main()


    
