
// ShadowfuryGoblin.java

public class ShadowfuryGoblin {
    private final String name = "Shadowfury Goblin";
    private final String origin = "Helheim";
    private final int duration = 60;
    private final int respawnTime = 75;

    public String getBuff() {
        return "+15% Movement Speed, +5% Dodge Chance";
    }

    public String onDeath() {
        return "Blind enemies for 0.5s";
    }
}
