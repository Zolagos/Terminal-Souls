import random

HP_HEROE_INICIAL   = 100
HP_ENEMIGO_INICIAL = 120
POCIONES_INICIALES = 3
HP_CURACION_HEROE  = 20
HP_CURACION_ENEMIGO = 25   # curación de la IA enemiga
PROB_CRITICO       = 0.10  # 10 % de crítico
UMBRAL_CURACION_IA = 0.20

# ─────────────────────────────────────────
#  1. generar_daño
# ─────────────────────────────────────────
def generar_daño(min_dmg: int, max_dmg: int) -> int:
    """Retorna un daño aleatorio dentro del rango [min_dmg, max_dmg]."""
    return random.randint(min_dmg, max_dmg)


# ─────────────────────────────────────────
#  DESAFÍO EXTRA – Sistema de Críticos
# ─────────────────────────────────────────
def aplicar_critico(daño: int) -> tuple[int, bool]:
    """
    Con un 10 % de probabilidad duplica el daño.
    Retorna (daño_final, fue_critico).
    """
    if random.random() < PROB_CRITICO:
        return daño * 2, True
    return daño, False


# ─────────────────────────────────────────
#  2. mostrar_estado
# ─────────────────────────────────────────
def barra_vida(hp_actual: int, hp_max: int, largo: int = 20) -> str:
    """Genera una barra visual del estilo [####----]."""
    hp_actual = max(0, hp_actual)
    llenos = round((hp_actual / hp_max) * largo)
    vacios = largo - llenos
    return f"[{'█' * llenos}{'─' * vacios}]"


def mostrar_estado(nombre_h: str, hp_h: int, nombre_e: str, hp_e: int,
                   pociones: int) -> None:
    """Imprime en pantalla la vida actual de ambos combatientes.""" 
    print("\n" + "═" * 50)
    print(f"  ⚔️  {'ESTADO DEL COMBATE':^44}  ⚔️")
    print("═" * 50)

    # Héroe
    bh = barra_vida(hp_h, HP_HEROE_INICIAL)
    print(f"  🧙 {nombre_h:<12} HP: {max(0,hp_h):>3}/{HP_HEROE_INICIAL}  {bh}")
    print(f"     🧪 Pociones: {pociones}")

    # Enemigo
    be = barra_vida(hp_e, HP_ENEMIGO_INICIAL)
    print(f"  👹 {nombre_e:<12} HP: {max(0,hp_e):>3}/{HP_ENEMIGO_INICIAL}  {be}")
    print("═" * 50)

