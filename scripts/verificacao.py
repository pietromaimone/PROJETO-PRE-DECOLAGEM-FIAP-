TEMPERATURA_INTERNA_MIN = 18
TEMPERATURA_INTERNA_MAX = 35

TEMPERATURA_EXTERNA_MIN = -120
TEMPERATURA_EXTERNA_MAX = 50

NIVEL_ENERGIA_MIN = 70

PRESSAO_TANQUES_MIN = 30
PRESSAO_TANQUES_MAX = 40

OK = 1


def verificar_decolagem(
    temperatura_interna,
    temperatura_externa,
    integridade_estrutural,
    nivel_energia,
    pressao_tanques,
    status_navegacao,
    status_comunicacao,
    status_propulsao,
    status_suporte_vida,
):

    modulos_criticos = [
        status_navegacao,
        status_comunicacao,
        status_propulsao,
        status_suporte_vida,
    ]

    if not (TEMPERATURA_INTERNA_MIN <= temperatura_interna <= TEMPERATURA_INTERNA_MAX):
        return False, "temperatura interna fora do limite"

    if not (TEMPERATURA_EXTERNA_MIN <= temperatura_externa <= TEMPERATURA_EXTERNA_MAX):
        return False, "temperatura externa fora do limite"

    if integridade_estrutural != OK:
        return False, "integridade estrutural comprometida"

    if nivel_energia < NIVEL_ENERGIA_MIN:
        return False, "nível de energia insuficiente"

    if not (PRESSAO_TANQUES_MIN <= pressao_tanques <= PRESSAO_TANQUES_MAX):
        return False, "pressão dos tanques fora do limite"

    if any(status != OK for status in modulos_criticos):
        return False, "algum módulo crítico com falha"

    return True, "pronto para decolar"
