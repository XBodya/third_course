package l2;



public class Main {
    public static void main(String[] args) throws OperationIsNotSupportException {
        //String res = "1 + (2 * (26 + 1 - 22424) + 239832) / 291";
        testCase();
        //System.out.println(res);
    }

    public static void isEqual(Double a, Double b, String message){
        System.out.print("Test name " + message);
        if(Math.abs(a -  b) < 1e-7){
            System.out.println(" OK\n");
        }
        else{
            System.out.println(" Failed. values: a=" + a.toString() + " b=" + b.toString() + "\n");
        }
    }

    public static void testCase() throws OperationIsNotSupportException{
        Double a;
        String b;
        ExpressionCalc calc = new ExpressionCalc("");
        a = 5. + 3;
        b = "5 + 3";
        calc.setExpression(b);
        Double c = calc.calculate(); 
        isEqual(a, c, b);
        
        a = 10. - 4;
        b = "10 - 4";
        calc.setExpression(b);
        c = calc.calculate(); 
        isEqual(a, c, b);
        
        a = 2 + 3 * Math.pow((4 - 2), 2);
        b = "2 + 3 * (4 - 2) ^ 2";
        calc.setExpression(b);
        c = calc.calculate(); 
        isEqual(a, c, b);
        
        a = 7 * 6.;
        b = "7 * 6";
        calc.setExpression(b);
        c = calc.calculate(); 
        isEqual(a, c, b);
        
        a = 20. / 4;
        b = "20 / 4";
        calc.setExpression(b);
        c = calc.calculate(); 
        isEqual(a, c, b);
        
        a = 5. + 3;
        b = "5 + 3";
        calc.setExpression(b);
        c = calc.calculate(); 
        isEqual(a, c, b);
        
        a = Math.pow(2, 3);
        b = "2 ^ 3";
        calc.setExpression(b);
        c = calc.calculate(); 
        isEqual(a, c, b);
        
        a = 3 + 5 * 2.;
        b = "3 + 5 * 2";
        calc.setExpression(b);
        c = calc.calculate(); 
        isEqual(a, c, b);
        
        a = (3 + 5) * 2.;
        b = "(3 + 5) * 2";
        calc.setExpression(b);
        c = calc.calculate(); 
        isEqual(a, c, b);
        
        a = 15. / 2.;
        b = "15 / 2";
        calc.setExpression(b);
        c = calc.calculate(); 
        isEqual(a, c, b);


    }
}