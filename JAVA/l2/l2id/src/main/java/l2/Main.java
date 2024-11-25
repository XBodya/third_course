package l2;

public class Main {
    public static void main(String[] args) throws OperationIsNotSupportException {
        String exp = "2 * 2 / 2 ^ (2 - 1)";
        
        exp = "4 ^ 0.5";
        exp = "(((sdw + gr) * 2) / abs) ^ (13 + 2)";
        exp = "a + b";
        //System.out.println(ExpressionCalc.getTerm(0, "exp 12"));
        ExpressionCalc calc = new ExpressionCalc(exp);
        System.out.println('\n');
        double res = calc.calculate();
        System.out.println(calc.postfixExpression);
        System.out.println(res);
    }
}