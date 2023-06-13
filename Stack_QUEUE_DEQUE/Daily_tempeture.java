package Stack_QUEUE_DEQUE;

import java.util.Stack;

public class Daily_tempeture {

    public static int[] temperature(int[] dizi) {
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> stack1 = new Stack<>();
        int[] s = new int[dizi.length];
        int temp, gun;
        for (int i = 0; i < dizi.length; i++)
            stack.push(dizi[i]);
        for (int i = 0; i < s.length; i++) {
            temp = stack.pop();
            stack1.push(temp);
            gun = 0;
            while (!stack1.isEmpty() && dizi[i] > temp) {
                gun++;
                temp = stack.pop();
                stack1.push(temp);
            }
            s[i] = gun;
            while (!stack1.isEmpty())
                stack.push(stack1.pop());
        }
        for (int i = 0; i < dizi.length; i++)
            System.out.print(s[i] + " ");
        return s;
    }

    public static void main(String[] args) {
        temperature(new int[]{73, 74, 75, 71, 69, 72, 76, 73});
    }
}
