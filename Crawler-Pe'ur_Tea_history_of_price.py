import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

def get_TAE_price_record(number):
    '''
    Some website would put important information in Javascript, if we want to get these, how can we do it???
    This time, we must use 'webdriver.PhantomJS' to crawle them. 
    (If you dont know whether these information is in Javascrpit? 
    I gonna tell you that there is a nice tool can help you finish the frist step.
    1. open the 'GOOGLE' to search 'Quick Javascript switcher'.
    2. download it!
    3. you would get a message on the right upper corner 'finished download'.
    4. turn on/off it, you would see that there are some information disappeared. That means they are in Javascript.
    )
    '''
    driver = webdriver.PhantomJS(executable_path='/Users/alex/Desktop/new_jupyter/phantomjs') #Javascript, only PhantomJS can see what we want.
    driver.get('https://www.donghetea.com/goods.php?id={}'.format(number)) # set up format()
    pageSource = driver.page_source
    #print(pageSource)
    soup = BeautifulSoup(pageSource, 'lxml')
    tea_rows = [t.text for t in soup.find('div', 'tabqushi').select('td')] # find div and td in a bowl of soup.
    df = pd.DataFrame()
    df['截止日期'] = tea_rows[0:2000:6]
    df['參考價'] = tea_rows[1:2000:6]
    df['漲跌額'] = tea_rows[2:2000:6]
    df['漲跌幅'] = tea_rows[3:2000:6]
    df['日均漲跌額'] = tea_rows[4:2000:6]
    df['日均漲跌幅'] = tea_rows[5:2000:6]
    '''
    This part is very important. It's because you would see all messages are in one row. 
    you need to set [start:end:interval] to divide each column.
    why did I set 2000 this numerable number? 
    when I test other Tea number, the number would exceed my original setting.
    Therefore, I setted 2000 here.
    '''
    #print(type(df))
    #df = df.head() # If you just want to find 5, 10, 15, 20 rows. if you use .head(number)
    return df
    
    
    
number = input() # Do you remember that we set format()?
df_tea_price_record = get_TAE_price_record(number)
print(df_tea_price_record)
