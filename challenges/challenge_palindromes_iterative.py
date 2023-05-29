def is_palindrome_iterative(word):
    if len(word) == 0 or not isinstance(word, str):
        return False

    char_left, char_right = 0, -1
    mid_position = len(word) // 2
    for i in range(char_left, mid_position):  # O(n)
        if word[char_left + i] != word[char_right - i]:
            return False

    return True
