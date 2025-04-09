"""
Ransor - Jungle Monster (Oblivion)
Provides: Void Essence to Slayers, Stamina to Juggernauts, Berzerker to Bruisers
"""

class Ransor:
    def __init__(self):
        self.name = "Ransor"
        self.health = 10000
        self.armor = 300
        self.damage = 800
        self.buff_given = {
            "Slayer": "Void Essence",
            "Juggernaut": "Stamina",
            "Bruiser": "Berzerker"
        }

    def attack(self):
        return "Ransor strikes with demonic fury!"

    def grant_buff(self, champion_class):
        return self.buff_given.get(champion_class, "No buff")

if __name__ == "__main__":
    r = Ransor()
    print(f"{r.name} attacks: {r.attack()}")
    print("Buff for Slayer:", r.grant_buff("Slayer"))
