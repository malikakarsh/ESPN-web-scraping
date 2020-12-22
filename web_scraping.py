from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'http://m.espncricinfo.com/india/content/player/253802.html').text
soup = BeautifulSoup(html_text, 'lxml')
findings = soup.find_all(
    'tr', attrs={"data-days": 738132})
'''
for finds in findings[1]:
    print(finds)
for finds in findings[3]:
    print(finds)
'''
Name = []
Country = []
Age = []
Gender = []
Player_type = []
Batting_style = []
Bowling_style = []
Batting_innings = []
Runs = []
Highest = []
Batting_average = []
Balls_faced = []
Strike_rate = []
Hundreds = []
Fours = []
Sixes = []
Catches = []
Stumpings = []
Bowling_innings = []
Wickets = []
Bowling_average = []
Economy = []
Bowling_strike_rate = []
name = soup.find_all('p', attrs={"class": "ciPlayerinformationtxt"})
print(name[0].span.text)
print(name[2].span.text.split()[0])
print(name[4].span.text)
print(name[5].span.text)
print(name[6].span.text)


def fetchData(url, id, i):
    html_text = requests.get(f'{url}').text
    soup = BeautifulSoup(html_text, 'lxml')
    name = soup.find_all('p', attrs={"class": "ciPlayerinformationtxt"})

    # Appending values:
    Name.append(name[0].span.text)
    Country.append("India")
    Age.append(name[2].span.text.split()[0])
    Gender.append("Male")
    Player_type.append(name[4].span.text)
    Batting_style.append(name[5].span.text)
    Bowling_style.append(name[6].span.text)

    findings = soup.find_all(
        'tr', attrs={"data-days": id})
