package l2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws OperationIsNotSupportException {
        String exp = "2 * 2 / 2 ^ (2 - 1)";
        exp = "(((14 + 10) * 2) / 42) ^ (13 + 2)";
        ExpressionCalc calc = new ExpressionCalc(exp);
        System.out.println('\n');
        double res = calc.calculate();
        System.out.println(calc.postfixExpression);
        System.out.println(res);
        // System.out.println(calc.GetStringNumber(1));
    }
}