import pandas as pd
import sys
import datetime
import random
import matplotlib.pyplot as plt


df = pd.read_csv("weightdata.csv", sep=",", index_col=0)

hiduke = datetime.date.today()

args = sys.argv

if len(args) is not 3:
    voice = ['今日の体重と体脂肪率を入力してください．', '今日の体重を入力してください！はとバスさん！', '体重を入力してぇ，はとバス']
    print(random.choice(voice))
    weight = float(input())
    fat = float(input())

else:
    weight = args[1]
    fat = args[2]

day_sum = len(df.index)
minweight = max(df['体重'])
sabun = round(minweight, 5) - weight
sabun = round(sabun, 5)
BMI = round(weight / (1.735 * 1.735), 5)
print("体重の差は {0} kg です.BMIは{1}ですよ〜！".format(sabun, BMI))

indx = ['日数', '日付', '体重', '差分', '体脂肪率', 'BMI']
data = [day_sum+1, hiduke, weight, sabun, fat, BMI]

df2 = pd.Series(data, index=indx)
df = df.append(df2, ignore_index=True)

df.to_csv('weightdata.csv')

plt.plot(df.体重)
plt.plot(df.体脂肪率)
plt.plot(df.BMI)
plt.savefig("./pic/data.png")
