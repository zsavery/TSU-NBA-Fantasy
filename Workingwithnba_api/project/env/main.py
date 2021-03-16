# %%

import pandas as pd # Import pandas
import requests     # Improt requests

# Import players from nba_api.stats
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelogs

# File imports
import get_player # 
import seasons

# Comment imports
# from nba_api.stats.endpoints import playerfantasyprofile
# from nba_api.stats.endpoints import franchiseleaders
# from nba_api.stats.endpoints import leaderstiles

# from nba_api.stats.endpoints import playergamelog



# %%


def game_stats(id, seas):
    player_game_logs_df = playergamelogs.PlayerGameLogs(player_id_nullable=id, season_nullable=seas,
                                                        last_n_games_nullable=5, timeout=2000).get_data_frames()

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


# def get_season():
#     current_day = datetime.now().day
#     current_month = datetime.now().month
#     current_year = datetime.now().year
#     season = ""

#     if current_month == 12 and current_day >= 22:
#         season = str(current_year) + '-' + str(current_year + 1)[2:]
#     else:
#         season = str(current_year - 1) + '-' + str(current_year)[2:]

#     return season


# %%
season = seasons.get_season()
# %%
# TODO: fix this function
#       Function Error


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

# TODO: Fix function below
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




# %%
