def enter_positiv_number(number: int) -> list:
    if number < 1:
        raise ValueError

    list = [number + numbers for numbers in range(10)]
    return list


print(enter_positiv_number(number=12))
