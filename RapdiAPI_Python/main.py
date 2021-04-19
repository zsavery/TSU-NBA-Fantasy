# %%
# %%

import pandas as pd
import rapidapi_nba

# %%

if __name__ == "__main__":
    # header
    head = {
        'x-rapidapi-key': "9ab5f1799cmsh27212c7d8f60efep17f457jsn395ab0f973b6",
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }
    # %%
    league = rapidapi_nba.get_leagues(head)
    # print(selected_league)
#%%
    players_by_league = rapidapi_nba.get_players_by_league(head, league)

#%%
    # Filter active players
    active_players = [x for x in players_by_league if x['leagues']['standard']['active'] == '1']
#%%
    # Data Frame of active players
    active_players_df = pd.DataFrame(active_players)
#%%
    # Data Frame of active players ids
    active_players_ids_df = pd.DataFrame(active_players_df["playerId"])
#%%
    player_ids_lst = [x for x in active_players_ids_df["playerId"]]

    # print list of player_

#%%
    # Get latest season
    season = rapidapi_nba.get_season(head)

#%%

    # Get stats from player
    player_stats_r = rapidapi_nba.get_player_stats_by_player_id(head, '265')
    player_stats = player_stats_r.json()['api']['statistics']

#%%

    stat_df = pd.json_normalize(player_stats)
    if len(player_stats) >= 5:
        latest_stat_df = pd.json_normalize(player_stats[len(player_stats) - 5:])
    else:
        latest_stat_df = pd.json_normalize(player_stats)
