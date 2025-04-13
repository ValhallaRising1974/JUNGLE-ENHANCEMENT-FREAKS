
// Ransor.java

public class Ransor {
    private final String name = "Ransor";
    private final String origin = "Muspelheim";
    private final int duration = 90;
    private final int respawnTime = 180;

    public String getBuff(String championClass) {
        switch (championClass) {
            case "Slayer":
                return "+1 Void Essence";
            case "Juggernaut":
                return "+15% Stamina Regen";
            case "Bruiser":
                return "+25% Berzerker Boost";
            default:
                return "Partial Buff (50%)";
        }
    }

    public String onDeath() {
        return "AoE Fear + Silence (1s)";
    }
}
