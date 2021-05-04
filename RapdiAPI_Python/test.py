import mysql.connector
import pandas as pd
import rapidapi_nba
import math
import time
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TSUFAN2021",
    database="mydatabase"
)
mycursor = mydb.cursor()
if mycursor != None:
    print("Connection made!")
sql = "DROP TABLE IF EXISTS Playerstest"
mycursor.execute(sql)
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Playerstest (player_Id VARCHAR(255) PRIMARY KEY,fname VARCHAR(255), lname VARCHAR(255),teamId VARCHAR(255),pos VARCHAR(255),points VARCHAR(255),totReb VARCHAR(255),assists VARCHAR(255),steals VARCHAR(255),blocks VARCHAR(255),turnovers VARCHAR(255),fantasyPoints VARCHAR(255))")
# %%
# %%
if __name__ == "__main__":
    start = time.perf_counter()  # start time
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    # header
    head = {
        'x-rapidapi-key': "9ab5f1799cmsh27212c7d8f60efep17f457jsn395ab0f973b6",
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }
    # %%
    league = rapidapi_nba.get_leagues(head)
    # print(selected_league)

    # %%

    players_by_league = rapidapi_nba.get_players_by_league(head, league)

    # %%

    # Filter active players
    active_players = [x for x in players_by_league if x['leagues']['standard']['active'] == '1']

    # %%

    # Data Frame of active players
    active_players_df = pd.DataFrame(active_players)
    filter_active_players = active_players_df.loc[active_players_df['startNba'] != '0']
    # %%

    # Data Frame of active players ids
    active_players_name_ids = filter_active_players[['playerId', 'firstName', 'lastName']].copy()

    # %%

    player_ids_lst = [x for x in active_players_name_ids["playerId"]]

    # %%

    # Get latest season
    season = rapidapi_nba.get_season(head)

    # %%
    # Set up table for that holds stats that will be displayed
    column_names = ['playerId', 'firstName', 'lastName', 'teamId', 'pos', 'points', 'totReb', 'assists',
                    'steals', 'blocks', 'turnovers', 'fantasyPoints']
    average_stats = pd.DataFrame(columns=column_names)
    add_Player = "REPLACE INTO Playerstest (player_Id,fname, lname,teamId,pos,points,totReb,assists,steals,blocks,turnovers,fantasyPoints) VALUES (%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    # %%
    # Get stats from player from player with id '265' ie LeBron James
    for i in range(len(player_ids_lst)):
    # for i in range(10):
        Id = player_ids_lst[i]
        player_stats_r = rapidapi_nba.get_player_stats_by_player_id(head, Id)
        player_stats = player_stats_r.json()['api']['statistics']
        stat_df = pd.json_normalize(player_stats)
        if len(player_stats) >= 5:
            latest_stat_df = pd.json_normalize(player_stats[-6:-1])
        elif len(player_stats) == 0 or math.isnan(['points'] == True):
            # print("Skip")
            continue
        else:
            latest_stat_df = pd.json_normalize(player_stats)

        # print(type(latest_stat_df['points'][0]))
        x = active_players_name_ids.loc[active_players_name_ids['playerId'] == Id]
        latest_stat_df[["points", "totReb", "assists", "steals", "turnovers", "blocks"]] = latest_stat_df[
            ["points", "totReb", "assists", "steals", "turnovers", "blocks"]].apply(pd.to_numeric)
        latest_stat_df['playerId'].fillna("NA", inplace=True)
        latest_stat_df['teamId'].fillna('NA', inplace=True)

        latest_stat_df['points'].fillna(0, inplace=True)
        latest_stat_df['totReb'].fillna(0, inplace=True)
        latest_stat_df['assists'].fillna(0, inplace=True)
        latest_stat_df['steals'].fillna(0, inplace=True)
        latest_stat_df['turnovers'].fillna(0, inplace=True)
        latest_stat_df['blocks'].fillna(0, inplace=True)

        #     # TODO: Add Player name to columns
        #     # print(type(latest_stat_df['points'][0]))
        if latest_stat_df['pos'][0] == "":
            latest_stat_df.at[0, 'pos'] = "NA"
        if latest_stat_df['pos'][0] == "":
            latest_stat_df.at[0, 'pos'] = "NA"
        fantasy = ((latest_stat_df['points'].mean() * 1) +
                   (latest_stat_df['totReb'].mean() * 1.2) +
                   (latest_stat_df['assists'].mean() * 1.5) +
                   (latest_stat_df['steals'].mean() * 2) +
                   (latest_stat_df['blocks'].mean() * 2) +
                   (latest_stat_df['turnovers'].mean() * -1))
        average_stats = (
            latest_stat_df['playerId'][0], x["firstName"].item(), x["lastName"].item(), latest_stat_df['teamId'][0],
            latest_stat_df['pos'][0], round(latest_stat_df['points'].mean(), 2),
            round(latest_stat_df['totReb'].mean(), 2),
            round(latest_stat_df['assists'].mean(), 2), round(latest_stat_df['steals'].mean(), 2),
            round(latest_stat_df['blocks'].mean(), 2),
            round(latest_stat_df['turnovers'].mean(), 2), round(fantasy, 2))

        if average_stats[3] is None or average_stats[3] == '':
            average_stats[3] = 'NA'
        if average_stats[4] is None or average_stats[4] == '':
            average_stats[4] = 'NA'

        average_stats = [str(x) for x in average_stats]
        mycursor.execute(add_Player, average_stats)
        average_stats.clear()

    # %%

    mydb.commit()
