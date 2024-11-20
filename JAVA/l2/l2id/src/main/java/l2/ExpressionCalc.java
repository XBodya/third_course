package l2;

import java.util.Stack;

public class ExpressionCalc {
    String curExpression;

    ExpressionCalc(String Expression) {
        curExpression = Expression;
    }

    public double calculate() {
        System.out.println(toPostfix());
        return 0;
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
        return 4;
    }

    public String GetStringNumber(int index) {
        String curNum = "";
        for (int i = index; i < curExpression.length(); ++i) {
            Character curChar = curExpression.charAt(i);
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

    private String toPostfix() {
        String postfixString = "";
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < curExpression.length(); ++i) {
            Character curChar = curExpression.charAt(i);
            if (Character.isDigit(curChar)) {
                String curNum = GetStringNumber(i);
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
        for (Character iterable_element : stack) {
            postfixString += iterable_element;
        }
        return postfixString;
    }
};
