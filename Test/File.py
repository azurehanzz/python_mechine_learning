import json
try:
  with open('Number_user_like.json') as num:
    number = json.load(num)
except FileNotFoundError:
    number_like = input("你最喜欢的数为多少:")
    with open('Number_user_like.json', 'w') as num:
      json.dump(number_like,num)
else:
    print(f"你最喜欢的数为{number}")