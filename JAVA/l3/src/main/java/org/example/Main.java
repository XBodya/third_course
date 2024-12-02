package org.example;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        System.out.print("ArrayList and LinkedList testing. (Time is measured by millisec. )");
        TestArrays testCases = new TestArrays();
        for(int i = 1; i <= 10; ++i){
            testCases.addTest(i * 100000);
        }
        for(int i = 1; i <= 10; ++i){
            testCases.getTest(i * 10000);
        }for(int i = 1; i <= 10; ++i){
            testCases.deleteTest(i * 100000);
        }
    //        ArrayList and LinkedList testing. (Time is measured by millisec. )
    //        Add testing for ArrayList and LinkedList for 100000 elements, ArrayList Time: 3, LinkedList Time: 3, Time difference: 0
    //        Add testing for ArrayList and LinkedList for 200000 elements, ArrayList Time: 2, LinkedList Time: 3, Time difference: 1
    //        Add testing for ArrayList and LinkedList for 300000 elements, ArrayList Time: 6, LinkedList Time: 2, Time difference: 4
    //        Add testing for ArrayList and LinkedList for 400000 elements, ArrayList Time: 3, LinkedList Time: 15, Time difference: 12
    //        Add testing for ArrayList and LinkedList for 500000 elements, ArrayList Time: 4, LinkedList Time: 7, Time difference: 3
    //        Add testing for ArrayList and LinkedList for 600000 elements, ArrayList Time: 9, LinkedList Time: 6, Time difference: 3
    //        Add testing for ArrayList and LinkedList for 700000 elements, ArrayList Time: 4, LinkedList Time: 11, Time difference: 7
    //        Add testing for ArrayList and LinkedList for 800000 elements, ArrayList Time: 11, LinkedList Time: 7, Time difference: 4
    //        Add testing for ArrayList and LinkedList for 900000 elements, ArrayList Time: 8, LinkedList Time: 89, Time difference: 81
    //        Add testing for ArrayList and LinkedList for 1000000 elements, ArrayList Time: 10, LinkedList Time: 197, Time difference: 187
    //        Get testing for ArrayList and LinkedList for 10000 elements, ArrayList Time: 0, LinkedList Time: 36, Time difference: 36
    //        Get testing for ArrayList and LinkedList for 20000 elements, ArrayList Time: 1, LinkedList Time: 142, Time difference: 141
    //        Get testing for ArrayList and LinkedList for 30000 elements, ArrayList Time: 0, LinkedList Time: 294, Time difference: 294
    //        Get testing for ArrayList and LinkedList for 40000 elements, ArrayList Time: 0, LinkedList Time: 930, Time difference: 930
    //        Get testing for ArrayList and LinkedList for 50000 elements, ArrayList Time: 0, LinkedList Time: 1336, Time difference: 1336
    //        Get testing for ArrayList and LinkedList for 60000 elements, ArrayList Time: 0, LinkedList Time: 2075, Time difference: 2075
    //        Get testing for ArrayList and LinkedList for 70000 elements, ArrayList Time: 0, LinkedList Time: 3018, Time difference: 3018
    //        Get testing for ArrayList and LinkedList for 80000 elements, ArrayList Time: 0, LinkedList Time: 3488, Time difference: 3488
    //        Get testing for ArrayList and LinkedList for 90000 elements, ArrayList Time: 0, LinkedList Time: 4947, Time difference: 4947
    //        Get testing for ArrayList and LinkedList for 100000 elements, ArrayList Time: 0, LinkedList Time: 6301, Time difference: 6301
    //        Delete testing for ArrayList and LinkedList for 100000 elements, ArrayList Time: 2, LinkedList Time: 2, Time difference: 0
    //        Delete testing for ArrayList and LinkedList for 200000 elements, ArrayList Time: 1, LinkedList Time: 2, Time difference: 1
    //        Delete testing for ArrayList and LinkedList for 300000 elements, ArrayList Time: 1, LinkedList Time: 2, Time difference: 1
    //        Delete testing for ArrayList and LinkedList for 400000 elements, ArrayList Time: 1, LinkedList Time: 3, Time difference: 2
    //        Delete testing for ArrayList and LinkedList for 500000 elements, ArrayList Time: 0, LinkedList Time: 4, Time difference: 4
    //        Delete testing for ArrayList and LinkedList for 600000 elements, ArrayList Time: 1, LinkedList Time: 5, Time difference: 4
    //        Delete testing for ArrayList and LinkedList for 700000 elements, ArrayList Time: 1, LinkedList Time: 5, Time difference: 4
    //        Delete testing for ArrayList and LinkedList for 800000 elements, ArrayList Time: 0, LinkedList Time: 6, Time difference: 6
    //        Delete testing for ArrayList and LinkedList for 900000 elements, ArrayList Time: 1, LinkedList Time: 6, Time difference: 5
    //        Delete testing for ArrayList and LinkedList for 1000000 elements, ArrayList Time: 0, LinkedList Time: 7, Time difference: 7

    }
}