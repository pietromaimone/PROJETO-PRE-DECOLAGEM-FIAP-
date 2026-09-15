import csv
from verificacao import verificar_decolagem
from analise_energetica import calcular_autonomia


def converter_linha(linha):

    valor_controle = linha.get("controle", linha.get("CONTROLE", ""))

    return {
        "id": linha["cenario_id"],
        "temperatura_interna": float(linha["temperatura_interna"]),
        "temperatura_externa": float(linha["temperatura_externa"]),
        "integridade_estrutural": int(linha["integridade_estrutural"]),
        "nivel_energia": float(linha["nivel_de_energia"].replace("%", "")),
        "pressao_tanques": float(linha["pressao_dos_tanques"]),
        "status_navegacao": int(linha["status_navegacao"]),
        "status_comunicacao": int(linha["status_comunicacao"]),
        "status_propulsao": int(linha["status_propulsao"]),
        "status_suporte_vida": int(linha["status_lifesuport"]),
        "capacidade_total_kwh": float(linha["capacidade_total_kwh"]),
        "consumo_decolagem_kwh": float(linha["consumo_decolagem_kwh"]),
        "perdas_kwh": float(linha["perdas_kwh"]),
        "controle": valor_controle.strip().upper(),
    }


def ler_cenarios(caminho_csv):

    with open(caminho_csv, newline="", encoding="utf-8") as arquivo:
        return [converter_linha(linha) for linha in csv.DictReader(arquivo)]


def avaliar_cenario(cenario):

    pode_decolar, motivo = verificar_decolagem(
        cenario["temperatura_interna"],
        cenario["temperatura_externa"],
        cenario["integridade_estrutural"],
        cenario["nivel_energia"],
        cenario["pressao_tanques"],
        cenario["status_navegacao"],
        cenario["status_comunicacao"],
        cenario["status_propulsao"],
        cenario["status_suporte_vida"],
    )

    gabarito_pode_decolar = cenario["controle"] == "TRUE"

    resultado = {
        "id": cenario["id"],
        "pode_decolar": pode_decolar,
        "motivo": motivo,
        "acertou": pode_decolar == gabarito_pode_decolar,
        "energia_restante_kwh": None,
        "energia_restante_percentual": None,
    }

    if pode_decolar:
        energia_restante_kwh, energia_restante_percentual = calcular_autonomia(
            cenario["capacidade_total_kwh"],
            cenario["nivel_energia"],
            cenario["consumo_decolagem_kwh"],
            cenario["perdas_kwh"],
        )
        resultado["energia_restante_kwh"] = energia_restante_kwh
        resultado["energia_restante_percentual"] = energia_restante_percentual

    return resultado


def imprimir_relatorio(resultados):

    print(f"{'Cenário':<15}{'Resultado':<22}{'Autonomia':<20}{'Gabarito'}")
    print("-" * 75)

    for r in resultados:
        resultado = "PRONTO PARA DECOLAR" if r["pode_decolar"] else "DECOLAGEM ABORTADA"
        marca = "OK" if r["acertou"] else "!! DIVERGE"

        if r["pode_decolar"]:
            autonomia = f"{r['energia_restante_kwh']:.0f} kWh ({r['energia_restante_percentual']:.0f}%)"
        else:
            autonomia = "—"

        print(f"{r['id']:<15}{resultado:<22}{autonomia:<20}{marca}")

    total = len(resultados)
    prontos = sum(1 for r in resultados if r["pode_decolar"])
    acertos = sum(1 for r in resultados if r["acertou"])

    print("-" * 75)
    print(f"Total de cenários:        {total}")
    print(f"Prontos para decolar:     {prontos}")
    print(f"Decolagens abortadas:     {total - prontos}")
    print(f"Acertos vs. gabarito:     {acertos}/{total}")


def buscar_cenario(cenarios, numero):

    cenario_id = f"cenario_{numero}"
    for cenario in cenarios:
        if cenario["id"] == cenario_id:
            return cenario
    return None


def processar_todos(caminho_csv):

    cenarios = ler_cenarios(caminho_csv)
    resultados = [avaliar_cenario(c) for c in cenarios]
    imprimir_relatorio(resultados)


if __name__ == "__main__":
    processar_todos("banco_de_dados_real.csv")
