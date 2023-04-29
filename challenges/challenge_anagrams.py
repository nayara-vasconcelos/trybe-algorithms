# Ideias:

# 1)
# - Converter str para int com enumerate e binary search
# - Usar Quicksort para ordenar
# - Converter int para string novamente

# 2)
# - Usar ord para converter str em int baseado no ASCII
# - Usar Quicksort para ordenar
# - Usar chr para converter int para str baseado no ASCII

# 3)
# - Personalisar o Quicksort ordenar por compação de chars
#   usando busca binária para comparar chars
#   com base no índice do alfabeto ordenado


def quicksort(numbers, start, end):
    if len(numbers) <= 1:
        return numbers

    if start < end:
        partition_index = partition(
            numbers, start, end
        )  # elemento na posição ordenada
        quicksort(
            numbers, start, partition_index - 1
        )  # menores que o pivô à esquerda
        quicksort(
            numbers, partition_index + 1, end
        )  # maiores que o pivô à direita


def partition(numbers, start, end):
    pivot = numbers[end]  # útimo elemento da lista
    delimiter = start - 1

    for index in range(start, end):  # índice no elemento a ser comparado
        if numbers[index] <= pivot:
            delimiter = delimiter + 1
            numbers[index], numbers[delimiter] = (
                numbers[delimiter],
                numbers[index],
            )  # Todos que forem menor que o pivô ficarão a esquerda
    numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    # Converte str para lista de int (ASCII)
    first_str_to_int = [
        ord(char) for char in list(first_string.strip().lower())
    ]
    second_str_to_int = [
        ord(char) for char in list(second_string.strip().lower())
    ]

    # Ordena lista de int
    quicksort(first_str_to_int, 0, (len(first_str_to_int) - 1))
    quicksort(second_str_to_int, 0, (len(second_str_to_int) - 1))

    # Converte lista de int para str com base no ASCII
    first_string_ordered = "".join(
        [chr(number) for number in first_str_to_int]
    )
    second_string_ordered = "".join(
        [chr(number) for number in second_str_to_int]
    )

    is_equal = (
        False
        if (first_string == "" or second_string == "")
        else (first_string_ordered == second_string_ordered)
    )

    return (first_string_ordered, second_string_ordered, is_equal)
