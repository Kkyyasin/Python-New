package Stack_QUEUE_DEQUE;

public class BaseballGame {
    public static void baseball(String[] dizi){
        Stack stack=new Stack(10);
        int t=0,s;
        for(int i=0;i<dizi.length;i++){
            try{
                s=Integer.parseInt(dizi[i]);
                stack.push(s);
            }catch (NumberFormatException e){
                if(dizi[i].equals("C"))//c ise bir onceki elemanı siler
                    stack.pop();
                if(dizi[i].equals("D"))//bir onceki elemanı iki katlayıp ekler
                    stack.push((int)stack.peak()*2);
                if(dizi[i].equals("+"))//stack elemanlarını toplar ekler stacke
                {
                    Stack temp=stack;

                    while (!temp.isEmpty())
                        t+=(int) temp.pop();
                }
            }
        }

        System.out.println(t*2);
    }
    public static void main(String[] args){
        String[] str={"5","2","C","D","+"};
        baseball(str);
    }
}
