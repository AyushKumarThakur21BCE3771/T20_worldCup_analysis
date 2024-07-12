import pandas as pd
import json

# match data transformation

with open('stats_json/match_stats.json') as f_match:
    dataMatch = json.load(f_match)

df_match = pd.DataFrame(dataMatch['matchSummary'])

df_match.rename({'matchId': 'match_id'}, axis = 1, inplace=True)

# exporting match_stats to excel file 

df_match.to_csv('stats_csv/match_stats.csv', index = False)

match_id_dict = {}

for index, row in df_match.iterrows():
    key1 = row['team1'] + ' vs ' + row['team2']
    key2 = row['team2'] + ' vs ' + row['team1']

    match_id_dict[key1] = row["match_id"]
    match_id_dict[key2] = row["match_id"]


# batting data transformation


with open('stats_json/batting_stats.json') as f_batting:
    dataBatting = json.load(f_batting)

    batting_records = []

    for rec in dataBatting:
        batting_records.extend(rec['battingSummary'])

df_batting = pd.DataFrame(batting_records)

df_batting['dismissal'] = df_batting['dismissal'].fillna('')
df_batting['out/not_out'] = df_batting['dismissal'].apply(lambda x: 'out' if pd.notna(x) and x != '' else 'not_out')

df_batting.drop(columns=["dismissal"], inplace=True)

df_batting["match_id"] = df_batting["match"].map(match_id_dict)

# exporting batting_stats to excel file 

df_batting.to_csv('stats_csv/batting_stats.csv', index = False)


# bowling data transformation


with open('stats_json/bowling_stats.json') as f:
    dataBowling = json.load(f)
    bowling_records = []
    for rec in dataBowling:
        bowling_records.extend(rec['bowlingSummary'])

df_bowling = pd.DataFrame(bowling_records)

df_bowling['match_id'] = df_bowling['match'].map(match_id_dict)

# exporting bowling_stats to excel file 

df_bowling.to_csv('stats_csv/bowling_stats.csv', index = False)



# players data transformation
with open('stats_json/player_info.json') as f:
    dataPlayer = json.load(f)

df_players = pd.DataFrame(dataPlayer)

df_players['name'] = df_players['name'].apply(lambda x: x.replace('â€', ''))
df_players['name'] = df_players['name'].apply(lambda x: x.replace('†', ''))
df_players['name'] = df_players['name'].apply(lambda x: x.replace('\xa0', ''))
df_players['description'] = df_players['description'].fillna('')

# exporting bowling_stats to excel file 

df_players.to_csv('stats_csv/players_info.csv', index = False)

