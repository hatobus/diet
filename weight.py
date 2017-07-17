#coding:utf-8

import pandas as pd,numpy as np , datetime, random , matplotlib.pyplot as plt
from PIL import Image

# %matplotlib inline

df = pd.read_csv("weightdata.csv",sep=",",index_col=0)

hiduke = datetime.date.today()

r = random.randint(0, 10)

if r % 2 == 0:
    print("今日の体重と体脂肪率を入力してください．")
    weight = float(input())
    fat = float(input())

elif r % 2 == 0 and r % 3 == 0:
    print("今日の体重を入力してください！はとバスさん！")
    weight = float(input())
    fat = float(input())

elif r % 2 == 1:
    print("体重を入力してぇ，はとバス")
    weight = float(input())
    fat = float(input())

day_sum = len(df.index)
minweight = min(df['体重'])
sabun = round(minweight, 5) - weight
sabun = round(sabun,5)
BMI = round(weight/(1.735*1.735),5)
print("体重の差は {0} kg です.BMIは{1}ですよ〜！".format(sabun,BMI))

# print(hiduke, day_sum, weight, sabun)

df2 = pd.Series([day_sum,hiduke,weight,sabun,fat,BMI],index=['日数','日付','体重','差分','体脂肪率','BMI'])
df = df.append(df2,ignore_index=True)

df.to_csv('weightdata.csv')
