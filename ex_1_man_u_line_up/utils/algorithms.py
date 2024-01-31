import random
from typing import List
from utils.mapper import Player, Data

def is_valid_team(players: [Player]) -> bool:
    
    if len(players) > 11:
        print("Mas de 11 jugadores")
        return False
    
    if not had_goalkeper(players):
        print("Does not have goalkeeper")
        return False
    
    # Verify if had four Defenders
    if not verify_positions(players, "Defender", 4):
        print("Does not have enough Defenders")
        return False
    
    # Verify if had three Midfielders
    if not verify_positions(players,"Midfielder", 3 ):
        print("Does not have enough Midfielders")
        return False
    
    # Verify if had three Forwards
    if not verify_positions(players, "Forward", 3):
        print("Does not have enough Forwards")
        return False
    
    return True
    
def had_goalkeper(players:[Player]) -> bool:
    flag = False
    for player in players:
        if player.position == "Goalkeeper":
            flag = True
            break
        
    return flag

def verify_positions(players:[Player], position:str, number:int):
    flag = False
    counter = 0
    for player in players:
        if player.position == position:
            counter +=1
            if counter == number:
                flag = True
                break
    
    return flag

def choice_random_goalkeper(players:[Player]) -> Player:
    goalkeepers = [player for player in players if player.position == "Goalkeeper"]

    if not goalkeepers:
        return None
    
    random_goalkeeper = random.choice(goalkeepers)
    
    return random_goalkeeper

def choice_random_players_by_position(players:[Player], position:str, number:int) -> List[Player]:

    players = [player for  player in players if player.position == position]
    
    if not players:
        return None
    
    random_players = random.sample(players, number)

    return random_players

def generate_random_team(players:[Player]) -> List[Player]:

    team =[]
    
    keeper = choice_random_goalkeper(players)
    team.append(keeper)
    
    defenders = choice_random_players_by_position(players, "Defender", 4)
    team.extend(defenders)
    
    midfielders = choice_random_players_by_position(players, "Midfielder", 3)
    team.extend(midfielders)
    
    fordwards = choice_random_players_by_position(players, "Forward", 3)
    team.extend(fordwards)
    
    if not is_valid_team(team):
        return None
    
    return team

def get_players_by_positions(players:[Player], position:str) -> List[Player]:
    players_by_position = [player for player in players if player.position == position]
     
    if not players_by_position:
        print(f'Do not exists players for this position: {position}')   
        return None
    return players_by_position

def search_player_by_name(players:List[Player], name:str) -> Player:
    for player in players:
        if player.name.strip() == name.strip():
            return player
    return None

def delete_selected_player(players:List[Player], selected_player:Player) -> List[Player]:
    updated_players = [player for player in players if player != selected_player]
    return updated_players

def select_player(players, position, max_selections):
    selected_players = []

    while len(selected_players) < max_selections:
        player_list = get_players_by_positions(players, position)
        names_of_players = [player.name for player in player_list]
        list_str = ' - '.join(names_of_players)
        player_name = input(f"Enter the name of your {position}: {list_str} ")
        player = search_player_by_name(player_list, player_name)

        if player:
            selected_players.append(player)
            print(f"{position} chosen: {player.name}")
            names_selected = [player.name for player in selected_players]
            print("Your current players: ", "  -  ".join(names_selected))
            players = delete_selected_player(players, player)  
        else:
            print(f"Invalid {position} name. Please try again.")

    return selected_players


def get_winner_team(team1:Data, team2:Data) -> (Data,int):
    
    players1 = team1.players
    players2 = team2.players
    
    winner, counter = compare_players(team1, team2)
    return winner, counter
    

def compare_goalkeeper(goalkeeper1:Player, goalkeeper2:Player) -> Player:
    if goalkeeper1.punctuation > goalkeeper2.punctuation:
        return goalkeeper1
    else:
        return goalkeeper2 
    
def compare_players(players1:Data, players2:Data) -> (Data, int):
    count_players_1 = sum([player.punctuation for player in players1.players])
    count_players_2 = sum([player.punctuation  for player in players2.players])
    if count_players_1 > count_players_2:
        return players1, count_players_1
    else:
        return players2, count_players_2
    