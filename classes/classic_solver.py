from itertools import combinations as c

import discord


class ClassicSolver:
    def __init__(self, rounds, matches, verified, ctx):
        self.rounds = rounds
        self.matches = matches
        self.verified = verified
        self.valid = []
        self.valid_cnt = 0
        self.combos = list(c(range(1, 16), 3))

        self.sol_panel = discord.Embed()
        self.sol_panel.set_footer(text=ctx.author)

    def solve(self):
        print(self.rounds)
        print(self.matches)
        print(self.verified)
        for cb in self.combos:
            flag = True

            for rnd, mt, vr in zip(self.rounds, self.matches, self.verified):
                if not vr:
                    continue

                tmp_rnd = list(rnd)
                cnt = 0

                for val in cb:
                    if val in tmp_rnd:
                        cnt += 1
                        tmp_rnd.remove(val)

                if cnt != mt:
                    flag = False
                    break

            if flag:
                self.valid.append(f"`{cb[0]} {cb[1]} {cb[2]}`")
                self.valid_cnt += 1

        self.gen_embed()

    def gen_embed(self):
        self.sol_panel.title = f"{self.valid_cnt} Valid Solution{'s'*(self.valid_cnt != 1)}"

        if self.valid_cnt > 64:
            self.sol_panel.description = f"Solutions will not be listed since there are over 64 possible valid combos"
        else:
            self.sol_panel.description = f"||{', '.join(self.valid)}||"
