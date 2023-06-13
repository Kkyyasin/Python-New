package Stack_QUEUE_DEQUE;

public class Test {
    public static void main(String[] args){
        Stack stack=new Stack(10);
        stack.push(5);
        stack.push(4);
        stack.push(4);
        System.out.println(stack.pop());
        stack.show();
        QUEUE<Integer> queue=new QUEUE<>(10);
        queue.enqueu(4);
        queue.enqueu(3);
        queue.enqueu(1);
        queue.enqueu(2);
        System.out.println(queue.dequeu());
        System.out.println(queue.peek());
            }

}
