class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name

        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1_score == self.player2_score:
            return self.tie_points()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.other_player_is_head()
        else:
            return self.final_points()

        return score

    def tie_points(self):
        score = ""
        if self.player1_score == 0:
                score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        elif self.player1_score == 3:
            score = "Forty-All"
        else:
            score = "Deuce"
        return score

    def other_player_is_head(self):
        score = ""
        head = self.player1_score - self.player2_score
        if head == 1:
            score = "Advantage player1"
        elif head == -1:
            score = "Advantage player2"
        elif head >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def final_points(self):
        temp_score = 0
        score = ""

        for point in range(1, 3):
            if point == 1:
                temp_score = self.player1_score
            else:
                score = score + "-"
                temp_score = self.player2_score

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"

        return score