import random

class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience

class Team:
    def __init__(self, players):
        self.players = players
        self.captain = None
        self.batting_order = players.copy()
        self.current_batsmen = []

    def select_captain(self, player):
        self.captain = player

    def next_player(self):
        # logic to select next player
        if len(self.batting_order) > 0:
            next_player = self.batting_order.pop(0)
            self.current_batsmen.append(next_player)
            return next_player
        else:
            return None

    def choose_bowler(self):
        # logic to choose bowler
        return random.choice(self.players)

class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

class Umpire:
    def __init__(self):
        self.score = 0
        self.wickets = 0
        self.overs = 0

    def predict_outcome(self, player):
        # logic to predict outcome
        batting_prob = player.batting
        bowling_prob = player.bowling
        fielding_prob = player.fielding
        running_prob = player.running

        # Calculate outcome based on probabilities
        outcome = random.choices(
            ["boundary", "out", "run"],
            weights=[batting_prob, 1 - batting_prob, running_prob],
            k=1
        )[0]

        return outcome

class Commentator:
    def __init__(self):
        pass

    def comment(self, event):
        # logic to comment on event
        print(event)

class Match:
    def __init__(self, teams, field, umpire, commentator):
        self.teams = teams
        self.field = field
        self.umpire = umpire
        self.commentator = commentator
        self.current_batting_team = None
        self.current_bowling_team = None

    def start_match(self):
        # logic to start match
        self.current_batting_team = self.teams[0]
        self.current_bowling_team = self.teams[1]
        self.current_batting_team.select_captain(random.choice(self.current_batting_team.players))
        self.current_bowling_team.select_captain(random.choice(self.current_bowling_team.players))
        self.commentator.comment("Match started!")

    def change_innings(self):
        # logic to change innings
        self.current_batting_team, self.current_bowling_team = self.current_bowling_team, self.current_batting_team
        self.current_batting_team.select_captain(random.choice(self.current_batting_team.players))
        self.current_bowling_team.select_captain(random.choice(self.current_bowling_team.players))
        self.commentator.comment("Innings changed!")

    def end_match(self):
        # logic to end match
        self.commentator.comment("Match ended!")

    def simulate_ball(self):
        batsman = self.current_batting_team.next_player()
        bowler = self.current_bowling_team.choose_bowler()

        outcome = self.umpire.predict_outcome(batsman)

        if outcome == "boundary":
            self.umpire.score += 4
            self.commentator.comment(f"{batsman.name} hit a boundary!")
        elif outcome == "out":
            self.umpire.wickets += 1
            self.commentator.comment(f"{batsman.name} got out!")
        elif outcome == "run":
            self.umpire.score += 1
            self.commentator.comment(f"{batsman.name} scored a run!")

        self.commentator.comment(f"Score: {self.umpire.score}/{self.umpire.wickets}")

        if self.umpire.wickets >= 10:
            self.end_match()
        elif self.umpire.overs >= 50:
            self.change_innings()

# Example usage
player1 = Player("MS Dhoni", 0.2, 0.8, 0.99, 0.8, 0.9)
player2 = Player("Virat Kohli", 0.1, 0.9, 0.95, 0.7, 0.8)
team1 = Team([player1, player2])
team2 = Team([player1, player2])
field = Field("large", 0.8, "dry", 0.1)
umpire = Umpire()
commentator = Commentator()
match = Match([team1, team2], field, umpire, commentator)
match.start_match()
match.simulate_ball()
