import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['nationality'],
            player_dict['goals'],
            player_dict['assists']
        )
        if player_dict['nationality'] == "FIN":
            players.append(player)
        else:
            continue
    
    print("Oliot:")
    for player in sorted(players, key=lambda x: x.goals + x.assists, reverse=True):
        print(player)

if __name__ == "__main__":
    main()
