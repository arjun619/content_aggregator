from bs4 import BeautifulSoup
import requests

def data_science_scrap():
    raw_info=requests.get("https://towardsdatascience.com/data-science/home")
    info=BeautifulSoup(raw_info.text)
    temp=info.find_all('a')
    