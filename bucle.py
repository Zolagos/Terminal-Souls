from funciones import *

HP_HEROE_INICIAL   = 100
HP_CURACION_HEROE  = 20
POCIONES_INICIALES = 3
HP_ENEMIGO_INICIAL = 120
"""



HP_CURACION_ENEMIGO = 25   # curación de la IA enemiga
PROB_CRITICO       = 0.10  # 10 % de crítico
UMBRAL_CURACION_IA = 0.20
"""



nombre_heroe = input("Nombre del jugador:\n")
nombre_enemigo = input("Nombre del enemigo:\n")
while not verificar_ganador(HP_HEROE_INICIAL, HP_ENEMIGO_INICIAL):

    turno_jugador()


    