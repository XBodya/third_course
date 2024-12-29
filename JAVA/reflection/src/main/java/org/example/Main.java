package org.example;

import java.io.FileNotFoundException;

public class Main {
    public static void main(String[] args) {
        Test A;
        try {
            A = (Test)Injector.inject(new Test());
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        System.out.println("FROM REFLECTION: " + A.doB);
    }
}