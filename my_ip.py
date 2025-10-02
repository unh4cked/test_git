from requests import get

my_ip = get("https://api.ipify.org").text
print(f"my ip: {my_ip}")