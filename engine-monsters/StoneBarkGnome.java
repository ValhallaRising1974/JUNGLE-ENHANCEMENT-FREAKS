
// StoneBarkGnome.java

public class StoneBarkGnome {
    private final String name = "Stone-Bark Gnome";
    private final String origin = "Svartalfheim";
    private final int duration = 70;
    private final int respawnTime = 60;

    public String getBuff() {
        return "+10% Armor, +8% Max HP, +10% Magic Resist";
    }

    public String groupDeathBonus(double killTimeSeconds) {
        return (killTimeSeconds <= 5) ? "Double HP Regen for 10s" : "Standard Buff Only";
    }
}
