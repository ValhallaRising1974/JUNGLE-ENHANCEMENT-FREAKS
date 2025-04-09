
public class Goblin {
    private int armor = 25;
    private int hp = 120;
    private int magicResistance = 20;

    public Map<String, Integer> grantBuff() {
        Map<String, Integer> buffs = new HashMap<>();
        buffs.put("armor", armor);
        buffs.put("hp", hp);
        buffs.put("magic_resistance", magicResistance);
        return buffs;
    }
}
