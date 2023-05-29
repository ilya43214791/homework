# 1
# def get_num(number: int):
#     if number == 1:
#         anicdot_schol = "Юро, скільки твоя мама повинна заплатити за 2 кілограми яблук, якщо 1 кг коштує 10 гривень?Не можу сказати, учителю, моя мама завжди торгується."
#         return anicdot_schol
#     elif number == 2:
#         anicdot_fish = "Дядьку, а риба клює? Ні, вона тільки натякає. Як це?А ось так. Поплавець веде, веде, а потім морду з води висуне і каже: Вибачте, що потурбувалa"
#         return anicdot_fish
#     else:
#         anicdot_cat =  "Захотілося уваги, любові, ласки...Непогодуй кота!"
#         return anicdot_cat
#
#
# user_input = int(input("Enter number get anicdot:"))
# print(get_num(number=user_input))

# 2
# def get_length_width_rectangle(length: int|float, width:int|float) -> float:
#     perimetr = (length + width)*2
#     perimetr_float = float(perimetr)
#     return perimetr_float
#
# user_input_length = int(input("Enter length rectangle:"))
# user_input_width = int(input("Enter width rectangle:"))
# print(get_length_width_rectangle(length=user_input_length,width=user_input_width))


# # 3
# def del_liter_str(string: str) -> str:
#     replace_word = string.replace('ї',"").replace("ж","").replace('Ї',"").replace("Ж","")
#         return replace_word
#
# user_input_str = str(input("Enter word:"))
# print(del_liter_str(string=user_input_str))

# def del_liter_str(string: str, string_two: str):
#     for value in set(string_two):
#         print(value)
#         string = string.replace(value.lower(), "").replace(value.upper(),"")
#     return string
#
# user_input_str = 'вікно'
# user_input_str_1 = 'вОоооооооооооооооооооооооно'
# print(del_liter_str(string=user_input_str, string_two=user_input_str_1))
