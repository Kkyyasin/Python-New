package LinkList;
public class DoubleLinkList<T> {
    private Node<T> head;
    private Node<T> tail;
    private int size;

    private class Node<T> {
        private T data;
        private Node<T> prev;
        private Node<T> next;

        public Node(T data) {
            this.data = data;
        }
    }

    public void add(T element) {
        Node<T> newNode = new Node<>(element);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }

    public void remove(T element) {
        Node<T> current = head;
        while (current != null) {
            if (current.data.equals(element)) {
                if (current == head) {
                    head = current.next;
                    if (head != null) {
                        head.prev = null;
                    }
                } else if (current == tail) {
                    tail = current.prev;
                    if (tail != null) {
                        tail.next = null;
                    }
                } else {
                    current.prev.next = current.next;
                    current.next.prev = current.prev;
                }
                size--;
                break;
            }
            current = current.next;
        }
    }

    public int size() {
        return size;
    }

    public void display() {
        Node<T> current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
    public void removenth(int x) {
        System.out.println(x);
        Node<T> current = head;


        // İndexi sondan x. elemanın bulunduğu düğüme getir
        while (current.next != null) {
            current = current.next;
                   }
        int i = 0;
        // İndex doğruysa düğümü sil
        while (i <x && current.prev != null) {
            i++;
            current=current.prev;
        }
      if (current.prev == null) {
            current.next.next = current.next;
        } else{
            current.prev.next = current.next;
        }
    }

}
