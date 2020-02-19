from bs4 import BeautifulSoup
import requests

def data_science_scrap():
    raw_info=requests.get("https://towardsdatascience.com/data-science/home")
    info=BeautifulSoup(raw_info.text,"html.parser")
    temp=info.find_all('a',"u-block u-xs-height170 u-height172 u-backgroundSizeCover u-backgroundOriginBorderBox u-backgroundColorGrayLight u-borderLighter")
    content_links=[]
    for i in range(len(temp)):
        url=temp[i]["href"]
        article=temp[i].text
        content_links.append([article,url])
    return content_links    
def football_scrap():
    raw_info=requests.get("https://www.foxsportsasia.com/football/premier-league/")
    info=BeautifulSoup(raw_info.text,"html.parser")
    temp=info.find_all('a')
    content_links=[]
    for link in range(7):
        if temp[link].text!='':
            url=temp[link]['href']
            content=temp[link].text
            content_links.append([content,url])
    return content_links

