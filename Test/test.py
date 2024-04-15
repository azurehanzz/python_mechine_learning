from random import randint
class Die:
    def __init__(self,sides = 6):
        self.sides = sides
    def roll_die(self,num):
        roll_num = 0
        while roll_num<num:
          print(randint(1,self.sides))
          roll_num = roll_num + 1
        print("此次摇筛结束")

die1 = Die()
die1.roll_die(10)
die2 = Die(10)
die2.roll_die(20)

lottary = ['a','b','c','d','e',1,2,3,4,5,6,7,8,9,10]
lottary_num =[lottary[randint(0,14)],lottary[randint(0,14)],lottary[randint(0,14)],lottary[randint(0,14)]]
print(f"if the numbers and characters are "
      f"{lottary_num}"
      f",you will get a big gift")
count = 1
while True:
     my_lottary = [lottary[randint(0, 14)], lottary[randint(0, 14)], lottary[randint(0, 14)], lottary[randint(0, 14)]]
     unsearch = [0,1,2,3]
     i = 0
     while i<4:
         j = 0
         for num in unsearch:
             if my_lottary[i] == lottary_num[num]:
                 del unsearch[j]
                 continue
             else:
                 j = j+1
         if my_lottary[i] != lottary_num[num]:
             break
         i =i +1
     if i == 4:
         print(f"中奖了！我的彩票为{my_lottary}"
               f"所需次数为{count}")
         break
     count = count+1





