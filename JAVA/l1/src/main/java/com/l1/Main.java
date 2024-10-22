package com.l1;

public class Main {
    public static void main(String[] args) {

        Container MyCont = new Container(5);
        MyCont.set(0, "str");
        MyCont.set(1, 1);
        System.out.println("\n" + MyCont);
    }
}