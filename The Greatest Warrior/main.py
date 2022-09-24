class Warrior:

    def __init__(self):

        self.level = 1

        self.all_ranks = [
            "Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
            "Elite", "Conqueror", "Champion", "Master", "Greatest"
        ]

        self.rank = self.all_ranks[0]
        self.experience = 100
        self.achievements = []

    def check_rank(self):
        if len(str(self.level)) > 1 and self.level < 100:
            index = int(str(self.level)[0])
            self.rank = self.all_ranks[index]
        if self.level == 100:
            self.rank = self.all_ranks[-1]

    def check_level(self):
        if self.level < 100:
            self.level = self.experience // 100
        else:
            self.level = 100

    def add_experience(self, gained_experience):
        exp_sum = self.experience + gained_experience
        if exp_sum > 10000:
            self.experience = 10000
        else:
            self.experience = exp_sum
        self.check_level()
        self.check_rank()

    def training(self, training_list):
        description = training_list[0]
        experience = training_list[1]
        level = training_list[2]
        if self.level >= level:
            self.add_experience(experience)
            self.achievements.append(description)
            return description
        else:
            return "Not strong enough"

    def check_opponent_rank_can_fight(self, opponent_lvl):
        opponent_rank = "Pushover"
        if len(str(opponent_lvl)) > 1 and opponent_lvl < 100:
            index = int(str(opponent_lvl)[0])
            opponent_rank = self.all_ranks[index]
        if opponent_lvl == 100:
            opponent_rank = self.all_ranks[-1]
        rank_diff = self.all_ranks.index(opponent_rank) - self.all_ranks.index(self.rank)
        if rank_diff < 1:
            return True
        else:
            return False

    def check_opponent_lvl_can_fight(self, opponent_lvl):
        diff = opponent_lvl - self.level
        if diff < 5:
            return True
        else:
            return False

    def battle(self, opponent_level):
        diff = opponent_level - self.level
        if 1 > opponent_level or opponent_level > 100:
            return "Invalid level"
        if opponent_level == self.level:
            self.add_experience(10)
            return "A good fight"
        if not self.check_opponent_lvl_can_fight(opponent_level) and\
                not self.check_opponent_rank_can_fight(opponent_level):
            return "You've been defeated"
        else:
            if diff == -1:
                self.add_experience(5)
                return "A good fight"
            if diff <= -2:
                return "Easy fight"
            if diff >= 1:
                gained_exp = 20 * diff * diff
                self.add_experience(gained_exp)
                return "An intense fight"