from requests import get

my_ip = get("https://api.ipify.org").text
print(my_ip)