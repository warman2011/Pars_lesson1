import requests
import time
import json

url_categories = "https://5ka.ru/api/v2/categories/" #URL с категориями товаров
url = "https://5ka.ru/api/v2/special_offers/"

response_categories = requests.get(url_categories) #Получаем категории товаров

for i in response_categories.json():#Перебираем категории товаров
    print(i)
    response = requests.get("https://5ka.ru/api/v2/special_offers/?categories=" + str(i['parent_group_code']) + "&ordering=&page=1&price_promo__gte=&price_promo__lte=&records_per_page=12&search=&store=")
    data = response.json()
    print(data["next"])
    with open(i["parent_group_name"]+ ".json","w", encoding="UTF-8") as file:
        json.dump(data["results"], file, ensure_ascii=False)
    if data["next"] ==None:
        continue
    a = 1
    result = []
    result.append(data["results"])
    while a == 1:
        response = requests.get(data["next"])
        data = response.json()
        result.append(data["results"])
        print(data["next"])
        if data["next"] == None:
            with open(i["parent_group_name"] + ".json", "w", encoding="UTF-8") as file:
                json.dump(result, file, ensure_ascii=False)
            a = 0
        time.sleep(1)



