package com.l1;

public class Container {
    int size;
    Object[] data;

    Container() {
        size = 0;
        data = new Object[0];
    }

    Container(int length) {
        size = length;
        data = new Object[size];
    }

    Container(Container otherContainer) {
        size = otherContainer.size;
        data = new Object[size];
        for (int i = 0; i < size; ++i) {
            data[i] = otherContainer.get(i);
        }
    }

    public Object get(int index) {
        return data[index];
    }

    public void set(int index, Object obj) {
        data[index] = obj;
    }

    public void addToEnd(Object obj) {

    }

    public void addToFront(Object obj) {

    }

    public void resize(int newSize) {
        Object[] newData = new Object[newSize];
        for (int i = 0; i < (newSize < size ? newSize : size); ++i) {

        }
    }

    public void delete(int index) {

    }
}
