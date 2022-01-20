from itertools import zip_longest
import json

with open('users.txt', 'r', encoding="utf-8") as name,\
        open('hobby.txt', 'r', encoding="utf-8") as hobby:
            names = name.read().splitlines()
            hobbys = hobby.read().splitlines()

if len(names) < len(hobbys):
    print(1)
else:
    users_hobby = dict(zip_longest(names, hobbys, fillvalue=None))
    with open('Task_3_dict.txt', 'w', encoding="utf-8") as f:
        json.dump(users_hobby, f, ensure_ascii=False)