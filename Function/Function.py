def display_message():
    print("今天学习函数")
display_message()

def my_favorite_book(book_name):
    print(f"我最喜欢的书为:{book_name.title()}")
my_favorite_book("高等数学")

def make_shirt(size,Alpha):
    print(f"T恤的大小为{size},T恤的上的字母为{Alpha}")
make_shirt(size = 'XXL' , Alpha = 'C')
make_shirt('XXL' , Alpha = 'C')
make_shirt('XXL' , 'C')

def make_shirt(size,Alpha = "I love python"):
    print(f"T恤的大小为{size},T恤的上的字母为{Alpha}")
make_shirt('BIG')
make_shirt('MIDDLE')
make_shirt('SMALL',Alpha = 'I love C++')

def city_country(cityname,country):
    full_city = f"{cityname.title()},{country.title()}"
    return full_city
print(city_country("shanghai","china"))
print(city_country("newyork","america"))
print(city_country("zhenjiang","china"))

def make_album(Singer_Name,Album_Name,Song_num = None):
    if Song_num:
        album = {'Single': Singer_Name, 'Album': Album_Name, 'NumofSong': Song_num}
    else:
        album = {'Single': Singer_Name, 'Album': Album_Name}
    return album
album1 = make_album('jaychou','qilixiang')
album2 = make_album('JJlin','tashuo')
album3 = make_album('Golden','Dr,paper',10)
print(f"{album1['Single']}")
print(f"{album2['Album']}")
print(album3)


# while True:
#     print("请输入以下信息:")
#     print("输入exit退出程序")
#     Singer_Name = input("歌手名字:")
#     if Singer_Name == 'exit':
#         print("退出成功!")
#         break
#     Album_Name = input("专辑名字:")
#     album = make_album(Singer_Name,Album_Name)
#     print(album)

arr = ['message1','message2','message3']
sent_messages=[]
def send_message(variable):
    while(variable):
      message = variable.pop()
      sent_messages.append(message)
      print(f"sending message: {message}")
    print("The following messages have been sent:")
    for message in sent_messages:
        print(message)
    print("The following messages have not been sent:")
    if variable == None:
        print("None")
    else:
        for message in variable:
          print(message)

send_message(arr[:])

print("original messgaes")
for message in arr:
    print(message)
print("sent messages")
sent_messages.sort()
for message in sent_messages:
    print(message)

def sandwitch(*food):
    print("The food in sandwitch")
    for sauce in food:
        print(f"-> {sauce}")

sandwitch('meet','vegetable','sausage')
sandwitch('shit1','shit2','shit3')
sandwitch('Just bread')

def user_profile(first_name,middle_name,last_name,**user_info):
    user_info['first_name'] = first_name
    if middle_name:
        user_info['middle_name'] = middle_name
        user_info['last_name'] = last_name
        return user_info
    else:
        user_info['last_name'] = last_name
        return user_info

my_info =user_profile(first_name='jiang',middle_name='jing',last_name='han',location = 'zhenjiang',grade='Level 1')
print(my_info)

def make_car(制造商,型号,**car_info):
    car_info['制造商'] = 制造商
    car_info['型号'] = 型号
    return car_info

car = make_car('奥迪','奥迪A6',color = 'black' , size = 'big')
print(car)
