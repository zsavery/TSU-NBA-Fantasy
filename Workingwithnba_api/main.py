# %%
# Import pandas

import pandas as pd
from datetime import datetime
# Import players from nba_api stats.static
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playerfantasyprofile
from nba_api.stats.endpoints import franchiseleaders
from nba_api.stats.endpoints import leaderstiles
from nba_api.stats.endpoints import playergamelogs
from nba_api.stats.endpoints import playergamelog

# %%
# Get players
player_dict = players.get_players()  # get the list of nba players as a dict
df_player_dict = pd.DataFrame.from_dict(player_dict)  # get the data frame of nba players using pandas
# %%
# Active players
#df_active_players = df_player_dict.query('is_active == True')  # active nba players data frame
df_player_players = df_player_dict.filter(df_player_dict["is_active" == True])
# %%
# print active player data frame
# print(df_active_players)
# %%
# print the column
print(df_active_players["id"])
# %%

# current_day = datetime.now().day
# current_month = datetime.now().month
# current_year = datetime.now().year
#
# if current_month == 12 and current_day >= 22:
#     season = str(current_year) + '-' + str(current_year + 1)[2:]
# else:
#     season = str(current_year - 1) + '-' + str(current_year)[2:]
# print(season)

# %%


def get_player_stats_name(player_name):

    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year

    if current_month == 12 and current_day >= 22:
        season = str(current_year) + '-' + str(current_year + 1)[2:]
    else:
        season = str(current_year - 1) + '-' + str(current_year)[2:]
    # print(season)

    nba_players = players.get_players()
    sel_player = [player for player in nba_players if player['full_name'] == player_name][0]
    career_stats = playercareerstats.PlayerCareerStats(player_id=sel_player['id'])
    df_career_stats = pd.DataFrame(career_stats.get_data_frames()[0])
    # print(df_career_stats)
    # pd.set_option('display.max_columns', None)
    df_career_stats =  df_career_stats.drop(['LEAGUE_ID', 'PLAYER_AGE', 'TEAM_ABBREVIATION'],1)
    print(df_career_stats.tail(1))
    df_season_stats = df_career_stats.query('SEASON_ID == "season"')
    # print(df_season_stats)

get_player_stats_name('LeBron James')

# %%


def get_player_stats_id(id):

    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year

    if current_month == 12 and current_day >= 22:
        season = str(current_year) + '-' + str(current_year + 1)[2:]
    else:
        season = str(current_year - 1) + '-' + str(current_year)[2:]
    # print(season)

    career_stats = playercareerstats.PlayerCareerStats(player_id=id)
    df_career_stats = pd.DataFrame(career_stats.get_data_frames()[0])
    # print(df_career_stats)
    # pd.set_option('display.max_columns', None)
    df_career_stats =  df_career_stats.drop(['LEAGUE_ID', 'PLAYER_AGE', 'TEAM_ABBREVIATION'],1)
    print(df_career_stats.tail(1))
    df_season_stats = df_career_stats.query('SEASON_ID == "season"')
    # print(df_season_stats)


get_player_stats_id(2544)


# %%
player_rank = playerfantasyprofile.PlayerFantasyProfile('203500').get_data_frames()
print(player_rank)
# %%
player_ids = [player_id for player_id in df_active_players]
# %%
# find the leader of the selected team w/ the team_id of each stat
leaders_franchise = franchiseleaders.FranchiseLeaders(1610612739).get_data_frames()
print(leaders_franchise)


# %%
player_game_log_dict = playergamelog.PlayerGameLog(player_id= 2544, season=2020).get_normalized_dict()
# %%
df_player_game_log = pd.DataFrame.from_dict(player_game_log_dict)

# %%
player_game_logs_df = playergamelogs.PlayerGameLogs(player_id_nullable=2544,
                                                      season_nullable="2020-21",
                                                      last_n_games_nullable=5).get_data_frames()
# %%
player_game_logs_json = playergamelogs.PlayerGameLogs(player_id_nullable=2544,
                                                      season_nullable="2020-21",
                                                      last_n_games_nullable=1).get_json()
# %%
#df_player_game_logs = pd.DataFrame.from_dict(player_game_logs_dict)
df = pd.json_normalize(player_game_logs_json, record_path=['games'])

# %%
print(player_game_logs_df[0].PTS.mean(),
      player_game_logs_df[0].AST.mean(),
      player_game_logs_df[0].REB.mean(),
      player_game_logs_df[0].BLK.mean(),
      player_game_logs_df[0].STL.mean(),
      player_game_logs_df[0].TOV.mean())
