
# goblin.py

class ShadowfuryGoblin:
    def __init__(self):
        self.name = "Shadowfury Goblin"
        self.origin = "Helheim"
        self.buffs = {
            "All": {
                "Move Speed": 0.15,
                "Dodge Chance": 0.05
            }
        }
        self.duration = 60
        self.respawn_time = 75

    def on_death(self):
        return "Blind enemies for 0.5s"
