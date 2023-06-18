"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
#    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    #   g = [i ** 2 for i in numbers]
    return [i ** 2 for i in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(nums, state):
    print(state)
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

#    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
#   >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if state == ODD:
        return [i for i in nums if i % 2 != 0]
    elif state == EVEN:
        return [i for i in nums if i % 2 == 0]
    elif state == PRIME:
        res = []
        for i in nums:
            if i <= 1:
                print ('Incorrect nums', i)
            else:
                counter = 0
                i_list = list(range(2, i))
                for n in i_list:
                    g = i / n
                    chk = float(g).is_integer()
                    if chk is True:
                        counter = counter + 1
                if counter == 0:
                    res.append(i)
        return res

