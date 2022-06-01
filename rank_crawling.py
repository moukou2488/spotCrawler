import requests
from bs4 import BeautifulSoup
import json

response = requests.get('https://www.koreabaseball.com/TeamRank/TeamRank.aspx')

soup = BeautifulSoup(response.content, 'html.parser')
 
table = soup.find('table')    # <table class="table_develop3">을 찾음
rank = []                            # 데이터를 저장할 리스트 생성
trs = table.find_all('tr')
for tr in trs:
    tds = list(tr.find_all('td'))
    ranking = ''
    team = ''
    win = ''
    lose = ''
    tie = ''
    odds = ''
    for td in tds:
        rankItem = {}
        ranking = tds[0].text
        team = tds[1].text
        win = tds[3].text
        lose = tds[4].text
        tie = tds[5].text
        odds = tds[6].text
    rankItem = {
            'ranking':ranking,'team':team,'win':win,'lose':lose,'tie':tie,'odds':odds
        }
    rank.append(rankItem)
    
rank = rank[1:]    
   
with open('rank.json', 'w', encoding="utf-8") as make_file:
     json.dump(rank, make_file, ensure_ascii=False, indent="\t")
        
