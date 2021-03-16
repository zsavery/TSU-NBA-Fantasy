import pandas as pd
from datetime import datetime as dt
# Import players from nba_api stats.static
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelogs
from nba_api.stats.endpoints import playercareerstats

import seasons

# %%

def get_player_stats_name(player_name):

    season = seasons.get_season()

    nba_players = players.get_players()
    sel_player = [player for player in nba_players if player['full_name'] == player_name][0]
    career_stats = playercareerstats.PlayerCareerStats(player_id=sel_player['id'])
    df_career_stats = pd.DataFrame(career_stats.get_data_frames()[0])
    # print(df_career_stats)
    # pd.set_option('display.max_columns', None)
    df_career_stats =  df_career_stats.drop(['LEAGUE_ID', 'PLAYER_AGE', 'TEAM_ABBREVIATION'],1)
    print(df_career_stats.tail(1))
    df_season_stats = df_career_stats.query('SEASON_ID == "season"')
    print(df_season_stats)
    # return df_season_stats


# get_player_stats_name('LeBron James')


def get_player_stats_id(id):

    current_day = dt.now().day
    current_month = dt.now().month
    current_year = dt.now().year

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
    print(df_season_stats)
#


# get_player_stats_id()
