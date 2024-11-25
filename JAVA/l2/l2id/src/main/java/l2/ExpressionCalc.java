package l2;

import java.util.Stack;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class ExpressionCalc {
    private String curExpression;

    String postfixExpression;

    private boolean havePostfixForm;

    protected static HashMap<String, Double> tableOfTermValues;

    ExpressionCalc(String Expression) {
        curExpression = Expression;
        postfixExpression = "";
        tableOfTermValues = new HashMap<>();
        havePostfixForm = false;
    }

    public void setExpression(String newEString) {
        curExpression = newEString;
        havePostfixForm = false;
    }

    private static int getPriority(Character value) {
        switch (value) {
            case '(':
                return 0;
            case '+':
                return 1;
            case '-':
                return 1;
            case '*':
                return 2;
            case '/':
                return 2;
            case '^':
                return 3;
            case '~':
                return 4;
        }
        return 3;
    }

    public static String getStringNumber(int index, String str) {
        String curNum = "";
        for (int i = index; i < str.length(); ++i) {
            Character curChar = str.charAt(i);
            if (Character.isDigit(curChar))
                curNum += curChar;
            else if(curChar == '.' && i + 1 < str.length() && Character.isDigit(str.charAt(i + 1))){
                    curNum += str.charAt(i);
            }
            else
                break;
        }
        return curNum;
    }

    public static String getStringTerm(int index, String str){
        String curTerm = "";
        for(int i = index; i < str.length(); ++i){
            Character curChar = str.charAt(i);
            if(Character.isLetter(curChar))
                curTerm += curChar;
            else
                break;
        }
        return curTerm;
    }

    private static boolean isOperationChars(char curChar) {
        return curChar == '(' || curChar == '+' || curChar == '-' || curChar == '*' || curChar == '/' || curChar == '^';
    }

    private static String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }

    private String getPostfix() {
        String postfixString = "";
        Stack<Character> stack = new Stack<>();
        ArrayList<String> listOfTerms = new ArrayList<>();
        tableOfTermValues.clear();
        for (int i = 0; i < curExpression.length(); ++i) {
            Character curChar = curExpression.charAt(i);
            if (Character.isDigit(curChar)) {
                String curNum = getStringNumber(i, curExpression);
                postfixString += curNum + " ";
                i = Math.min(curExpression.length() - 1, i + curNum.length());
                curChar = curExpression.charAt(i);
            }
            if(Character.isLetter(curChar)){
                String curTerm = getStringTerm(i, curExpression);
                listOfTerms.add(curTerm);
                postfixString += curTerm + " ";
                i = Math.min(curExpression.length() - 1, i + curTerm.length());
                curChar = curExpression.charAt(i);
            }
            if (curChar == '(') {
                stack.push(curChar);
            } else if (curChar == ')') {
                while (stack.size() > 0 && stack.peek() != '(')
                    postfixString += stack.pop();
                stack.pop();
            } else if (isOperationChars(curChar)) {
                Character tmp = curChar;
                if (tmp == '-' && (i == 0 || (i >= 1 && isOperationChars(curExpression.charAt(i - 1))))) {
                    tmp = '~';
                }
                // System.out.println(getPriority(stack.peek()) >= getPriority(tmp));
                while (stack.size() > 0 && (getPriority(stack.peek()) >= getPriority(tmp))) {
                    postfixString += stack.pop();
                    // System.out.println(1);
                }

                stack.push(tmp);
            }
        }
        String lastOperations = "";
        for (Character iterable_element : stack) {
            lastOperations += iterable_element;
        }
        lastOperations = reverseString(lastOperations);
        postfixString += lastOperations;

        Scanner inputScanner = new Scanner(System.in);
        String userNotify = "Enter values for variables (by current order): ";
        for (int i = 0; i < listOfTerms.size() - 1; ++i) {
            userNotify += (listOfTerms.get(i) + " ");
        }
        if(!listOfTerms.isEmpty())
            userNotify += listOfTerms.get(listOfTerms.size() - 1);
        System.out.println(userNotify);
        for(int cntOfUsed = 0; cntOfUsed < listOfTerms.size(); ++cntOfUsed){
            tableOfTermValues.put(listOfTerms.get(cntOfUsed), inputScanner.nextDouble());
            //System.out.println(tableOfTermValues.get(listOfTerms.get(cntOfUsed)));
        }
        for (String term : listOfTerms) {
            postfixString = postfixString.replaceAll(term, tableOfTermValues.get(term).toString());
        }
        inputScanner.close();
        return postfixString;
    }

    public void toPostfix() {
        postfixExpression = getPostfix();
        havePostfixForm = true;
    }

    private static double action(char operations, double a, double b) throws OperationIsNotSupportException {
        switch (operations) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                return a / b;
            case '^':
                return Math.pow(a, b);
        }
        throw new OperationIsNotSupportException("This operation is not supported");
    }

    public double calculate() throws OperationIsNotSupportException {
        // System.out.println(toPostfix());
        if (!havePostfixForm)
            toPostfix();
        Stack<Double> resultOfOperations = new Stack<>();
        for (int i = 0; i < postfixExpression.length(); ++i) {
            Character curChar = postfixExpression.charAt(i);
            if (Character.isDigit(curChar)) {
                String curNum = getStringNumber(i, postfixExpression);
                resultOfOperations.push(Double.parseDouble(curNum));
                i = Math.min(postfixExpression.length() - 1, i + curNum.length());
                curChar = postfixExpression.charAt(i);
            }
            if (isOperationChars(curChar)) {
                if (curChar == '~') {
                    double last = (!resultOfOperations.isEmpty()) ? resultOfOperations.pop() : 0;
                    resultOfOperations.push(action('-', 0.0, last));
                    continue;
                }
                double second = (!resultOfOperations.isEmpty()) ? resultOfOperations.pop() : 0,
                        first = (!resultOfOperations.isEmpty()) ? resultOfOperations.pop() : 0;

                resultOfOperations.push(action(curChar, first, second));
            }
        }
        return resultOfOperations.pop();
    }
};
