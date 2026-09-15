from analise_energetica import exibir_analise_cenario
from processar_csv import processar_todos, ler_cenarios, buscar_cenario, avaliar_cenario

NOME_ARQUIVO_CSV = "banco_de_dados_real.csv"


def escolher_cenario(cenarios):
    while True:
        numero = input("Qual cenário da nave (1 a 100)? ").strip()

        if not numero.isdigit():
            print("Digite apenas números, por exemplo: 7")
            continue

        cenario = buscar_cenario(cenarios, numero)

        if cenario is None:
            print(f"Cenário 'cenario_{numero}' não existe no CSV. Tente outro número.")
            continue

        return cenario


def analise_energetica_por_cenario():
    resposta = (
        input("\nGostaria de fazer uma análise energética? (sim/não): ").strip().lower()
    )
    if resposta != "sim":
        return

    cenarios = ler_cenarios(NOME_ARQUIVO_CSV)
    cenario = escolher_cenario(cenarios)
    resultado = avaliar_cenario(cenario)

    if resultado["pode_decolar"]:
        exibir_analise_cenario(cenario, resultado)
    else:
        print(f"\nA nave não está pronta para decolagem! Motivo: {resultado['motivo']}")


def main():
    print("=== SISTEMA DE VERIFICAÇÃO DE DECOLAGEM ===\n")
    processar_todos(NOME_ARQUIVO_CSV)
    analise_energetica_por_cenario()


if __name__ == "__main__":
    main()
