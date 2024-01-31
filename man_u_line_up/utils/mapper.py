class Player:
    def __init__(self, name: str, punctuation: int, position: str) -> None:
        self.name = name
        self.punctuation = punctuation
        self.position = position

    @staticmethod
    def from_dict(obj: any) -> 'Player':
        name = obj.get("name")
        punctuation = obj.get("punctuation")
        position = obj.get("position")
        
        return Player(name=name, punctuation=punctuation, position=position)

class Data:
    def __init__(self, team: str, players: [Player]) -> None:
        self.team = team
        self.players = players
    
    @staticmethod
    def from_dict(obj: any) -> 'Data':
        team = obj.get("team")
        players_data = obj.get("players", [])
        players = [Player.from_dict(player) for player in players_data]
        
        return Data(team=team, players=players)
