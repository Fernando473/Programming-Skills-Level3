import os
from typing import List
from services.teams import get_teams
from utils.algorithms import   generate_random_team, is_valid_team, select_player, get_winner_team
from utils.mapper import Data, Player
from views.line_up import display_lineup


file_path = os.path.abspath("man_u_line_up\source\data.json")

    
def main():
    
    tot , man_u = get_teams(file_path)
    players = tot.players
    tottenham_team = generate_random_team(players)
    manchester_team = man_u.players
    manchester_team_selected = List[Player]
    
    display_lineup(tottenham_team,"Tottenham Hotspur")
    winner = False
    while not winner:
        goalkeeper = select_player(manchester_team, 'Goalkeeper', 1)
        
        defenders = select_player(manchester_team, 'Defender', 4)
        
        midfielders= select_player(manchester_team, 'Midfielder', 3)
        
        forwards = select_player(manchester_team, 'Forward', 3)
        
        manchester_team_selected = goalkeeper + defenders + midfielders + forwards
        
        if not is_valid_team(manchester_team_selected):
            print("Your team selected is not a valid team. Try again")
        
        print("Es un equipo válido ", end=" ")
        
        display_lineup(tottenham_team, "Tottenham Hotspur")
        display_lineup(manchester_team_selected, "Manchester United")
        
        print("Iniciando Comparacion de equipos.........",end= " ")
        
        team_winner, counter = get_winner_team(Data("Tottenham Hotspur", tottenham_team), Data("Manchester United", manchester_team_selected))
        
        print(f'{team_winner.team} points: {counter}')
        
        if team_winner.team == "Manchester United":
            winner = True
            return winner
        else:
            print("Your team selected is not a winner. Try Again")

             
    
main()