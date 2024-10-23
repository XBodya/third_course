package com.l1;

public class Main {
    public static void main(String[] args) {

        Container MyCont = new Container(5);
        MyCont.set(0, "str");
        MyCont.set(1, 1);
        System.out.println("\n" + MyCont);
        MyCont.resize(0);
        System.out.println("\n" + MyCont);
        MyCont.resize(1);
        MyCont.addToEnd('s');
        System.out.println("\n" + MyCont);
        MyCont.delete(0);
        System.out.println("\n" + MyCont);
        MyCont.delete(0);
        System.out.println("\n" + MyCont);
    }
}