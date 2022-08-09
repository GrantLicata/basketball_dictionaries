from unicodedata import name


players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]

    # Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects. Be sure to test your method!

    @classmethod
    def get_team(cls, team_list):
        my_team = []
        for players in range(len(team_list)):
            player_instance = Player(team_list[players])
            my_team.append(player_instance)
            print(my_team[players].name)
            return my_team



# Create player instances for each of: Kevin, Jason, Kyrie
player_kevin = Player(players[0])
player_jason = Player(players[1])
player_kyrie = Player(players[2])

# Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.


def populate_players(players_list):
    my_team = []
    for players in range(len(players_list)):
        player_instance = Player(players_list[players])
        my_team.append(player_instance)
        print(my_team[players].name)

populate_players(players)

Player.get_team(players)