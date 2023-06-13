package Stack_QUEUE_DEQUE;

public class  Stack {
    Object[] dizi;
    int size, peak;

    public Stack(int size) {
        dizi = new Object[size];
        this.size = size;
        peak = -1;
    }

    public void push(Object obj) {
        if (peak == size-1) {
            System.out.println("Stack dolu...");
            return;
        }
        peak++;
        dizi[peak] = obj;

    }

    public Object pop() {
        if (isEmpty()) {
            System.out.println("Stack bos...");
            return null;
        }
        Object temp = dizi[peak];
        dizi[peak] = null;
        peak--;
        return temp;
    }

    public Object peak() {
        if (isEmpty()) {
            System.out.println("Stack bos...");
            return null;
        }
        return dizi[peak];
    }

    public boolean isEmpty() {
        if (peak == -1)
            return true;
        return false;
    }

    public void show() {
        for (Object obj : dizi) {
            if (obj != null)
                System.out.println(obj);
        }
    }
}
