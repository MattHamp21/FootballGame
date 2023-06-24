import random
from players import *
from game import *


def generate_random_values():
    return random.randint(2, 5), random.randint(2, 5), random.randint(2, 5), random.randint(2, 5), random.randint(2,
                                                                                                                  5), random.randint(
        2, 5), random.randint(2, 5)


def create_random_player():
    try:
        accuracy, evade, speed, power, catch, blocking, after_catch = generate_random_values()
        qb = Quarterback(accuracy, evade)
        rb = RunningBack(speed, power)
        wr = WideReceiver(speed, catch, after_catch)
        ol = OLine(blocking)
        return qb, rb, wr, ol
    except Exception as e:
        print(f"An error occurred while creating random player: {str(e)}")


def select_difficulty():
    try:
        difficulty = input("Select difficulty (Easy, Medium, Hard): ")
        if difficulty == "Easy":
            return 35
        elif difficulty == "Medium":
            return 25
        else:
            return 15
    except Exception as e:
        print(f"An error occurred while selecting difficulty: {str(e)}")


def select_play_style():
    try:
        return input("Select play style (Pass offense, Run Offense, Balanced): ")
    except Exception as e:
        print(f"An error occurred while selecting play style: {str(e)}")


def assign_points(player_name, points, *attributes):
    print(f"Assign points to your {player_name}:")
    player_points = {}
    for attribute in attributes:
        while True:
            try:
                assigned_points = int(input(f"Enter points for {attribute} ({points} points left): "))
                if 0 <= assigned_points <= 5 and assigned_points <= points:
                    points -= assigned_points
                    player_points[attribute] = assigned_points
                    break
                else:
                    print("Invalid point assignment, please try again.")
            except ValueError:
                print("Please input a number.")
            except Exception as e:
                print(f"An error occurred while assigning points: {str(e)}")
    return player_points, points


def make_team():
    try:
        points = select_difficulty()
        print(
            "You have {} points to assign to your team. You are only allowed to assign 5 points to each attribute".format(
                points))

        qb_points, points = assign_points("Quarterback", points, "Accuracy", "Evade")
        rb_points, points = assign_points("Running Back", points, "Speed", "Power")
        wr_points, points = assign_points("Wide Receiver", points, "Speed", "Catch", "After Catch")
        ol_points, points = assign_points("Offensive Line", points, "Blocking")

        player_qb = Quarterback(qb_points["Accuracy"], qb_points["Evade"])
        player_rb = RunningBack(rb_points["Speed"], rb_points["Power"])
        player_wr = WideReceiver(wr_points["Speed"], wr_points["Catch"], wr_points["After Catch"])
        player_ol = OLine(ol_points["Blocking"])

        player_play_style = select_play_style()
        player_offense = Offense(player_qb, player_rb, player_wr, player_ol, player_play_style)
        player_defense = Defense(points // 2, points // 2,
                                 player_play_style)  # New - divide remaining points evenly between pass_def and run_def

        player_team = Team(player_offense, player_defense)
        return player_team
    except Exception as e:
        print(f"An error occurred while making team: {str(e)}")


def create_teams():
    try:
        player_team = make_team()

        cpu_qb, cpu_rb, cpu_wr, cpu_ol = create_random_player()
        cpu_play_style = random.choice(["Pass offense", "Run offnese", "balanced"])
        cpu_offense = Offense(cpu_qb, cpu_rb, cpu_wr, cpu_ol, cpu_play_style)
        cpu_defense = Defense(random.randint(2, 5), random.randint(2, 5), cpu_play_style)
        cpu_team = Team(cpu_offense, cpu_defense)

        return player_team, cpu_team
    except Exception as e:
        print(f"An error occurred while creating teams: {str(e)}")


def play_game():
    try:
        player_team, cpu_team = create_teams()
        game = Game(player_team, cpu_team)

        for i in range(60):
            print(game.simulate_play())
    except Exception as e:
        print(f"An error occurred while playing game: {str(e)}")


play_game()
