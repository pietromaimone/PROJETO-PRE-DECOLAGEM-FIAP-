def calcular_autonomia(
    capacidade_total_kwh: float,
    carga_atual_percentual: float,
    consumo_decolagem_kwh: float,
    perdas_kwh: float,
) -> tuple[float, float]:

    if capacidade_total_kwh <= 0:
        raise ValueError("capacidade_total_kwh precisa ser maior que zero")

    energia_disponivel = capacidade_total_kwh * (carga_atual_percentual / 100)
    energia_restante = energia_disponivel - consumo_decolagem_kwh - perdas_kwh
    percentual_restante = (energia_restante / capacidade_total_kwh) * 100

    return energia_restante, percentual_restante


def exibir_analise_cenario(cenario: dict, resultado: dict):

    print("\n=== ANÁLISE ENERGÉTICA ===")
    print(f"Cenário Selecionado:     {cenario['id']}")
    print(f"Capacidade Total:        {cenario['capacidade_total_kwh']:.2f} kWh")
    print(f"Carga Inicial:           {cenario['nivel_energia']:.1f}%")
    print(f"Consumo Decolagem:       {cenario['consumo_decolagem_kwh']:.2f} kWh")
    print(f"Perdas Estimadas:        {cenario['perdas_kwh']:.2f} kWh")
    print("-" * 40)
    print(f"Energia Restante:        {resultado['energia_restante_kwh']:.2f} kWh")
    print(f"Autonomia Pós-Decolagem: {resultado['energia_restante_percentual']:.2f}%")
