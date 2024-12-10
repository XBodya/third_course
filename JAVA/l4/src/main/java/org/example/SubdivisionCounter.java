package org.example;

import java.util.HashMap;

/**
 * Класс для генерации id для подразделений
 */
public class SubdivisionCounter{
    private final int minValue;
    private final int maxValue;
    private int currentId;
    private HashMap<String, Integer> divisionData;

    public SubdivisionCounter(int startId) {
        this.currentId = startId;
        this.minValue = Integer.MIN_VALUE;
        this.maxValue = Integer.MAX_VALUE;
        divisionData = new HashMap<>();
    }

    public SubdivisionCounter(int startId, int minValue, int maxValue) {
        this.currentId = startId;
        this.minValue = minValue;
        this.maxValue = maxValue;
        divisionData = new HashMap<>();
    }

    /**
     * @param name Имя подразделения
     * @return id подразделения по его имени, диапазон значений от minValue до maxValue
     *
     */
    public int getId(String name){
        if(!divisionData.containsKey(name)) {
            divisionData.put(name, this.currentId);
            this.currentId = Math.max(Math.min(++this.currentId, this.maxValue), this.minValue);
        }
        return divisionData.get(name);
    }

}
