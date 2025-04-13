
# nymph.py

class StormNymph:
    def __init__(self):
        self.name = "Storm Nymph"
        self.origin = "Svartalfheim"
        self.buffs = {
            "All": {
                "Attack Speed": 0.20,
                "Crit Chance (First 3 Hits)": 0.05
            }
        }
        self.duration = 60
        self.respawn_time = 90

    def special_condition(self, champion_hp_percent):
        if champion_hp_percent < 0.5:
            return "+2% Cooldown Reduction"
        return None
