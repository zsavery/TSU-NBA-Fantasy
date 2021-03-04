# %%
# Import pandas

import pandas as pd
from datetime import datetime
# Import players from nba_api stats.static
from nba_api.stats.static import players
# from nba_api.stats.endpoints import playercareerstats
# from nba_api.stats.endpoints import playerfantasyprofile
# from nba_api.stats.endpoints import franchiseleaders
# from nba_api.stats.endpoints import leaderstiles
from nba_api.stats.endpoints import playergamelogs
# from nba_api.stats.endpoints import playergamelog

# %%

# def get_player_stats_name(player_name):
#
#     current_day = datetime.now().day
#     current_month = datetime.now().month
#     current_year = datetime.now().year
#
#     if current_month == 12 and current_day >= 22:
#         season = str(current_year) + '-' + str(current_year + 1)[2:]
#     else:
#         season = str(current_year - 1) + '-' + str(current_year)[2:]
#     # print(season)
#
#     nba_players = players.get_players()
#     sel_player = [player for player in nba_players if player['full_name'] == player_name][0]
#     career_stats = playercareerstats.PlayerCareerStats(player_id=sel_player['id'])
#     df_career_stats = pd.DataFrame(career_stats.get_data_frames()[0])
#     # print(df_career_stats)
#     # pd.set_option('display.max_columns', None)
#     df_career_stats =  df_career_stats.drop(['LEAGUE_ID', 'PLAYER_AGE', 'TEAM_ABBREVIATION'],1)
#     print(df_career_stats.tail(1))
#     df_season_stats = df_career_stats.query('SEASON_ID == "season"')
#     # print(df_season_stats)
#
#
# # get_player_stats_name('LeBron James')


# def get_player_stats_id(id):
#
#     current_day = datetime.now().day
#     current_month = datetime.now().month
#     current_year = datetime.now().year
#
#     if current_month == 12 and current_day >= 22:
#         season = str(current_year) + '-' + str(current_year + 1)[2:]
#     else:
#         season = str(current_year - 1) + '-' + str(current_year)[2:]
#     # print(season)
#
#     career_stats = playercareerstats.PlayerCareerStats(player_id=id)
#     df_career_stats = pd.DataFrame(career_stats.get_data_frames()[0])
#     # print(df_career_stats)
#     # pd.set_option('display.max_columns', None)
#     df_career_stats =  df_career_stats.drop(['LEAGUE_ID', 'PLAYER_AGE', 'TEAM_ABBREVIATION'],1)
#     print(df_career_stats.tail(1))
#     df_season_stats = df_career_stats.query('SEASON_ID == "season"')
#     # print(df_season_stats)
#
#
# # get_player_stats_id()

# %%


def game_stats(id, seas):
    player_game_logs_df = playergamelogs.PlayerGameLogs(player_id_nullable=id, season_nullable=seas,
                                                        last_n_games_nullable=5).get_data_frames()

    new_stats = pd.DataFrame([[id, player_game_logs_df[0].PTS.mean(), player_game_logs_df[0].AST.mean(),
                               player_game_logs_df[0].REB.mean(), player_game_logs_df[0].BLK.mean(),
                               player_game_logs_df[0].STL.mean(), player_game_logs_df[0].TOV.mean()]],
                             columns=["player_id", "PTS", "AST", "REB", "BLK", "STL", "TOV"])
    new_row = new_stats.to_dict()

    return new_row



# %%
def getplayerids():
    # Get dict of all players info -> [id, full_name, first_name, last_name, is_active]
    players_dict = players.get_active_players()
    return players_dict


player_dict = getplayerids()
# %%
player_ids = [x['id'] for x in player_dict]


# %%


# %%


def get_season():
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year
    season = ""

    if current_month == 12 and current_day >= 22:
        season = str(current_year) + '-' + str(current_year + 1)[2:]
    else:
        season = str(current_year - 1) + '-' + str(current_year)[2:]

    return season


# %%
season = get_season()

# %%
# TODO: fix this function
#       Funtion Error


# def func(ids, seas):
#     # Temp dataframe
#     stats = pd.DataFrame(columns=['player_id', 'PTS', 'AST', 'REB', 'BLK', 'STL', 'TOV'])
#
#     for i in ids:
#         x = game_stats(i, seas)
#         stats = stats.append(x, ignore_index=True)
#
#     return stats

# df_stats = func(player_ids, season)
# print(df_stats)
# %%

# y = game_stats(player_ids[12], season)
# df_stats = df_stats.append(y, ignore_index=True)

# %%

df_stats = pd.DataFrame(columns=['player_id', 'PTS', 'AST', 'REB', 'BLK', 'STL', 'TOV'])

# %%

# TODO: Fix funtion below
# ErrorL
# raise ReadTimeout(e, request=request)
# requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='stats.nba.com', port=443): Read timed out. (read timeout=30)
count = 0
limit = 9
while limit < len(player_ids):
    for i in player_ids:
        if count > limit:
            break
        else:
            x = game_stats(i, season)
            df_stats = df_stats.append(x, ignore_index=True)
            count += 1
    if (len(player_ids) - 9) > 0:
        limit += 9
    elif len(player_ids) == limit:
        break
    else:
        limit += (len(player_ids) - limit)




