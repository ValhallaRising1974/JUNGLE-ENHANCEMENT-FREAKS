
// StormNymph.java

public class StormNymph {
    private final String name = "Storm Nymph";
    private final String origin = "Svartalfheim";
    private final int duration = 60;
    private final int respawnTime = 90;

    public String getBuff() {
        return "+20% Attack Speed, +5% Crit Chance (First 3 Hits)";
    }

    public String conditionalBuff(double championHpPercent) {
        return (championHpPercent < 0.5) ? "+2% Cooldown Reduction" : "No Bonus";
    }
}
