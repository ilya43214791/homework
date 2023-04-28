name = input('enter your name:')
surname = input('enter your surname:')
big_surname = surname.upper().strip(' 0123456789')
first_one_name = name.capitalize().strip(' 0123456789')
len_object = len(first_one_name)
sum = f"Привіт, {first_one_name}  {big_surname} а ти знав, що твоє імя складється з {len_object} літер "
replace_str = sum.replace("Привіт","Здарова")
total = f"{replace_str} ?"
print(total)