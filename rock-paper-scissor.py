class Participant:
    def __init__(self, name):
        self.name = name
        self.__points = 0
        self.choice = ""

    def choose(self):
        self.choice = input("{name}, select rock, scissor, lizard or spock: ".format(name=self.name))
        print("{name} selects {choice}".format(name=self.name, choice=self.choice))

    def to_numerical_choice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
            "lizard": 3,
            "spock": 4
        }
        return switcher[self.choice]

    def get_points(self):
        return self.__points

    def set_points(self, new_point):
        self.__points = new_point


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compare_choices(p1, p2)
        print("Round resulted in a {result}".format(result=self.get_result_as_string(result)))
        if result > 0:
            self.award_points(p1)
        elif result < 0:
            self.award_points(p2)

    def compare_choices(self, p1, p2):
        return self.rules[p1.to_numerical_choice()][p2.to_numerical_choice()]

    def award_points(self, p):
        award = p.get_points() + 1
        p.set_points(award)

    def get_result_as_string(self, result):
        res = {
            0: 'draw',
            1: 'win',
            -1: 'loss'
        }
        return res[result]


class Game:
    def __init__(self):
        self.end_game = False
        self.participant = Participant('Isaias')
        self.second_participant = Participant('Sirak')

    def start(self):
        while not self.end_game:
            GameRound(self.participant, self.second_participant)
            self.check_end_condition()

    def check_end_condition(self):
        answer = input("Continue game y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.second_participant)
            self.check_end_condition()
        else:
            print(
                "Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name=self.participant.name,
                                                                                          p1points=self.participant.get_points(),
                                                                                          p2name=self.second_participant.name,
                                                                                          p2points=self.second_participant.get_points()))
            self.determine_winner()
            self.end_game = True

    def determine_winner(self):
        result_string = "It's a Draw"
        if self.participant.get_points() > self.second_participant.get_points():
            result_string = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.get_points() < self.second_participant.get_points():
            result_string = "Winner is {name}".format(name=self.second_participant.name)

        print(result_string)


game = Game()
game.start()
