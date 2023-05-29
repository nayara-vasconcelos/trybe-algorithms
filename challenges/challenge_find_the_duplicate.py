def check_input(input):
    valid_input = (
        input is not None and isinstance(input, list) and len(input) > 1
    )
    if not valid_input:
        return False

    for element in input:  # O(n)
        valid_value = isinstance(element, int) and (element > 0)
        if not valid_value:
            return False

    return True


def find_duplicate(nums):
    if check_input(nums):
        ordered_nums = sorted(nums)  # O(n log n)
        for i in range(1, len(ordered_nums)):  # O(n)
            if ordered_nums[i - 1] == ordered_nums[i]:
                return ordered_nums[i - 1]

    return False
