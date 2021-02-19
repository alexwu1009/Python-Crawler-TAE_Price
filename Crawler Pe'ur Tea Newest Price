import requests
import pandas as pd
from bs4 import BeautifulSoup

def TAE_now_tea_price():
    url = 'https://donghetea.com/fanti/quotes.php?id=5'
    r = requests.get(url ,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
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
    now_tea_df = pd.DataFrame(result, columns=['產品名', '參考價', '升跌幅度', '升降百分比', '更新日期', '評分'])
    return now_tea_df

def TAE_New_tea_price():
    url = 'https://donghetea.com/fanti/quotes.php?id=6'
    r = requests.get(url ,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
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

def TAE_NewMiddle_tea_price():
    url = 'https://donghetea.com/fanti/quotes.php?id=7'
    r = requests.get(url ,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
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
