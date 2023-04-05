class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]

    @classmethod
    def get_team(cls, team_list):
        new_list = []
        for dict in team_list:
            new_list.append(Player(dict))
        return new_list


kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
        "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

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
    "age":32,
        "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33,
        "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
	"name": "Joel Embiid", 
	"age":32,
        "position": "Power Foward", 
	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# new_team = []

# for dict in players:
#     new_team.append(Player(dict))

# print(new_team[0].age)

team1 = Player.get_team(players)
for player in team1:
    print(player.name)