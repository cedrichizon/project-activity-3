import requests #The request module allows you to send HTTP requests using Python
from requests import get

ip = get('https://api64.ipify.org').text #variable ip will determine the current user's public ip address

response = requests.get("https://geo.ipify.org/api/v2/country,city?apiKey=at_aKdQtFtfKSTzTC44OmrcH6pvEChz8&ipAddress=" + ip).json()
print("\n=============================================================")
print("Your Current Public IP Address: " + (response['ip']))
print("--------------------------LOCATION---------------------------")
print("Country: " + (response['location']['country']))
print("Region: " + (response['location']['region']))
print("City: " + (response['location']['city']))
print("Latitude: " + str(response['location']['lat']))
print("Longitude: " + str(response['location']['lng']))
print("-------------------------------------------------------------")
print("Internet Service Provider: " + (response['isp']))
print("Name: " + (response['as']['name']))
print("Autonomous System Number: " + str(response['as']['asn']))
print("Route: " + str(response['as']['route']))
print("Domain: " + str(response['as']['domain']))
print("Type: " + str(response['as']['type']))
print("=============================================================")
