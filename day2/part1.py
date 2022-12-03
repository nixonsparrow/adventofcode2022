from utils import read_input


class Hand:
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"
    WEAPON_CHOICES = {
        "A": ROCK, "X": ROCK,
        "B": PAPER, "Y": PAPER,
        "C": SCISSORS, "Z": SCISSORS,
        None: None
    }
    BASIC_POINTS = {
        ROCK: 1,
        PAPER: 2,
        SCISSORS: 3,
    }
    WINNERS = {
        SCISSORS: PAPER,
        PAPER: ROCK,
        ROCK: SCISSORS,
    }

    def __init__(self, shape):
        self.shape = self.WEAPON_CHOICES[shape]

    def __str__(self):
        return self.shape

    def switch(self, new_shape):
        self.shape = self.WEAPON_CHOICES[new_shape]
        return self

    def get_letter(self, shape):
        return [letter for letter, sh in self.WEAPON_CHOICES.items() if sh == shape][0]


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.weapon = None

    def prepare(self, weapon):
        self.weapon = self.weapon.switch(weapon) if self.weapon else Hand(weapon)
        pass

    def get_points_for_weapon(self):
        self.points += Hand.BASIC_POINTS.get(self.weapon.shape)

    def play(self, enemy):
        self.get_points_for_weapon()
        enemy.get_points_for_weapon()
        if self.weapon.shape == enemy.weapon.shape:
            self.points += 3
            enemy.points += 3
        elif Hand.WINNERS.get(self.weapon.shape) == enemy.weapon.shape:
            self.points += 6
        else:
            enemy.points += 6

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Duel:
    def __init__(self, battle_input, player, opponent):
        self.battle_input = battle_input
        self.player = player
        self.opponent = opponent
        self.result = {}

    def fight(self):
        for row in self.battle_input:
            opponent_weapon, player_weapon = row.split(' ')
            self.player.prepare(player_weapon)
            self.opponent.prepare(opponent_weapon)
            self.player.play(self.opponent)
        self.result.update({self.player: self.player.points, self.opponent: self.opponent.points})


if __name__ == '__main__':
    duel = Duel(read_input("input.txt"), Player("Nixon"), Player("Elf"))
    duel.fight()
    print(duel.result)
