import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

def get_TAE_price_record(number):
    driver = webdriver.PhantomJS(executable_path='/Users/alex/Desktop/new_jupyter/phantomjs') #因檔案在Javascript中，使用PhantomJS可觀察。
    driver.get('https://www.donghetea.com/goods.php?id={}'.format(number))                    #格式化設定，可以輸入想查詢的號碼。
    pageSource = driver.page_source
    #print(pageSource)
    soup = BeautifulSoup(pageSource, 'lxml')
    tea_rows = [t.text for t in soup.find('div', 'tabqushi').select('td')] #從前看到的資訊都會分別放在不同的編碼中，但因此網站有反爬蟲機制，把所有資訊都放在同一個td當中。
    df = pd.DataFrame()                                                    #抓到的資料會顯示在同一個row中，為了通通放進不同的column中，使用迴圈。
    df['截止日期'] = tea_rows[0:2000:6]                                     #資料中每六個跳一列，依照規律設定為6。
    df['參考價'] = tea_rows[1:2000:6]                                       #因不同茶類有可能會導致超過欄位數，所以把結束數字增加到2000(大於結束數都可）。
    df['漲跌額'] = tea_rows[2:2000:6]
    df['漲跌幅'] = tea_rows[3:2000:6]
    df['日均漲跌額'] = tea_rows[4:2000:6]
    df['日均漲跌幅'] = tea_rows[5:2000:6]
    #print(type(df))
    #df = df.head() 如果只想找前幾個，可以使用head()函數達到目的。
    return df
    
    
    
number = input() #預設2020年的7542（編號2354）
df_tea_price_record = get_TAE_price_record(number)
df_tea_price_record


#=================================以下為作圖======================================
#不同編號的茶品做成的圖樣不同，需重新再次製作
#舉例2020年7542歷史價格漲幅度
x = df_tea_price_record['截止日期']
y = df_tea_price_record['參考價']

my_font = FontProperties(fname='STHeiti Medium.ttc') #中文字體 my_font

fig, axes = plt.subplots(figsize=(30, 10))
axes = plt.axes()

axes.set_title('大益-2001_7542', color='r', fontsize=100, FontProperties=my_font) #設定中文字體
axes.set_xlabel('Date', fontsize=100, color='r', FontProperties=my_font)
axes.set_xticklabels(['2020年4月', '2020年5月', '2020年6月', '2020年7月', '2020年8月', '2020年9月', '2020年10月', '2020年11月', '2020年12月','2021年1月', '2021年2月'], FontProperties=my_font)
                                             #原始資料的日期非常多，製作圖表時會影響視覺感，重新設定以月份為主。
axes.set_xticks(np.arange(3, 290, 12))       #X軸刻度設定
axes.set_xlim(0, 125)                        #設定圖表的線性長度

axes.set_ylabel('RMD', fontsize=100, color='r', FontProperties=my_font)
axes.set_yticklabels(['3萬', '4萬', '5萬', '6萬', '7萬', '8萬', '9萬', '10萬', '11萬', '12萬', '13萬', '14萬', '15萬', '16萬'], 
                     FontProperties=my_font) #因價格數字複雜，重新設定價格標示
axes.set_yticks(np.arange(0, 200, 10))       #Y軸刻度設定
axes.set_ylim(0, 140)                        #設定Y軸平均間格

axes.plot(x, y)
plt.show()
