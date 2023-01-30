import requests

url = "https://mac-address-lookup1.p.rapidapi.com/static_rapid/mac_lookup/"

querystring = {"query":"BC:5F:F4:36:78:7A"}

headers = {
	"X-RapidAPI-Key": "1bb9a3b011msh6251b8cf0c87342p184852jsned36deac6de7",
	"X-RapidAPI-Host": "mac-address-lookup1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)