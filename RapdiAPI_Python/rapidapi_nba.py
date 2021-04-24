import requests
from requests import Response


def get_leagues(header):
    # Get leagues
    url = "https://api-nba-v1.p.rapidapi.com/leagues/"
    response = requests.request("GET", url, headers=header)
    leagues = response.json()
    selected_league = leagues['api']['leagues'][3]  # selected standard league
    return selected_league


def get_players_by_league(header, league):
    # Get player by league
    url = f"https://api-nba-v1.p.rapidapi.com/players/league/{league}"
    response = requests.request("GET", url, headers=header)
    get_players_json = response.json()
    get_players = get_players_json['api']['players']
    return get_players


def get_player_by_player_id(header, player_id) -> Response:
    url = f"https://api-nba-v1.p.rapidapi.com/players/playerId/{player_id}"
    response = requests.request("GET", url, headers=header)
    return response


def get_player_by_last_name(header, last_name) -> Response:
    url = f"https://api-nba-v1.p.rapidapi.com/players/lastName/{last_name}"
    response = requests.request("GET", url, headers=header)
    return response


def get_player_by_first_name(header, first_name) -> Response:
    url = f"https://api-nba-v1.p.rapidapi.com/players/firstName/{first_name}"
    response = requests.request("GET", url, headers=header)
    return response


def get_player_stats_by_player_id(header, player_id):
    url = f"https://api-nba-v1.p.rapidapi.com/statistics/players/playerId/{player_id}"
    response = requests.request("GET", url, headers=header)

    return response


def get_season(header):
    url = "https://api-nba-v1.p.rapidapi.com/seasons/"
    response = requests.request("GET", url, headers=header)
    seasons_json = response.json()
    current_season = seasons_json['api']['seasons'][-1]
    return current_season


