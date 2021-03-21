import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import sys
import csv
import re
# import mysql.connector

start_time = time.time()

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="phpmyadmin",
#     passwd="Admin1!",
#     database="ppl20"
# )


def copyRight(name):
    if 'A' in name:
        name = name.replace('A', 'À')
    elif 'a' in name:
        name = name.replace('a', 'à')
    elif 'E' in name:
        name = name.replace('E', 'È')
    elif 'e' in name:
        name = name.replace('e', 'è')
    elif 'I' in name:
        name = name.replace('I', 'Ì')
    elif 'i' in name:
        name = name.replace('i', 'ì')
    elif 'O' in name:
        name = name.replace('O', 'Ò')
    elif 'o' in name:
        name = name.replace('o', 'ò')
    elif 'U' in name:
        name = name.replace('U', 'Ù')
    elif 'u' in name:
        name = name.replace('u', 'ù')
    else:
        name = name + name[len(name)]

    return name


# share
data = []
for i in range(1, 13):
    if i == 10:
        i = 25
    elif i == 11:
        i = 29
    elif i == 12:
        i = 40
    ids = str(i)
    temp_url = []
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        "/usr/local/bin/chromedriver", options=chrome_options)
    url = "http://www.espncricinfo.com/india/content/player/country.html?country=" + ids
    driver.get(url)
    elem = driver.find_elements_by_xpath(
        '//*[@id="rectPlyr_Playerlistt20"]/table/tbody/tr/td/a')
    [temp_url.append(ele.get_attribute("href")) for ele in elem if ele]
    driver.close()
    count = 0
    temp_team = []
    for url in temp_url:
        temp_data = []
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        heading = soup.select('.ciPlayernametxt div h1')[0].getText().rstrip()
        heading = copyRight(heading)
        temp_data.append(heading)

        country = soup.select('.PlayersSearchLink')[0].getText().rstrip()
        temp_data.append(country)

        fields = ['Current age', 'Playing role', 'Bowling style']
        for field in fields:
            try:
                info = soup.find('b', string=field).parent.find(
                    'span').getText()
                if field == 'Current age':
                    info = info.split(' ')[0]
                if field == 'Playing role':
                    if 'Wicketkeeper' in info:
                        info = 'Wicketkeeper'
                    elif 'Bowling' in info:
                        info = 'Bowler'
                    elif 'Bowling' in info:
                        info = 'Bowler'
                    elif 'allrounder' in info:
                        info = 'All-rounder'
                    else:
                        info = 'Batsman'
                temp_data.append(info)
            except AttributeError:
                temp_data.append('Wicketkeeper')

        batting = soup.select('.data1')[2].getText().split('\n')
        if batting[1] != 'T20Is':
            batting = soup.select('.data1')[0].getText().split('\n')
        if batting[1] != 'T20Is':
            batting = soup.select('.data1')[1].getText().split('\n')

        fields = [3, 7, 9, 5, 8, 6, 10, 13, 12]
        for field in fields:
            batting_field = batting[field]
            if batting_field == '-':
                batting_field = 0

            if type(batting_field) == str and field == 6:
                batting_field = re.sub(
                    "[^0-9 and field == 6]", "", batting_field)
            temp_data.append(batting_field)

        bowling = soup.select('.data1')[8].getText().split('\n')
        if bowling[1] != 'T20Is':
            bowling = soup.select('.data1')[4].getText().split('\n')
        if bowling[1] != 'T20Is':
            bowling = soup.select('.data1')[6].getText().split('\n')

        fields = [3, 9, 4, 10, 6, 7, 11]
        for field in fields:
            bowling_field = bowling[field]
            if bowling_field == '-':
                bowling_field = 0
            try:
                temp_data.append(bowling_field)
            except:
                temp_data.append(0)

        temp_data.extend([batting[14], batting[15]])
        temp_team.append(temp_data)
    data.append(temp_team)

file = open("final.txt", 'a')

# mycursor = mydb.cursor()
# sql =
# val =
# mycursor.execute(sql, val)
# mydb.commit()

# with open('output.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(data[0])
# csvFile.close()

# with open('output.csv', 'a') as csvFile:
#     writer = csv.writer(csvFile)
#     for i in range(1, len(data)):
#         writer.writerows(data[i])
# csvFile.close()

# sys.stdout = open('output.txt','wt')
print(data)
print(len(data))
print(time.time()-start_time)


df = pd.DataFrame(data[0])
df.to_csv("final1.txt", index=False)
