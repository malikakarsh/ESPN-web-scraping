from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

html_text = requests.get(
    'http://m.espncricinfo.com/india/content/player/253802.html').text
soup = BeautifulSoup(html_text, 'lxml')
findings = soup.find_all(
    'tr', attrs={"data-days": 738132})
'''
for finds in findings[1]:
    print(finds)
'''
'''
my_list = []
for finds in findings:
    my_list.append(finds.text.replace('\n', ' ').split())
print(len(my_list))
'''
name = soup.find_all('p', attrs={"class": "ciPlayerinformationtxt"})
'''
print(name[0].span.text)
print(name[2].span.text.split()[0])
print(name[4].span.text)
print(name[5].span.text)
print(name[6].span.text)
'''


def fetchData(url, id):
    html_text = requests.get(f'{url}').text
    soup = BeautifulSoup(html_text, 'lxml')
    name = soup.find_all('p', attrs={"class": "ciPlayerinformationtxt"})
    # Name = []
    # Country = []
    # Age = []
    # Gender = []
    # Player_type = []
    # Batting_style = []
    # Bowling_style = []
    # Batting_innings = []
    # Runs = []
    # Highest = []
    # Batting_average = []
    # Balls_faced = []
    # Strike_rate = []
    # Hundreds = []
    # Fours = []
    # Sixes = []
    # Catches = []
    # Stumpings = []

    # -------
    Best_bowling_figure = []
    Balls_bowled = []
    # Bowling_average = []
    # Economy = []
    # Bowling_strike_rate = []

    # Appending values:
    try:
        # Name.append(name[0].span.text)
        # Country.append("Ireland")
        # Age.append(name[2].span.text.split()[0])
        # Gender.append("Male")
        # Player_type.append(name[4].span.text)
        # Batting_style.append(name[5].span.text)
        # Bowling_style.append(name[6].span.text)

        findings = soup.find_all(
            'tr', attrs={"data-days": id})
        my_list = []
        for finds in findings:
            my_list.append(finds.text.replace('\n', ' ').split())

        if (len(my_list) == 5):
            first = 1
            second = 3
        else:
            first = 0
            second = 1

        # Batting_innings.append(my_list[first][2])
        # Runs.append(my_list[first][4])
        # Highest.append(my_list[first][5])
        # Batting_average.append(my_list[first][6])
        # Balls_faced.append(my_list[first][7])
        # Strike_rate.append(my_list[first][8])
        # Hundreds.append(my_list[first][9])
        # Fours.append(my_list[first][11])
        # Sixes.append(my_list[first][12])
        # Catches.append(my_list[first][13])
        # Stumpings.append(my_list[first][14])

        Best_bowling_figure.append(my_list[second][6])
        Balls_bowled.append(my_list[second][3])

        # value = pd.DataFrame(
        #     {'Name': Name, 'Country': Country, 'Age': Age, 'Gender': Gender, 'Player_type': Player_type, 'Batting_style': Batting_style,
        #      'Bowling_style': Bowling_style, 'Batting_innings': Batting_innings, 'Runs': Runs, 'Highest': Highest, 'Batting_average': Batting_average,
        #      'Balls_faced': Balls_faced, 'Strike_rate': Strike_rate, 'Hundreds': Hundreds, 'Fours': Fours, 'Sixes': Sixes, 'Catches': Catches,
        #      'Stumpings': Stumpings, 'Bowling_innings': Bowling_innings, 'Wickets': Wickets, 'Bowling_average': Bowling_average, 'Economy': Economy, 'Bowling_strike_rate': Bowling_strike_rate})

        value = pd.DataFrame(
            {'Best_bowling_figure': Best_bowling_figure,
             'Balls_bowled': Balls_bowled}
        )
        if not os.path.isfile('Test.csv'):
            value.to_csv('Test.csv', index=False, mode='a')
        else:
            value.to_csv('Test.csv', index=False,
                         header=False, mode='a')
        print(value)
    except:
        print("Error")


while (True):
    index = input("Continue? ")
    if (index == 'NO'):
        break
    else:
        try:
            url = input("Enter URL: ")
            id = int(input("Enter id: "))
            fetchData(url, id)
        except:
            print("There is an error")
