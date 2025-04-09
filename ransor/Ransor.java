// Ransor.java
// Jungle Monster - Oblivion

public class Ransor {
    private String name = "Ransor";
    private int health = 10000;
    private int armor = 300;
    private int damage = 800;

    public String attack() {
        return "Ransor strikes with demonic fury!";
    }

    public String grantBuff(String championClass) {
        switch (championClass) {
            case "Slayer": return "Void Essence";
            case "Juggernaut": return "Stamina";
            case "Bruiser": return "Berzerker";
            default: return "No buff";
        }
    }

    public static void main(String[] args) {
        Ransor r = new Ransor();
        System.out.println(r.name + " attacks: " + r.attack());
        System.out.println("Buff for Slayer: " + r.grantBuff("Slayer"));
    }
}
