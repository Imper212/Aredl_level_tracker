import requests
url = "https://api.aredl.net/v2/api/aredl/levels?exclude_legacy=true"


my_dict = {}
my_demons_set = set()
with open("my_demons.txt", "r") as file:
            for line_number, line in enumerate(file, start=1):
                clean = line.strip().lower() 
                if clean:
                    my_dict[clean] = line_number
                    my_demons_set.add(clean)
     

response = requests.get(url)
levels = response.json()
Demon_list_str = {}


for index in range(len(levels)):
    Demon_list_str[ levels[index]["name"]] = levels[index]["position"]


visited=[]


for word in Demon_list_str:
    for word2 in my_demons_set:
        if word2 == word.lower().strip():
            print(word,Demon_list_str[word])
            visited.append(word2)


for index in my_demons_set:
    if index not in visited:
        print(f"{index} not found in line {my_dict[index]}")