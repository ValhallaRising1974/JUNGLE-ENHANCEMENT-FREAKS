
# ransor.py

class Ransor:
    def __init__(self):
        self.name = "Ransor"
        self.origin = "Muspelheim"
        self.buffs = {
            "Slayer": {"Void Essence": 1},
            "Juggernaut": {"Stamina Regen": 0.15},
            "Bruiser": {"Berzerker Boost": 0.25}
        }
        self.duration = 90
        self.respawn_time = 180

    def on_death(self):
        return "AoE Fear + Silence (1s)"
