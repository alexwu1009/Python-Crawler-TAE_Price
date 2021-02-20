import requests
import pandas as pd
from bs4 import BeautifulSoup

def TAE_now_tea_price(): #TAE has divied several different categories, 'now' means under 5 years.
    url = 'https://donghetea.com/fanti/quotes.php?id=5'
    r = requests.get(url)
    html_str = r.text
    soup = BeautifulSoup(html_str, 'lxml')
    teas = soup.find_all('li', 'quotes_list')
    result = []
    for tea in teas:  # make a For to get each information
        name = tea.find("span", "dh1").text.strip() #return on the inspector, we can find where the name is or where the price is. 
        price = tea.find("span", "dh2").text.strip() 
        up = tea.find("span", "dh3").text.strip()
        down = tea.find("span", "dh4").text.strip()
        date = tea.find("span", "dh6").text.strip()
        evaluation = tea.find("span", "dh7").text.strip().replace('\n|', '') # sometimes, we won't find any mistake on any column, dont forget to test each column.  
        result.append((name, price, up, down, date, evaluation))  #here we have to put all columns in one result[]
    now_tea_df = pd.DataFrame(result, columns=['產品名', '參考價', '升跌幅度', '升降百分比', '更新日期', '評分']) #if we dont set up columns, we won't see any column.
    return now_tea_df                          #this part, if you want to change these chinese words to English or any language, you can directly change them:))

def TAE_New_tea_price(): # 'New' means between 5 to 15 years 
    url = 'https://donghetea.com/fanti/quotes.php?id=6'
    r = requests.get(url)
    html_str = r.text
    soup = BeautifulSoup(html_str, 'lxml')
    teas = soup.find_all('li', 'quotes_list')
    result = []
    for tea in teas:
        name = tea.find("span", "dh1").text.strip()
        price = tea.find("span", "dh2").text.strip()
        up = tea.find("span", "dh3").text.strip()
        down = tea.find("span", "dh4").text.strip()
        date = tea.find("span", "dh6").text.strip()
        evaluation = tea.find("span", "dh7").text.strip().replace('\n|', '')
        result.append((name, price, up, down, date, evaluation))
    new_tea_df = pd.DataFrame(result, columns=['產品名', '參考價', '升跌幅度', '升降百分比', '更新日期', '評分'])
    return new_tea_df

def TAE_NewMiddle_tea_price(): # 'NewMiddle' means 15 years upper which tea is going to become old tea(unless 20 years)
    url = 'https://donghetea.com/fanti/quotes.php?id=7'
    r = requests.get(url)
    html_str = r.text
    soup = BeautifulSoup(html_str, 'lxml')
    teas = soup.find_all('li', 'quotes_list')
    result = []
    for tea in teas:
        name = tea.find("span", "dh1").text.strip()
        price = tea.find("span", "dh2").text.strip()
        up = tea.find("span", "dh3").text.strip()
        down = tea.find("span", "dh4").text.strip()
        date = tea.find("span", "dh6").text.strip()
        evaluation = tea.find("span", "dh7").text.strip().replace('\n|', '')
        result.append((name, price, up, down, date, evaluation))
    new_middle_df = pd.DataFrame(result, columns=['產品名', '參考價', '升跌幅度', '升降百分比', '更新日期', '評分'])
    return new_middle_df

now_tea_long = TAE_now_tea_price()
new_tea_long = TAE_New_tea_price()
new_middle_long = TAE_NewMiddle_tea_price()
