
// JungleBuff.java

import java.util.HashMap;
import java.util.Map;

public class JungleBuff {
    private String name;
    private int duration;
    private Map<String, Double> effects;
    private String exclusiveClass;

    public JungleBuff(String name, int duration, Map<String, Double> effects, String exclusiveClass) {
        this.name = name;
        this.duration = duration;
        this.effects = effects;
        this.exclusiveClass = exclusiveClass;
    }

    public Map<String, Double> applyBuff(String championClass) {
        Map<String, Double> result = new HashMap<>();
        for (Map.Entry<String, Double> entry : effects.entrySet()) {
            if (exclusiveClass != null && !exclusiveClass.equals(championClass)) {
                result.put(entry.getKey(), entry.getValue() * 0.5);
            } else {
                result.put(entry.getKey(), entry.getValue());
            }
        }
        return result;
    }

    public String getName() {
        return name;
    }

    public int getDuration() {
        return duration;
    }
}
