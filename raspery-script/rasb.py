#!/usr/bin/python
import requests
import json

ROOT_URL = "http://guitar-tuner-smart.herokuapp.com/selected"
response = requests.get(ROOT_URL)

data = response.json()["selected"]

message = (
    "n="
    + data["name"]
    + "|"
    + "1="
    + str(data["str_one"])
    + "|"
    + "2="
    + str(data["str_two"])
    + "|"
    + "3="
    + str(data["str_three"])
    + "|"
    + "4="
    + str(data["str_four"])
    + "|"
    + "5="
    + str(data["str_five"])
    + "|"
    + "6="
    + str(data["str_six"])
    + "!"
)

print(message)


##n=asd|1=123.9|2=134.8|.....5=123.0!#
# signal = "n=" + r.text.selected.name + "|"
