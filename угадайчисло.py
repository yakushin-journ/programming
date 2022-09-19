#Игра угадай число

import random

secret=random.randint(1,101)
status=-2 #-2 начало, -1 меньше, 1 больше, 0 угадал
count=0

while (status!=0) and (count<=7):
    x=int(input("Введи число: "))
    count=count+1
    if x<secret:
        status=-1
        print("Меньше")
    if x>secret:
        status=1
        print("Больше")
    if x==secret:
        status=0
        print("Угадал")

if count>7:
    print("Вы исчерпали количество попыток!")
