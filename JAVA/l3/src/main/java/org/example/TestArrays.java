package org.example;

import java.util.ArrayList;
import java.util.LinkedList;

/**
 * Class for testing ArrayList and LinkedList in time
 */
public class TestArrays {
    long timeStart;
    ArrayList<Object> arrList;
    LinkedList<Object> linkedList;
    TestArrays(){
        arrList= new ArrayList<>();
        linkedList = new LinkedList<>();
    }
    public void startTimer(){
        timeStart = System.currentTimeMillis();
    }
    public long stopTimerAndGetTime(){
        return System.currentTimeMillis() - timeStart;
    }
    public void arraysClear(){
        arrList.clear();
        linkedList.clear();
    }
    /**
     * @param N count of elemens
     */
    public void fillArrays(int N){
        for(int i = 0; i < N; ++i){
            arrList.add(new Object());
        }
        for(int i = 0; i < N; ++i){
            linkedList.add(new Object());
        }
    }
    /**
     * @param N count of elemens
     */
    public void addTest(int N){
        startTimer();
        for(int i = 0; i < N; ++i){
            arrList.add(new Object());
        }
        long arrAddTime = stopTimerAndGetTime();
        startTimer();
        for(int i = 0; i < N; ++i){
            linkedList.add(new Object());
        }
        long linkedAddTime = stopTimerAndGetTime();
        System.out.printf("\nAdd testing for ArrayList and LinkedList for %d elements, ArrayList Time: %d, LinkedList Time: %d, Time difference: %d",
                N, arrAddTime, linkedAddTime, Math.abs(arrAddTime - linkedAddTime));
        arraysClear();
    }
    /**
     * @param N count of elemens
     */
    public void getTest(int N) {
        fillArrays(N);
        startTimer();
        for(int i = 0; i < N; ++i){
            arrList.get(i);
        }
        long arrTime = stopTimerAndGetTime();
        startTimer();
        for(int i = 0; i < N; ++i){
            linkedList.get(i);
        }
        long linkedTime = stopTimerAndGetTime();
        System.out.printf("\nGet testing for ArrayList and LinkedList for %d elements, ArrayList Time: %d, LinkedList Time: %d, Time difference: %d",
                N, arrTime, linkedTime, Math.abs(arrTime - linkedTime));
        arraysClear();
    }

    /**
     * @param N count of elemens
     */
    public void deleteTest(int N) {
        fillArrays(N);
        startTimer();
        for(int i = 0; i < N; ++i){
            arrList.removeLast();
        }
        long arrTime = stopTimerAndGetTime();
        startTimer();
        for(int i = 0; i < N; ++i){
            linkedList.removeLast();
        }
        long linkedTime = stopTimerAndGetTime();
        System.out.printf("\nDelete testing for ArrayList and LinkedList for %d elements, ArrayList Time: %d, LinkedList Time: %d, Time difference: %d",
                N, arrTime, linkedTime, Math.abs(arrTime - linkedTime));
        arraysClear();
    }
}
