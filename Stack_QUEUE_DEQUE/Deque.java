package Stack_QUEUE_DEQUE;


import java.util.ArrayList;
import java.util.List;

public class Deque<T> {
    private List<T> elements;

    public Deque() {
        elements = new ArrayList<>();
    }

    public void addFirst(T item) {
        elements.add(0, item);
    }

    public void addLast(T item) {
        elements.add(item);
    }

    public T removeFirst() {
        if (isEmpty()) {
            throw new IllegalStateException("Deque is empty");
        }
        return elements.remove(0);
    }

    public T removeLast() {
        if (isEmpty()) {
            throw new IllegalStateException("Deque is empty");
        }
        return elements.remove(elements.size() - 1);
    }

    public T peekFirst() {
        if (isEmpty()) {
            throw new IllegalStateException("Deque is empty");
        }
        return elements.get(0);
    }

    public T peekLast() {
        if (isEmpty()) {
            throw new IllegalStateException("Deque is empty");
        }
        return elements.get(elements.size() - 1);
    }

    public boolean isEmpty() {
        return elements.isEmpty();
    }

    public int size() {
        return elements.size();
    }
}

