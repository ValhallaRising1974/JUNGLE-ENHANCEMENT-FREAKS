
class Nymph:
    def __init__(self):
        self.attack_speed = 1.5
        self.base_damage = 50

    def grant_buff(self):
        return {
            'attack_speed': self.attack_speed,
            'base_damage': self.base_damage
        }
