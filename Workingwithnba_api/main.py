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

# player_rank = playerfantasyprofile.PlayerFantasyProfile('203500').get_data_frames()
# print(player_rank)

# find the leader of the selected team w/ the team_id of each stat
# leaders_franchise = franchiseleaders.FranchiseLeaders(1610612739).get_data_frames()
# print(leaders_franchise)

# %%
# create a dataframe

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
def game_stats(id, seas):
    player_game_logs_df = playergamelogs.PlayerGameLogs(player_id_nullable=id, season_nullable=seas,
                                                        last_n_games_nullable=5).get_data_frames()

    new_stats = pd.DataFrame([[id, player_game_logs_df[0].PTS.mean(), player_game_logs_df[0].AST.mean(),
                               player_game_logs_df[0].REB.mean(), player_game_logs_df[0].BLK.mean(),
                               player_game_logs_df[0].STL.mean(), player_game_logs_df[0].TOV.mean()]],
                             columns=["player_id", "PTS", "AST", "REB", "BLK", "STL", "TOV"])

    return new_stats


# x = game_stats(2544, "2020-21")
# df_stats = df_stats.append(x, ignore_index=True)
# print(df_stats)


# x = game_stats(101108, "2020-21")
# df_stats = df_stats.append(x, ignore_index=True)
# print(df_stats)
#
# df_stats = pd.DataFrame(columns=['player_id', 'PTS', 'AST', 'REB', 'BLK', 'STL', 'TOV'])
# print(df_stats)
# %%

df_stats = pd.DataFrame(columns=['player_id', 'PTS', 'AST', 'REB', 'BLK', 'STL', 'TOV'])

# TODO: fix this function
# def func():
#     # Get dict of all players info -> [id, full_name, first_name, last_name, is_active]
#     players_dict = players.get_players()
#     # season = get_season()
#
#     # Temp dataframe
#     # stats = pd.DataFrame(columns=['player_id', 'PTS', 'AST', 'REB', 'BLK', 'STL', 'TOV'])
#
#     # Change dict of all players into a dataframe using pandas
#     df_players = pd.DataFrame.from_dict(players_dict)
#
#     # Filter df_players by only active players
#     df_active_players = pd.DataFrame(df_players.query('is_active == True'))
#
#     # for i in df_active_players.id:
#     #     x = game_stats(int(i), season)
#     #     stats = stats.append(x, ignore_index=True)
#
#     return df_active_players
#
#
# season = get_season()
# active_players = func()
# for i in active_players.id:
#     x = game_stats(int(i), season)
#     df_stats = df_stats.append(x, ignore_index=True)
# df_stats = func()
# print(df_stats)
