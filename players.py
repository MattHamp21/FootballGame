import random


class Player:
    def __init__(self, speed=0, power=0, accuracy=0, evade=0, catch=0, blocking=0, after_catch=0):
        try:
            self.speed = speed
            self.power = power
            self.accuracy = accuracy
            self.evade = evade
            self.catch = catch
            self.blocking = blocking
            self.after_catch = after_catch
        except Exception as e:
            print(f"An error occurred when creating a Player: {str(e)}")


class Quarterback(Player):
    def __init__(self, accuracy, evade):
        super().__init__(accuracy=accuracy, evade=evade)


class RunningBack(Player):
    def __init__(self, speed, power):
        super().__init__(speed=speed, power=power)


class WideReceiver(Player):
    def __init__(self, speed, catch, after_catch):
        super().__init__(speed=speed, catch=catch, after_catch=after_catch)


class OLine(Player):
    def __init__(self, blocking):
        super().__init__(blocking=blocking)


class Offense:
    def __init__(self, qb, rb, wr, ol, play_style):
        self.qb = qb
        self.rb = rb
        self.wr = wr
        self.ol = ol
        self.play_style = play_style


class Defense:
    def __init__(self, pass_def, run_def, play_style):
        self.pass_def = pass_def
        self.run_def = run_def
        self.play_style = play_style


class Team:
    def __init__(self, offense, defense):
        self.offense = offense
        self.defense = defense
