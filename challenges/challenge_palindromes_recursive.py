# - Objetivo:
# Determinar se a palavra (string) é um palíndromo.
# Ou seja, um conjunto de caracteres que é igual ao seu inverso.
# - Estratéria:
# Recursividade


def is_palindrome_recursive(word, low_index, high_index):
    """
    Inputs:
    word: str
    low_index: int
    high_index: int

    Output:
    bool
    """
    if not (isinstance(word, str) and len(word) > 0):
        return False
    if not (word[low_index] == word[high_index]):
        return False
    if (high_index - low_index) <= 1:
        return True

    return is_palindrome_recursive(word, (low_index + 1), (high_index - 1))
