from decimal import Decimal

# one task

list_number = [12, 2.1, 31, 1.2, 5]
for num in list_number:
    result = num * 2
    print(f"{result}")


# two task

surname = input("Enter please list surname:")
title_surname = surname.title()
split_surname = title_surname.split()
sorted_surname = sorted(split_surname)
for surname in sorted_surname:
    print(surname)


# 3 task

enter_word = input("Enter word:")
for word in enter_word:
    if word == word.upper():
        print(word, end="")

# 4 task
temperatur = float(input("Enter temperature in Celsius:"))
result = (temperatur - 32) * 5 / 9
decimal_result = Decimal(str(result)).quantize(Decimal("0.1"))
print(decimal_result)