from random import randint, choice

import discord

from classes.classic import Classic


class Detective(Classic):
    def __init__(self, discord_tag):
        super().__init__(discord_tag)
        self.game_id = 2
        self.board.title = "Repeat Gamemode"
        self.lie_index = randint(1, 4)  # Index of the lie
        self.actual = 0  # Real number of matches
        self.found_lie = False
        print(self.lie_index, self.answer)

    def match_ans(self, guess):
        tmp_guess = list(guess)
        match = 0

        for num in self.answer:
            if num in tmp_guess:
                tmp_guess.remove(num)
                match += 1

        if self.round_number == self.lie_index:
            self.actual = match
            return self.create_lie(match, len(guess))
        else:
            return match

    def win(self, guess):
        return (self.matches[-1] == len(guess) == 3) and self.round_number > 4

    def lose(self):
        return self.round_number == 9

    def update_stats(self, guess):
        self.round_number += 1
        self.rounds.append(guess)
        self.matches.append(self.match_ans(guess))

        if self.round_number <= 4:
            self.verified.append(False)
        else:
            self.verified.append(True)

    def last_guess(self, guess, flag):
        return self.round_number == 8 and len(guess) != 3 and flag

    def create_lie(self, actual, guess_len):
        """Returns a random number from 0 to `guess_len` that is not `actual`"""

        guess_len = 3 if guess_len == 4 else guess_len
        st = set(range(guess_len+1)) - {actual}
        return choice(list(st))
