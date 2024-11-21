package l2;

import java.util.Stack;

public class ExpressionCalc {
    private String curExpression;

    String postfixExpression;

    private boolean havePostfixForm;

    ExpressionCalc(String Expression) {
        curExpression = Expression;
        postfixExpression = "";
        havePostfixForm = false;
    }

    public void setExpression(String newEString) {
        curExpression = newEString;
        havePostfixForm = false;
    }

    private int getPriority(Character value) {
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

    public String GetStringNumber(int index, String str) {
        String curNum = "";
        for (int i = index; i < str.length(); ++i) {
            Character curChar = str.charAt(i);
            if (Character.isDigit(curChar))
                curNum += curChar;
            else
                break;
        }
        return curNum;
    }

    private boolean isOperationChars(char curChar) {
        return curChar == '(' || curChar == '+' || curChar == '-' || curChar == '*' || curChar == '/' || curChar == '^';
    }

    private String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }

    private String getPostfix() {
        String postfixString = "";
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < curExpression.length(); ++i) {
            Character curChar = curExpression.charAt(i);
            if (Character.isDigit(curChar)) {
                String curNum = GetStringNumber(i, curExpression);
                postfixString += curNum + " ";
                i = Math.min(curExpression.length() - 1, i + curNum.length());
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
        return postfixString;
    }

    public void toPostfix() {
        postfixExpression = getPostfix();
        havePostfixForm = true;
    }

    private double action(char operations, double a, double b) throws OperationIsNotSupportException {
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
                String curNum = GetStringNumber(i, postfixExpression);
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
