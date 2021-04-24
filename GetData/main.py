import pandas as pd
import math
import time

import rapidapi_nba
import create_db
# %%

if __name__ == "__main__":
    # start time
    # create_db.drop()
    # exit()
    start = time.perf_counter()
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    # header
    head = {
        'x-rapidapi-key': "9ab5f1799cmsh27212c7d8f60efep17f457jsn395ab0f973b6",
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }
    # %%
    # Selected League
    # league = rapidapi_nba.get_leagues(head)
    league = "standard"


    # %%
    # Get All Players in Selected League
    players_by_league = rapidapi_nba.get_players_by_league(head, league)

    # %%
    # Filter Players by Activity
    active_players = [x for x in players_by_league if x['leagues']['standard']['active'] == '1']

    # %%

    # Data Frame of Active players
    active_players_df = pd.DataFrame(active_players)
    filter_active_players = active_players_df.loc[active_players_df['startNba'] != '0']
    # %%

    # Data Frame of active players ids
    active_players_name_ids = filter_active_players [['playerId', 'firstName', 'lastName']].copy()

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

    # %%

    for i in range(len(player_ids_lst)):
    # for i in range(50):
        Id = player_ids_lst[i]
        print(f"Getting Stats for player: {Id}")
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
        latest_stat_df.fillna("0")
        x = active_players_name_ids.loc[active_players_name_ids['playerId'] == Id]
        latest_stat_df[["playerId", "teamId", "points", "totReb", "assists", "steals", "turnovers",
                        "blocks"]] = latest_stat_df[["playerId", "teamId", "points", "totReb", "assists", "steals",
                                                     "turnovers", "blocks"]].apply(pd.to_numeric)

        if latest_stat_df['pos'][0] == "":
            latest_stat_df.at[0, 'pos'] = "NA"

        points = latest_stat_df['points'].mean()
        totReb = latest_stat_df['totReb'].mean()
        assists = latest_stat_df['assists'].mean()
        steals = latest_stat_df['steals'].mean()
        blocks = latest_stat_df['blocks'].mean()
        turnovers = latest_stat_df['turnovers'].mean()

        if latest_stat_df['pos'][0] == "":
            latest_stat_df.at[0, 'pos'] = "NA"

        average_stats = average_stats.append({'playerId': latest_stat_df['playerId'][0],
                                              'firstName': x["firstName"].item(),
                                              'lastName': x["lastName"].item(),
                                              'teamId': latest_stat_df['teamId'][0],
                                              'pos': latest_stat_df['pos'][0],
                                              'points': points,
                                              'totReb': totReb,
                                              'assists': assists,
                                              'steals': steals,
                                              'blocks': blocks,
                                              'turnovers': turnovers,
                                              'fantasyPoints': ((points * 1) + (totReb * 1.2) +
                                                                (assists * 1.5) + (steals * 2) +
                                                                (blocks * 2) + (turnovers * -1))
                                              }, ignore_index=True)

    average_stats = average_stats.fillna(0)

    print(average_stats)
    # print(rapidapi_nba.top_five(average_stats))

    #%%
    average_stats.to_csv("average_stats.csv", index=False)
    #%%
    create_db.to_mysql(average_stats)
    #%%
    #%%
    finish = time.perf_counter()  # end time
    print(f"Finished in {round(finish - start, 2)} second(s)")
