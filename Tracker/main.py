import phonenumbers
from test import number
from phonenumbers import geocoder


# get county name of number

ch_number = phonenumbers.parse(number, "CH") 
print(geocoder.description_for_number(ch_number, "en"))

# get service provider of number

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))