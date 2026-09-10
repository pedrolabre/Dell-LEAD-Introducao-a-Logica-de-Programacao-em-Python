# Módulo de funções auxiliares de formatação de data e hora


def formatar_data(data):
    """Formata uma data para o padrão 'dd/mes/aaaa'.

    Recebe uma tupla no formato (ano, mês, dia), onde cada elemento é um número inteiro.
    Retorna uma string com o dia em dois dígitos, o mês representado por suas três
    letras iniciais em minúsculo por extenso e o ano com quatro dígitos.
    """
    ano, mes, dia = data
    meses = (
        'jan', 'fev', 'mar', 'abr', 'mai', 'jun',
        'jul', 'ago', 'set', 'out', 'nov', 'dez'
    )
    mes_extenso = meses[mes - 1]
    return "{:02d}/{}/{:04d}".format(dia, mes_extenso, ano)


def formatar_hora(horario):
    """Formata um horário para o padrão 'hh:mm' no formato de 24 horas.

    Recebe uma tupla no formato (hora, minuto), onde hora e minuto são inteiros.
    Retorna uma string com hora e minuto preenchidos com dois dígitos.
    """
    hora, minuto = horario
    return "{:02d}:{:02d}".format(hora, minuto)


# Módulo de filtragem e impressão de eventos


def imprimir_eventos(eventos, de_data=(1, 1, 1), ate_data=(9999, 12, 31)):
    """Filtra e imprime os eventos ocorridos em um intervalo de datas.

    Recebe:
        eventos (list): Lista de tuplas representando os eventos no formato
                        ((ano, mes, dia), (hora, minuto), 'descricao').
        de_data (tuple, opcional): Data inicial do intervalo (ano, mes, dia).
                                   Padrão: (1, 1, 1).
        ate_data (tuple, opcional): Data final do intervalo (ano, mes, dia).
                                    Padrão: (9999, 12, 31).

    Para cada evento dentro do intervalo especificado (de_data <= data <= ate_data),
    exibe uma linha formatada como:
    dd/mes/aaaa - hh:mm: Descricao do evento
    """
    for data, hora, descricao in eventos:
        if de_data <= data <= ate_data:
            data_formatada = formatar_data(data)
            hora_formatada = formatar_hora(hora)
            print("{} - {}: {}".format(data_formatada, hora_formatada, descricao))


# Dados da agenda de eventos
agenda = [
    ((2020, 1, 13), (11, 50), 'Renovar identidade'),
    ((2020, 1, 15), (16, 30), 'Fazer compras'),
    ((2020, 1, 25), (8, 45), 'Autenticar documentos'),
    ((2020, 2, 29), (14, 15), 'Prestar concurso'),
    ((2020, 3, 15), (17, 50), 'Buscar bolo pro aniversário da vovó'),
    ((2020, 3, 17), (13, 20), 'Consulta de revisão com dentista')
]

# Execução e testes de impressão com diferentes passagens de parâmetros
print("--- Sistema de Gerenciamento de Eventos da Agenda ---")

print("\n--- Eventos a partir de 20/01/2020 (data inicial posicional) ---")
imprimir_eventos(agenda, (2020, 1, 20))

print("\n--- Eventos até 15/03/2020 (data final nomeada) ---")
imprimir_eventos(agenda, ate_data=(2020, 3, 15))

print("\n--- Todos os eventos cadastrados (parâmetros padrão) ---")
imprimir_eventos(agenda)

print("\n--- Eventos no intervalo entre 15/01/2020 e 29/02/2020 ---")
imprimir_eventos(agenda, (2020, 1, 15), (2020, 2, 29))

input("\nPressione Enter para encerrar...")
