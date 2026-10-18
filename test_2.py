import requests
with open("api.txt", "r") as file:
    api = file.readline()    


url_user_id = "https://api.aredl.net/v2/api/aredl/profile/(api_key)"
url = "https://api.aredl.net/v2/api/aredl/records/@me"
headers = {
    "Authorization": f"Bearer {api}"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("API request successful.")
else:
    print(f"API request failed with status code: {response.status_code}")
    exit(1)

def Record_names(url):
    data = requests.get(url, headers=headers).json()
    demons = []
    for i in range(len(data["records"])):
        demons.append(data["records"][i]["level"]['name'])
    return demons
