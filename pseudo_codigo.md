## Pseudo codigo 

~~~text
INÍCIO
    ler temperatura_interna
    ler temperatura_externa
    ler integridade_estrutural
    ler nivel_energia
    ler pressao_tanques
    ler status_navegacao
    ler status_comunicacao
    ler status_propulsao
    ler status_suporte_vida

    se temperatura_interna < 18 ou temperatura_interna > 35 entao
        exibir "DECOLAGEM ABORTADA"
    senão se temperatura_externa < -120 ou temperatura_externa > 50 entao
        exibir "DECOLAGEM ABORTADA"
    senão se integridade_estrutural <> 1 entao
        exibir "DECOLAGEM ABORTADA"
    senão se nivel_energia < 70 entao
        exibir "DECOLAGEM ABORTADA"
    senão se pressao_tanques < 30 ou pressao_tanques > 40 entao
        exibir "DECOLAGEM ABORTADA"
    senão se algum modulo_critico <> "OK" entao
        exibir "DECOLAGEM ABORTADA"
    senão
        exibir "PRONTO PARA DECOLAR"
    fimse
FIM

~~~
