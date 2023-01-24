def efficient_check_sum_in_list(target: int, int_list: list) -> list:  # Assume the list has no duplicate values
    index_dict = {}
    pairs = []

    for i, n in enumerate(int_list):
        if n in index_dict:
            pairs.append((i, index_dict[n]))

        required_pair = target - n

        if required_pair in index_dict:
            index_dict[required_pair] = i

        else:
            index_dict[required_pair] = i

    return pairs


print(efficient_check_sum_in_list(10, [1, 9, 5, 3, -55, -55, -55, 3, 65, 4]))