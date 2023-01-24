class CheckSumInList:
    def __init__(self, int_list: list, target: int):
        self.int_list = int_list
        self.target = target

    def no_duplicates(self) -> list:  # Assume the list has no duplicate values
        index_dict = {}
        pairs = []

        for i, n in enumerate(self.int_list):
            if n in index_dict:
                pairs.append((i, index_dict[n]))

            required_pair = self.target - n
            index_dict[required_pair] = i

        return pairs


print(CheckSumInList([1, 9, 8, 6, 2, -55, 10, 65], 10).no_duplicates())