from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    rez = list(map(lambda d: {k: (v if k != "name" else v.title()) for (k, v) in d.items()}, data))
    return rez


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    rez = list(map(lambda d: {k: v for (k, v) in d.items() if k not in redundant_keys}, data))
    return rez


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    rez = list(filter(lambda d: {k: v for (k, v) in d.items() if v == value}, data))
    return rez


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    return min(data, default=None)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the shorter string
    """
    # optimal solution
    rez = min(data, default=None, key=lambda x: (len(str(x))))
    return str(rez) if rez is not None else None

    # !! by using list comprehension

    # if not data:
    #     return None
    # else:
    #     all_el_to_str = [str(el) for el in data]
    #     all_length = [len(el) for el in all_el_to_str]
    #     rez = [el for el in all_el_to_str if len(el) == min(all_length)]
    #     rez_to_str = ''.join(str(e) for e in rez)
    #     return rez_to_str

    # !! solution by using cycles

    # if not data:
    #     return None
    # else:
    #     data_to_str = []
    #     for i in data:
    #         data_to_str.append(str(i))
    #     print(data_to_str)
    #     list_of_length = []
    #     for i in data_to_str:
    #         list_of_length.append(len(i))
    #     min_len = min(list_of_length)
    #     for i in data_to_str:
    #         if len(i) == min_len:
    #             return i


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    rez = min(
        filter(lambda x: key in x, data),
        key=lambda x: x[key]
    )
    return rez


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    rez = max([max(e) for e in data if len(e) > 0])
    return rez
    # rez_2 = list((lambda x: x[i] for i in data))
    # return rez_2


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data)


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    rez = sum(ord(x) for x in text)
    return rez


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """

    def prime(num):
        i = 2
        while i < num:
            j = 2
            while j <= (i / j):
                if not (i % j):
                    break
                j += 1
            if j > i / j:
                yield i
            i += 1

    for i in prime(200):
        yield i


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """
    import string
    import random

    list1 = list(string.ascii_lowercase)
    list2 = list1[:-6]
    res = random.sample(list2, len(list2))
    return res
