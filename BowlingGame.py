class BowlingGame:
    def __init__(self):
        self.rolls=[]

    def roll(self,pins):
        self.rolls.append(pins)

    def total_score(self):
        score = 0
        roll_index = 0
        for frame in range(10):
            if self._is_strike(roll_index):
                score += 10 + self.rolls[roll_index+1] + self.rolls[roll_index+2]
                roll_index += 1
            elif self._is_spare(roll_index):
                score += 10 + self.rolls[roll_index+2]
                roll_index += 2