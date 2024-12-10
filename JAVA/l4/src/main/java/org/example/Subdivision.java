package org.example;

public class Subdivision {
    int id;
    String name;
    static SubdivisionCounter counter = new SubdivisionCounter(0);

    Subdivision(int id, String name){
        this.id = id;
        this.name = name;
    }

    Subdivision(String name){
        this.id = counter.getId(name);
        this.name = name;
    }

    public int getId() {
        return id;
    }

    @Override
    public String toString() {
        return "Subdivision{" +
                "id=" + id +
                ", name='" + name + '\'' +
                '}';
    }

    public String getName() {
        return name;
    }
}

