package com.l1;

import java.lang.annotation.Inherited;

public class Container implements Cloneable {
    private int length;
    private Object[] data;

    Container() {
        this.length = 0;
        this.data = new Object[0];
    }

    Container(int length) {
        this.length = length;
        this.data = new Object[length];
    }

    Container(Object[] otherArray) {
        this(otherArray.length);
        for (int i = 0; i < this.length; ++i) {
            this.data[i] = otherArray[i];
        }
    }

    Container(Container otherContainer) {
        this(otherContainer.data);
    }

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

    public Object pop(int index) {
        Object popElement = this.get(index);
        this.delete(index);
        return popElement;
    }
}
