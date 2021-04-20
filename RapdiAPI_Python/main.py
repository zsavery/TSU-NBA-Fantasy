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

    # %%

    players_by_league = rapidapi_nba.get_players_by_league(head, league)

    # %%

    # Filter active players
    active_players = [x for x in players_by_league if x['leagues']['standard']['active'] == '1']

    # %%

    # Data Frame of active players
    active_players_df = pd.DataFrame(active_players)
    # %%

    # Data Frame of active players ids
    active_players_name_ids = active_players_df[['playerId', 'firstName', 'lastName']].copy()

    # %%

    player_ids_lst = [x for x in active_players_name_ids["playerId"]]
    print(player_ids_lst)
    # print list of player_

    # %%

    # Get latest season
    season = rapidapi_nba.get_season(head)

    # %%
    # Set up table for that holds stats that will be displayed
    column_names = ['playerId', 'teamId', 'pos', 'points', 'totReb', 'assists',
                    'steals', 'blocks', 'turnovers', 'fantasyPoints']
    average_stats = pd.DataFrame(columns=column_names)

    # %%
    # Get stats from player from player with id '265' ie LeBron James
    player_stats_r = rapidapi_nba.get_player_stats_by_player_id(head, '265')
    player_stats = player_stats_r.json()['api']['statistics']
    stat_df = pd.json_normalize(player_stats)
    if len(player_stats) >= 5:
        latest_stat_df = pd.json_normalize(player_stats[-6:-1])
    else:
        latest_stat_df = pd.json_normalize(player_stats)

    # print(type(latest_stat_df['points'][0]))

    latest_stat_df[["points", "totReb", "assists", "steals", "turnovers", "blocks"]] = latest_stat_df[
        ["points", "totReb", "assists", "steals", "turnovers", "blocks"]].apply(pd.to_numeric)

#     # TODO: Add Player name to columns
#     # print(type(latest_stat_df['points'][0]))
    average_stats = average_stats.append({'playerId': latest_stat_df['playerId'][0],
                                          'teamId': latest_stat_df['teamId'][0],
                                          'pos': latest_stat_df['pos'][0],
                                          'points': latest_stat_df['points'].mean(),
                                          'totReb': latest_stat_df['totReb'].mean(),
                                          'assists': latest_stat_df['assists'].mean(),
                                          'steals': latest_stat_df['steals'].mean(),
                                          'blocks': latest_stat_df['blocks'].mean(),
                                          'turnovers': latest_stat_df['turnovers'].mean(),
                                          'fantasyPoints': ((latest_stat_df['points'].mean() * 1) +
                                                            (latest_stat_df['totReb'].mean() * 1.2) +
                                                            (latest_stat_df['assists'].mean() * 1.5) +
                                                            (latest_stat_df['steals'].mean() * 2) +
                                                            (latest_stat_df['blocks'].mean() * 2) +
                                                            (latest_stat_df['turnovers'].mean() * -1))
                                          },
                                         ignore_index=True)
    print(average_stats)

# %%
#
#     average_stats = pd.DataFrame(columns=column_names)
# %%
#     # Try the same as above except in a loop
#     completed_player = 0
#     for player_id in player_ids_lst[0:300]:
#         # Get stats from player
#         player_stats_r = rapidapi_nba.get_player_stats_by_player_id(head, player_id)
#         player_stats = player_stats_r.json()['api']['statistics']
#         stat_df = pd.json_normalize(player_stats)
#         if len(player_stats) >= 5:
#             latest_stat_df = pd.json_normalize(player_stats[-6:-1])
#         else:
#             latest_stat_df = pd.json_normalize(player_stats)
#
#         latest_stat_df[["points", "totReb", "assists", "steals", "turnovers", "blocks"]] = latest_stat_df[
#             ["points", "totReb", "assists", "steals", "turnovers", "blocks"]].apply(pd.to_numeric)
#
#         average_stats = average_stats.append({'playerId': latest_stat_df['playerId'][0],
#                                               'teamId': latest_stat_df['teamId'][0],
#                                               'pos': latest_stat_df['pos'][0],
#                                               'points': latest_stat_df['points'].mean(),
#                                               'totReb': latest_stat_df['totReb'].mean(),
#                                               'assists': latest_stat_df['assists'].mean(),
#                                               'steals': latest_stat_df['steals'].mean(),
#                                               'blocks': latest_stat_df['blocks'].mean(),
#                                               'turnovers':latest_stat_df['turnovers'].mean(),
#                                               'fantasyPoints': ((latest_stat_df['points'].mean() * 1) +
#                                                                 (latest_stat_df['totReb'].mean() * 1.2) +
#                                                                 (latest_stat_df['assists'].mean() * 1.5) +
#                                                                 (latest_stat_df['steals'].mean() * 2) +
#                                                                 (latest_stat_df['blocks'].mean() * 2) +
#                                                                 (latest_stat_df['turnovers'].mean() * -1))},
#                                              ignore_index=True)
#         completed_player += 1
#         print(f"Completed player {completed_player} of {len(player_ids_lst)}")
#     print(average_stats)


