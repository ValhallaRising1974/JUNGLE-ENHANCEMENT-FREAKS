
# gnome.py

class StoneBarkGnome:
    def __init__(self):
        self.name = "Stone-Bark Gnome"
        self.origin = "Svartalfheim"
        self.buffs = {
            "All": {
                "Armor": 0.10,
                "Max HP": 0.08,
                "Magic Resist": 0.10
            }
        }
        self.duration = 70
        self.respawn_time = 60

    def group_death_bonus(self, kill_time):
        if kill_time <= 5:
            return "Double HP Regen for 10s"
        return None
