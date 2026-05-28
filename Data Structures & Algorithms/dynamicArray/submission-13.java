class DynamicArray {
    private int capacity;
    private int length;
    private int[] arr;

    public DynamicArray(int capacity) {
        this.capacity = capacity; 
        arr = new int[capacity];
        this.length = 0;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (length == capacity) resize();

        arr[length] = n;
        length++;
    }

    public int popback() {
        if (length > 0) length--;
        return arr[length];
    }

    private void resize() {
        int[] temp = arr;
        capacity *= 2;
        arr = new int[capacity];
        System.arraycopy(temp, 0, arr, 0, temp.length);
    }

    public int getSize() {
        return length;
    }

    public int getCapacity() {
        return capacity;
    }
}
