# Problema:
# Descobrir o horário que tem a maior quantidade de pessoas acessando a plataforma
# Dados: Tuple(horário de entrada, horario de saída) -> permanece_period
# Estratégia: Força bruta

# verificar se o horário de entrada é menor ou igual ao target_time
# ou se o horário de saída é maior ou igual ao target_time
# se verdadeiro, counter += 1
# retornar counter


def study_schedule(permanence_period, target_time):
    """
    Inputs:
    permanence_period: list[tuple[int, int]]
    target_time: int

    Output:
    counter: int
    """
    if target_time is None:
        return None

    counter = 0
    for login_time, logout_time in permanence_period:
        if not (isinstance(login_time, int) and isinstance(logout_time, int)):
            return None

        if login_time <= target_time <= logout_time:
            counter += 1

    return counter
