
import requests
import json

location = input("Şehir Arayınız: ")
# istek atacağı yer
endpoint = "https://www.metaweather.com/api/location/search/?query={}".format(
    location)
response = requests.get(endpoint)  # gelen cevap


def filter_cities(response):
    # location typesi city olan verileri getirdik
    cities = list(filter(lambda x: x.get("location_type") == 'City', response))
    return cities


# burada ise gelen bi sürü responselere bir id atadık mesela  SA yazdık
def print_citites(cities):
    # 1 San Fransisco
    # 2 Osaka
    # 3 San Diego
    for id, city in enumerate(cities):
        # sıralı ve sadece city isimleriyle gelmesini sağladı
        print("{} - {}".format(id, city.get("title")))


# 5 GÜNLÜK HAVA TAHMİNİ VERİSİNİ ÇEKME
def forecast(woeid):
    endpoint_forecasting = "https://www.metaweather.com/api/location/{}/".format(
        woeid)
    response = requests.get(endpoint_forecasting)
    response_to_json = json.loads(response.content)
    consolidated_weather = response_to_json["consolidated_weather"]
    return consolidated_weather


if response.status_code == 200:
    conver_to_dict = json.loads(response.content)
    cities = filter_cities(conver_to_dict)
    print_citites(cities)


city_id = int(input("şehir seç: "))
city = cities[city_id]
city_wooid = city.get("woeid")
forsecting_result = forecast(city_wooid)

for weather in forsecting_result:  # verileri yazdırdık
    print("-----" *30)
    print("Tarih:"+" " + weather.get("applicable_date"), "| | Hava Durumu:"+" " + weather.get("weather_state_name"), "| | Minumum Derece:" +
          " ", weather.get("min_temp"), "| | Maksimum Derece:"+" ", weather.get("max_temp"))  # tahmin durumunu yazdırıyor tarih ve gün
    print("-----" *30)
