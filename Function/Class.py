class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_servered = 0
    def describe_restaurant(self):
        print(f"这间餐厅的名字为{self.restaurant_name}\n"
              f"这间餐厅的菜类别为{self.cuisine_type}")
    def open_restaurant(self):
        print("这间餐厅正在营业")
    def set_number_serverd(self,number):
        self.number_servered = number
        print(f"现在服务人数为{self.number_servered}")
    def increment_number_serverd(self,increnum):
        self.number_servered = self.number_servered + increnum
        print(f"现在服务人数为{self.number_servered}")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
    def favor(self):
        self.favor = ['甜','少冰','正常甜']
        print(self.favor)



