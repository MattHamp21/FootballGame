import random
from players import *


class Game:
    def __init__(self, player_team, cpu_team):
        try:
            self.player_team = player_team
            self.cpu_team = cpu_team
            self.possession = random.choice(['player', 'cpu'])
            self.player_score = 0
            self.cpu_score = 0
            self.yards = 0
            self.yards_to_first_down = 10
            self.yards_to_touchdown = 75
            self.plays = 0
            self.downs = 1
            self.finished = False
        except Exception as e:
            print(f"An error occurred when creating a Game: {str(e)}")

    def end_game(self):
        self.finished = True
        if self.player_score > self.cpu_score:
            print(f"Player team wins! Final score: Player team {self.player_score}, CPU team {self.cpu_score}")
        elif self.player_score < self.cpu_score:
            print(f"CPU team wins! Final score: CPU team {self.cpu_score}, Player team {self.player_score}")
        else:
            print(f"The game is a tie! Final score: Player team {self.player_score}, CPU team {self.cpu_score}")

    def simulate_play(self):
        try:
            self.downs += 1
            self.plays += 1

            # Initialize gained_yards for each play
            gained_yards = 0
            random_factor = random.uniform(2, 3)

            play_type = ''
            player = ''

            if self.possession == 'player':
                play_choices = ['Pass offense', 'Run offense']
                play_probs = [0.75, 0.25] if self.player_team.offense.play_style == 'Pass offense' else [0.25, 0.75]
                selected_play = random.choices(play_choices, weights=play_probs, k=1)[0]

                if selected_play == 'Pass offense':
                    gained_yards = ((self.player_team.offense.qb.accuracy * random.uniform(0.8, 1.2) +
                                     self.player_team.offense.wr.catch * random.uniform(0.8, 1.2)) -
                                    self.cpu_team.defense.pass_def * random.uniform(0.8, 1.2)) * random_factor
                    play_type = 'Pass offense'
                    player = 'Player Quarterback and Wide Receiver'
                else:
                    gained_yards = ((self.player_team.offense.rb.power * random.uniform(0.8, 1.2) +
                                     self.player_team.offense.ol.blocking * random.uniform(0.8, 1.2)) -
                                    self.cpu_team.defense.run_def * random.uniform(0.8, 1.2)) * random_factor
                    play_type = 'Run offense'
                    player = 'Player Running Back and Offensive Line'
            else:
                play_choices = ['Pass offense', 'Run offense']
                play_probs = [0.75, 0.25] if self.cpu_team.offense.play_style == 'Pass offense' else [0.25, 0.75]
                selected_play = random.choices(play_choices, weights=play_probs, k=1)[0]

                if selected_play == 'Pass offense':
                    gained_yards = ((self.cpu_team.offense.qb.accuracy * random.uniform(0.8, 1.2) +
                                     self.cpu_team.offense.wr.catch * random.uniform(0.8, 1.2)) -
                                    self.player_team.defense.pass_def * random.uniform(0.8, 1.2)) * random_factor
                    play_type = 'Pass offense'
                    player = 'CPU Quarterback and Wide Receiver'
                else:
                    gained_yards = ((self.cpu_team.offense.rb.power * random.uniform(0.8, 1.2) +
                                     self.cpu_team.offense.ol.blocking * random.uniform(0.8, 1.2)) -
                                    self.player_team.defense.run_def * random.uniform(0.8, 1.2)) * random_factor
                    play_type = 'Run offense'
                    player = 'CPU Running Back and Offensive Line'

            gained_yards = max(0, round(gained_yards))  # ensure gained yards is non-negative
            self.yards += gained_yards

            self.yards_to_first_down -= gained_yards
            self.yards_to_touchdown -= gained_yards

            if self.yards_to_first_down <= 0:
                self.yards_to_first_down = 10  # Reset yards_to_first_down
                print("First down!")

            if self.yards_to_touchdown <= 0:
                self.yards_to_touchdown = 75  # Reset yards_to_touchdown
                print("Touchdown!")
                if self.possession == 'player':
                    self.player_score += 7
                    self.possession = 'cpu'
                else:
                    self.cpu_score += 7
                    self.possession = 'player'

            print(
                f"Total Plays: {self.plays}, Possession: {self.possession}, Player score: {self.player_score}, CPU score: {self.cpu_score}, Yards Gained This Play: {gained_yards}, Total Yards: {self.yards}, Downs: {self.downs}, Yards until first down: {self.yards_to_first_down} \n , Yards until touchdown: {self.yards_to_touchdown}, Ball Carrier: {player}, Play Type: {play_type}")

            if self.plays >= 60:
                self.end_game()

            return "Play simulation completed"

        except Exception as e:
            print(f"An error occurred while simulating a play: {e}")
