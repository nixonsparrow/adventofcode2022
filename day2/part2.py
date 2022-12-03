from utils import read_input
from part1 import Duel, Hand, Player


class RealPlayer(Player):
    def prepare(self, tactic, opponent_weapon=None):
        if tactic == "X":
            weapon = self.weapon.get_letter(Hand.WINNERS.get(Hand.WEAPON_CHOICES.get(opponent_weapon)))
        elif tactic == "Y":
            weapon = opponent_weapon
        else:
            weapon = [winner for winner, loser in Hand.WINNERS.items() if loser == Hand.WEAPON_CHOICES.get(opponent_weapon)][0]
            weapon = [letter for letter, name in Hand.WEAPON_CHOICES.items() if name == weapon][0]
        super().prepare(weapon)


class RealDuel(Duel):
    def fight(self):
        for row in self.battle_input:
            opponent_weapon, player_weapon = row.split(' ')
            self.player.prepare(player_weapon, opponent_weapon)
            self.opponent.prepare(opponent_weapon)
            self.player.play(self.opponent)
        self.result.update({self.player: self.player.points, self.opponent: self.opponent.points})
        return self.result


if __name__ == '__main__':
    duel = RealDuel(read_input("input.txt"), RealPlayer("Nixon"), Player("Elf"))
    print(duel.fight())
