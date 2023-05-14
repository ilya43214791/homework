city_visit = input("Enter the cities you have already visited, separated by a space:").title()
city_not_visit = input("Enter сities you want to visit within 10 years:").title()
city_visit_split = city_visit.split()
city_not_visit_split = city_not_visit.split()
city_visit_set = set(city_visit_split)
city_not_visit_set = set(city_not_visit_split)
city_repid_items_origin = str(city_visit_set & city_not_visit_set).replace("{","").replace("}","")
city_repid_items = bool(city_visit_set & city_not_visit_set)
if city_repid_items == True:
    print("You alredy visit thisis city:" + str(city_repid_items_origin))
else:
    print("new cities are open to you")