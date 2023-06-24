import unittest
from players import *
from main import *  # I'm assuming that your main code is in a file named "main.py"

class TestGame(unittest.TestCase):
    def setUp(self):
        # Initialize the game
        qb = Player(power=3, accuracy=4)
        wr = Player(power=3, accuracy=3)
        rb = Player(power=4, accuracy=3)
        ol = Player(power=3, accuracy=4)

        offense = Offense(qb=qb, wr=wr, rb=rb, ol=ol, play_style='Pass offense')
        defense = Defense(pass_def=4, run_def=4, play_style='balanced')

        team1 = Team(offense=offense, defense=defense)
        team2 = Team(offense=offense, defense=defense)

        self.game = Game(player_team=team1, cpu_team=team2)

    def test_simulate_play(self):
        self.game.simulate_play()
        self.assertTrue(self.game.plays > 0)



    def test_end_game(self):
        self.game.plays = 60
        self.game.end_game()
        self.assertTrue(self.game.finished)

if __name__ == '__main__':
    unittest.main()
