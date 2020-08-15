from django.shortcuts import render
import requests
import json
import math
from math import *


# /
def iss_home_page_method(request):
    # Make a get request to get the latest position of the international space station from the opennotify api.
    response = requests.get("http://api.open-notify.org/iss-now.json")
    # Print the status code of the response.
    print(response.status_code)
    # print content
    # print(response.content)

    dictionary_iss_position = response.json()
    print(dictionary_iss_position)

    latitude_my = 53.13
    print("latitude_my = " + str(latitude_my))
    latitude_my_in_radians = latitude_my * pi / 180

    longitude_my = 23.16
    print("longitude_my = " + str(longitude_my))
    longitude_my_in_radians = longitude_my * pi / 180

    latitude_iss = round(float(dictionary_iss_position["iss_position"]["latitude"]), 4)
    print("latitude_iss = " + str(latitude_iss))
    latitude_iss_sign = 0
    if latitude_iss >= 0:
        latitude_iss_sign = 1
    elif latitude_iss < 0:
        latitude_iss_sign = -1
        latitude_iss = (-1) * latitude_iss

    latitude_iss_in_radians = latitude_iss * pi / 180

    longitude_iss = round(float(dictionary_iss_position["iss_position"]["longitude"]), 4)
    print("longitude_iss = " + str(longitude_iss))
    longitude_iss_sign = 0
    if longitude_iss >= 0:
        longitude_iss_sign = 1
    elif longitude_iss < 0:
        longitude_iss_sign = -1
        longitude_iss = (-1) * longitude_iss

    longitude_iss_in_radians = longitude_iss * pi / 180

    earth_radious_in_km = 6371

    central_angle_in_radians = acos((sin(latitude_my_in_radians) * sin(latitude_iss_in_radians)) +
                                        (cos(latitude_my_in_radians) * cos(latitude_iss_in_radians) * cos(
                                            longitude_my_in_radians - longitude_iss_in_radians)))

    distance_exact = earth_radious_in_km * central_angle_in_radians
    distance_in_km = int(round(distance_exact, 0))

    print("distance_in_km = " + str(distance_in_km))

    context = {
        "dictionary_iss_position": dictionary_iss_position,
        "latitude_iss": latitude_iss,
        "latitude_iss_sign": latitude_iss_sign,
        "longitude_iss": longitude_iss,
        "longitude_iss_sign": longitude_iss_sign,
        "latitude_my": latitude_my,
        "longitude_my": longitude_my,
        "earth_radious_in_km": earth_radious_in_km,
        "central_angle_in_radians": central_angle_in_radians,
        "distance_in_km": distance_in_km
    }

    return render(request, "iss/iss.html", context)
