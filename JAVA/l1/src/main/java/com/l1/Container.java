package com.l1;

import java.lang.annotation.Inherited;

/*
 * Class Container
 */
public class Container implements Cloneable {
    /*
     * @param length: count of elements in container
     * 
     * @param data: array of elements
     */
    private int length;
    private Object[] data;

    /*
     * Default constructor
     */
    Container() {
        this.length = 0;
        this.data = new Object[0];
    }

    /*
     * Constructor with length of container
     */
    Container(int length) {
        this.length = length;
        this.data = new Object[length];
    }

    /*
     * Constructor based on other array of objects
     */
    Container(Object[] otherArray) {
        this(otherArray.length);
        for (int i = 0; i < this.length; ++i) {
            this.data[i] = otherArray[i];
        }
    }

    /*
     * Constructor of coping
     */
    Container(Container otherContainer) {
        this(otherContainer.data);
    }

    /*
     * @return String by example Container{length=@length, data=[@elements_of_data]}
     */
    @Override
    public String toString() {
        String dataString = "";
        for (Object curObject : data) {
            dataString += (curObject.toString() + " ");
        }
        return "Container{length=" + length + ", data=[ " + dataString + "]}";
    }

    @Override
    public Object clone() {
        Container clonedContainer = new Container(this.data);
        return clonedContainer;
    }

    /*
     * @return true if objects is equal else false
     */
    public boolean equals(Object obj) {
        if (obj == null && this != null)
            return false;
        if (((Container) obj).length != this.length)
            return false;
        else if (((Container) obj).length == this.length) {
            for (int i = 0; i < this.length; ++i) {
                if (!this.data[i].equals(((Container) obj).data[i]))
                    return false;
            }
        }
        return true;

    }

    public Object get(int index) {
        if (index < 0 || index >= this.length)
            return null;
        return this.data[index];
    }

    public int getLength() {
        return this.length;
    }

    public void set(int index, Object obj) {
        if (index < 0 || index >= this.length)
            return;
        this.data[index] = obj;
    }

    public void addToEnd(Object obj) {
        this.resize(length + 1);
        this.set(length, obj);
    }

    /*
     * method for resize Container and changed length on newLength
     */
    public void resize(int newLength) {
        Object[] newData = new Object[newLength];
        for (int i = 0; i < newLength; ++i) {
            if (i < length) {
                newData[i] = data[i];
            }
        }
        this.data = newData;
        this.length = newLength;
    }

    public void delete(int index) {
        if (index < 0 || index >= length)
            return;
        if (length == 0)
            return;

        Object[] newData = new Object[length - 1];
        for (int i = 0; i < (length - 1); ++i) {
            if (i < index) {
                newData[i] = data[i];
            } else if (i > index) {
                newData[i - 1] = data[i];
            }
        }
        this.data = newData;
        this.length -= 1;
    }

    /*
     * delete element with index of @index and @return this element
     */
    public Object pop(int index) {
        Object popElement = this.get(index);
        this.delete(index);
        return popElement;
    }
}
