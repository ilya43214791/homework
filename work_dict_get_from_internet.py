import requests
from pprint import pprint

url = 'https://dummyjson.com/users'

respon = requests.get(url)

data = respon.json()

user_live_in_Louisville = []
len_user = []
user_age = []
all_user = data["users"]
for user in all_user:
    user_hair = user["hair"]
    hair_color = user_hair['color']
    if user["gender"] == "male" and hair_color == "Brown":
        user_list = user
        user_age_list = user_list["age"]
        user_age.append(user_age_list)
        len_user.append(user_list)
    adreses_user = user["address"]
    if adreses_user["city"] == 'Louisville':
        user_list_adress = user
        reesult_user_list_adress = user_list_adress['firstName']
        add_user_in_adress = user_live_in_Louisville.append(reesult_user_list_adress)

len_total_user = (len(len_user))
sum_user = sum(user_age)
total_sum_user = sum_user / len_total_user
around_total_sum_user = round(total_sum_user)
print(f"середній вік чоловіків з Brown волоссям {around_total_sum_user}")
print(f'Список людей які проживають в населеному пункті "Louisville": {user_live_in_Louisville} ')
