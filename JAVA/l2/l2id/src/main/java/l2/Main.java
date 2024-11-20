package l2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String exp = "(((-14 + 10) * 2) / 42) ^ (13 + 2) + (1 + 2)";
        ExpressionCalc calc = new ExpressionCalc(exp);
        System.out.println('\n');
        calc.calculate();
        // System.out.println(calc.GetStringNumber(1));
    }
}