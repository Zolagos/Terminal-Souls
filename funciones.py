import random
import constantes as const


# ─────────────────────────────────────────
#  1. generar_daño
# ─────────────────────────────────────────
def generar_daño(min_dmg: int, max_dmg: int) -> int:
    """Retorna un daño aleatorio dentro del rango [min_dmg, max_dmg]."""
    daño = random.randint(min_dmg, max_dmg)
    daño = aplicar_critico(daño)
    return daño


# ─────────────────────────────────────────
#  DESAFÍO EXTRA – Sistema de Críticos
# ─────────────────────────────────────────
def aplicar_critico(daño: int) -> int:
    """
    Con un 10 % de probabilidad duplica el daño.
    Retorna daño_final.
    """
    if random.random() < const.PROB_CRITICO:
        print("¡CRITICAL HIT!")
        daño = daño * 2
        
    return daño

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
    print(f"  ⚔️  {'COMBAT STATUS':^44}  ⚔️")
    print("═" * 50)

    # Héroe
    bh = barra_vida(hp_h, const.HP_HEROE_INICIAL)
    print(f"  🧙 {nombre_h:<12} HP: {max(0,hp_h):>3}/{const.HP_HEROE_INICIAL}  {bh}")
    print(f"     🧪 Potions: {pociones}")

    # Enemigo
    be = barra_vida(hp_e, const.HP_ENEMIGO_INICIAL)
    print(f"  👹 {nombre_e:<12} HP: {max(0,hp_e):>3}/{const.HP_ENEMIGO_INICIAL}  {be}")
    print("═" * 50)