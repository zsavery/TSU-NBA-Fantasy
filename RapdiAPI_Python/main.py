# %%
import pandas as pd
import rapidapi_nba

if __name__ == "__main__":
    # header
    head = {
        'x-rapidapi-key': "9ab5f1799cmsh27212c7d8f60efep17f457jsn395ab0f973b6",
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }
#%%
    league = rapidapi_nba.get_leagues(head)
    # print(selected_league)

    response_player_league = rapidapi_nba.get_player_by_league(head, selected_league)
    # print(response_player_league.text)

    get_player_league = response_player_league.json()

    get_player_league_filters = get_player_league['api']['filters']
    get_player_league_players = get_player_league['api']['players']
    get_player_league_results = get_player_league['api']['results']
    # print('filters: ', get_player_league_filters)
    # print('players: ', get_player_league_players)
    # print('player & filters: ', get_player_league_results)
    # %%
    # test_frame = pd.DataFrame(data= get_player_league_players)
    # %%
    # test_frame2 = pd.json_normalize(data= get_player_league_players)
    # %%
    # JSON  filter active players
    active_players_json = [x for x in get_player_league_players if x['leagues'][f'{selected_league}']['active'] == '1']
    # %%
    # Data Frame of active players
    # active_players_df1 = pd.DataFrame(data= active_players_json)
    active_players_df2 = pd.json_normalize(data=active_players_json)
    # %%
    # Data Frame of active players ids
    active_players_ids_df2 = pd.DataFrame(active_players_df2["playerId"])
    # %%
    player_ids_lst = [x for x in active_players_ids_df2["playerId"]]
    # print list of player_

# %%
