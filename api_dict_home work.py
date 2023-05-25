import requests

url = 'https://script.google.com/macros/s/AKfycbyoM2WaGUIes2nAxDO01c346hf2zaIB3A-R7RU5BZjXhaSE58BVLdBRU8ujSQ6WZHFv/exec'

respon = requests.get(url)

data = respon.json()["data"]

items_gluten = []
new_list_value_price = []
for value in data:
    value_data = value["price"]
    float_value_data = float(value_data)
    if float_value_data:
        new_list_value_price.append(float_value_data)
    if value['gluten']:
        list_bool = value['gluten']
        items_gluten.append(list_bool)

sum_new_list_value_price = sum(new_list_value_price)
round_sum = round(sum_new_list_value_price, 2)
len_items_gluten = len(items_gluten)
print(f"Сума цін товарів = {round_sum}")
print(f"Кількість товарів з глютеном:{len_items_gluten}")
