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

# %%
# Get players
player_dict = players.get_players()
df_player_dict = pd.DataFrame.from_dict(player_dict)

# Active players
df_active_players = df_player_dict.query('is_active == True')
# active_players = [player for player in player_dict if player['is_active'] == True]
# active_players_dict = dict()
# for key, value in player_dict
# df_active_players = pd.DataFrame.from_dict(active_players)
# %%
print(df_active_players)
print(df_active_players["id"])

# %%

current_day = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year

if current_month == 12 and current_day >= 22:
    season = str(current_year) + '-' + str(current_year + 1)[2:]
else:
    season = str(current_year - 1) + '-' + str(current_year)[2:]
print(season)
#%%



# %%
def get_player_stats(player_name):

    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year

    if current_month == 12 and current_day >= 22:
        season = str(current_year) + '-' + str(current_year + 1)[2:]
    else:
        season = str(current_year - 1) + '-' + str(current_year)[2:]
    #print(season)

    nba_players = players.get_players()
    sel_player = [player for player in nba_players if player['full_name'] == player_name][0]
    career_stats = playercareerstats.PlayerCareerStats(player_id=sel_player['id'])
    df_career_stats = pd.DataFrame(career_stats.get_data_frames()[0])
    # print(df_career_stats)
    #pd.set_option('display.max_columns', None)
    df_career_stats =  df_career_stats.drop(['LEAGUE_ID', 'PLAYER_AGE', 'TEAM_ABBREVIATION'],1)
    print(df_career_stats.tail(1))
    df_season_stats = df_career_stats.query('SEASON_ID == "season"')
    #print(df_season_stats)


get_player_stats('LeBron James')
# %%
player_rank = playerfantasyprofile.PlayerFantasyProfile('203500').get_data_frames()
print(player_rank)
# %%
player_ids = [player_id for player_id in df_active_players]
# %%
# find the leader of the selected team w/ the team_id of each stat
leaders_franchise = franchiseleaders.FranchiseLeaders(1610612739).get_data_frames()
print(leaders_franchise)
