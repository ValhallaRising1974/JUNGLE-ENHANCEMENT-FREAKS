
class Goblin:
    def __init__(self):
        self.armor = 25
        self.hp = 120
        self.magic_resistance = 20

    def grant_buff(self):
        return {
            'armor': self.armor,
            'hp': self.hp,
            'magic_resistance': self.magic_resistance
        }
