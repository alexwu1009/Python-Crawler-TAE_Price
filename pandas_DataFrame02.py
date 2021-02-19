import pandas as pd

data = pd.DataFrame({
    "name":["Amy", "John", "Bob"],
    "Salary":[30000, 50000, 40000]
    }, index=['a', 'b', 'c'])
#print(data)
#print(data.size) #資料數值
#print(data.shape) #資料型態
#print(data.index) ＃資料索引

#print(data.iloc[1], data.iloc[2], sep='\n') #取得列
#print(data.loc['c'], sep='\n') #根據索引index取得資料
"""
print(data["name"], sep='\n')

names = data["name"] #取得特定的列則會成為單為度的資料
print(names.str.upper(), sep='\n') #字體轉大寫

salaries = data["Salary"]
print(salaries.mean()) #取平均值, mean()
"""

#建立新的欄位
data["revenue"]=[500000, 300000, 400000]
#另一個使用pd.Series增加新欄位的方法，要加寫入對應index值
data["rank"]=pd.Series([3, 6, 1], index=["a", "b", "c"])
#根據現有的欄位複製至最後
data["cp"]=data["Salary"]
#在欄位中運用加減乘除
data["cp"]=data["revenue"]/data["Salary"]
print(data)

