
public class Nymph {
    private double attackSpeed = 1.5;
    private int baseDamage = 50;

    public Map<String, Object> grantBuff() {
        Map<String, Object> buffs = new HashMap<>();
        buffs.put("attack_speed", attackSpeed);
        buffs.put("base_damage", baseDamage);
        return buffs;
    }
}
