import pandas

players = pandas.read_csv('Players.csv')


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
        name = name + name[len(name)-1]

    return name


# for i in range(len(players['Name'])):
#     players['Name'][i] = copyRight(players['Name'][i])

# for i in range(len(players['Gender'])):
#     players['Gender'][i] = 'M'

# for i in range(len(players['Player_type'])):
#     if players['Player_type'][i] == 'Wicketkeeper batsman':
#         if players['Batting_style'][i] == 'Wicketkeeper' or players['Bowling_style'][i] == 'Wicketkeeper':
#             players['Player_type'][i] = 'Wicketkeeper'
#         else:
#             players['Player_type'][i] = 'Batsman'

#     elif 'batsman' in players['Player_type'][i]:
#         players['Player_type'][i] = 'Batsman'

#     elif players['Player_type'][i] == 'Batting allrounder':
#         players['Player_type'][i] = 'Batsman'

#     elif players['Player_type'][i] == 'Bowling allrounder':
#         players['Player_type'][i] = 'Bowler'


# print(players[['Name', 'Gender', 'Player_type', 'Country']].head(60))
# print(f"(hello,'{players['Player_type'][0]}',ghetto)")

# 'Bowling_style', 'Matches_played', 'Batting_average', 'Strike_rate', 'Runs', 'Balls_faced', 'Highest', 'Hundreds',
my_list = ['Name', 'Country', 'Player_type', 'Age']
#            'Sixes', 'Fours', 'Bowling_innings', 'Bowling_average', 'Balls', 'Economy', 'Wickets', 'Best_bowling_figure', 'Bowling_strike_rate', 'Catches', 'Stumpings']
# for i in range(len(my_list)):
#     for j in range(len(players['Name'])):
#         if players[my_list[i]][j] == '-':
#             players[my_list[i]][j] = 0

# print(players.head(40))

file = open('Batting_details.txt', 'w+')

for i in range(len(players['Name'])):
    file.write(
        f"({i+1},{players['Batting_innings'][i]},{players['Batting_average'][i]},{players['Balls_faced'][i]},{players['Runs'][i]},'{players['Highest'][i]}',{players['Hundreds'][i]},'{players['Strike_rate'][i]}',{players['Sixes'][i]},{players['Fours'][i]},'2021-03-22 01:42:03','2021-03-22 01:42:03'), \n")

# for i in range(len(players['Name'])):
#     file.write(
#         f"({i+1},{players['Bowling_innings']},{players['Bowling_average']},{players['']})")
