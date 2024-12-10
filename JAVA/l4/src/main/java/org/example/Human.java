package org.example;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.format.DateTimeFormatter;
import java.util.Date;


public class Human {
    int id;
    String name;
    String gender;
    Subdivision subdivide;
    int salary;
    Date birthday;

    Human(int id, String name, String gender, Subdivision subdivide, int salary, String birthday) {
        this.id = id;
        this.name = name;
        this.gender = gender;
        this.subdivide = subdivide;
        this.salary = salary;
        try {
            this.birthday = new SimpleDateFormat("dd.MM.yyyy").parse(birthday);
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }
    }

    Human(String[] args){
        this.id = Integer.parseInt(args[0]);
        this.name = args[1];
        this.gender = args[2];
        try {
            this.birthday = new SimpleDateFormat("dd.MM.yyyy").parse(args[3]);
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }
        this.subdivide = new Subdivision(args[4]);
        this.salary = Integer.parseInt(args[5]);

    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public void setBirthday(String strBirthday) throws ParseException {
        this.birthday = new SimpleDateFormat("dd.MM.yyyy").parse(strBirthday);
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public Subdivision getSubdivide() {
        return subdivide;
    }

    public void setSubdivide(Subdivision subdivide) {
        this.subdivide = subdivide;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    @Override
    public String toString() {
        return "Human{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", gender='" + gender + '\'' +
                ", subdivide=" + subdivide +
                ", salary=" + salary +
                ", birthday=" + birthday +
                '}';
    }
}
