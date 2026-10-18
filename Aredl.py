import requests
from test_2 import *
url = "https://api.aredl.net/v2/api/aredl/levels?exclude_legacy=true"


Beaten_extremes = Record_names(url_user_id)
my_dict = {}
my_demons_set = set()
with open("my_demons.txt", "r") as file:
            for line_number, line in enumerate(file, start=1):
                normal = line.strip().lower() 
                if normal:
                    my_dict[normal] = line_number
                    my_demons_set.add(normal)

response = requests.get(url)
if response.status_code == 200:
    print("API request successful.")
else:
    print(f"API request failed with status code: {response.status_code}")
    exit(1)

levels = response.json()
Demon_list_str = {}
for index in range(len(levels)):
    Demon_list_str[levels[index]["name"]] = levels[index]["position"],levels[index]["level_id"], levels[index]["nlw_tier"], levels[index]["gddl_tier"]


visited_counter= 0
visited=[]


for word in Demon_list_str:
    normal_word = word.strip().lower()
    if normal_word in my_demons_set: 
        print(f'{word}: {Demon_list_str[word][0]} Id:({Demon_list_str[word][1]}) nlw_tier: {Demon_list_str[word][2]} gddl_tier: {Demon_list_str[word][3]}')
        visited.append(normal_word)
    if word in Beaten_extremes:
        visited_counter += 1

for demon in my_demons_set:
    if demon not in visited:
        print(f"{demon} not found in line {my_dict[demon]}")
    

print(Beaten_extremes)

print(f"{visited_counter}/{len(visited)}\n{visited_counter/len(visited)*100}% of the list is completed")
#ideas: 
#
# get pecentage of demons I have beaten from my list  ✓
#
# count every demon in my_demons, subtract not found ones
#
# get the beaten demons from user api then make a fraction ✓
#
# fileter by tier or any other type of filtering
#
# filter oposite way :-1 easy
#
#I can just count beaten extremes /my_demon_set or I can do beaten extremes /aredl
#
#I can put this loop for word in Demon_list_str: into this for index in range(len(levels)):
#    Demon_list_str[levels[index]["name"]] = levels[index]["position"],levels[index]["level_id"], levels[index]["nlw_tier"], levels[index]["gddl_tier"]
#
#
#
