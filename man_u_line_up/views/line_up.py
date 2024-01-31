from utils.mapper import Player

def display_lineup(players:[Player], team:str):
    goalkeepers = [player for player in players if player.position == "Goalkeeper"]
    defenders = [player for player in players if player.position == "Defender"]
    midfielders = [player for player in players if player.position == "Midfielder"]
    forwards = [player for player in players if player.position == "Forward"]

    print(f"Alineación {team} 4-3-3")
    print(f"Portero: {goalkeepers[0].name} {goalkeepers[0].punctuation} pts")

    print("\nDefensores:")
    for defender in defenders:
        print(f"{defender.position} {defender.name} {defender.punctuation} pts")

    print("\nCentrocampistas:")
    for midfielder in midfielders:
        print(f"{midfielder.position} {midfielder.name} {midfielder.punctuation} pts")

    print("\nDelanteros:")
    for forward in forwards:
        print(f"{forward.position} {forward.name} {forward.punctuation} pts")
