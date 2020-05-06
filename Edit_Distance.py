"""
Given two strings, determine the edit distance between them.
The edit distance is defined as the minimum number of edits
(insertion, deletion, or substitution)
needed to change one string to the other.

For example, "biting" and "sitting"
have an edit distance of 2 (substitute b for s, and insert a t).
"""


def min_distance(first_string: 'str', second_string: 'str') -> 'int':
    """
    :return: number of operations need to be done to change first_string into second_string
    """
    memory_table = [[None for j in range(len(second_string) + 1)] for i in range(len(first_string) + 1)]

    def calculate_for_substring(sub_first_string: 'str', sub_second_string: 'str') -> 'int':
        """
        :param sub_first_string: part of first string
        :param sub_second_string: part of second string
        :return: number of operations need to be done to change sub_first_string into sub_second_string


        """
        if not sub_first_string:
            return len(sub_second_string)

        if not sub_second_string:
            return len(sub_first_string)

        if memory_table[len(sub_first_string)][len(sub_second_string)] is None:
            memory_table[len(sub_first_string)][len(sub_second_string)] = calculate_for_substring(sub_first_string[:-1],
                                                                                                  sub_second_string[:-1])
            if sub_first_string[-1] != sub_second_string[-1]:
                memory_table[len(sub_first_string)][len(sub_second_string)] = 1 + min(
                    memory_table[len(sub_first_string)][len(sub_second_string)],
                    calculate_for_substring(sub_first_string[:-1], sub_second_string),
                    calculate_for_substring(sub_first_string, sub_second_string[:-1]))

        return memory_table[len(sub_first_string)][len(sub_second_string)]

    return calculate_for_substring(first_string, second_string)


if __name__=='__main__':
    s1 = 'biting'
    s2 = 'sitting'
    print(min_distance(s1, s2))

