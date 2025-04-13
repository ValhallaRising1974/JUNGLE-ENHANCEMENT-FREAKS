
# jungle_buff_system.py

class JungleBuff:
    def __init__(self, name, duration, effects, exclusive_class=None):
        self.name = name
        self.duration = duration
        self.effects = effects
        self.exclusive_class = exclusive_class

    def apply_buff(self, champion_class):
        if self.exclusive_class and self.exclusive_class != champion_class:
            return {k: v * 0.5 for k, v in self.effects.items()}  # 50% if not original class
        return self.effects


# Example Buff Definitions

ransor_buff = JungleBuff(
    name="Ransor's Blessing",
    duration=90,
    effects={
        "Void Essence": 1,
        "Stamina Regen": 0.15,
        "Berzerker Boost": 0.25
    },
    exclusive_class="Jungler"
)

gnome_buff = JungleBuff(
    name="Stone-Bark Defense",
    duration=70,
    effects={
        "Armor": 0.10,
        "Max HP": 0.08,
        "Magic Resist": 0.10
    }
)

goblin_buff = JungleBuff(
    name="Shadowfury Speed",
    duration=60,
    effects={
        "Move Speed": 0.15,
        "Dodge Chance": 0.05
    }
)

nymph_buff = JungleBuff(
    name="Storm Grace",
    duration=60,
    effects={
        "Attack Speed": 0.20,
        "Critical Chance": 0.05
    }
)
