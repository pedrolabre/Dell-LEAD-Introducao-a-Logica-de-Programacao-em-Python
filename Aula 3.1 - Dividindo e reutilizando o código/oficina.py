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


input("\nPressione Enter para encerrar...")
