def add_two_numbers(n1: int, n2: int) -> int:
    """

    :param n1: First number to add
    :param n2: Second number to add
    :return: Wow! it is n1+n2!
    """
    return n1 + n2


if __name__ == '__main__':
    num1 = int(input('Первое число: '))
    num2 = int(input('Второе число: '))
    print('Сумма', add_two_numbers(num1, num2))
