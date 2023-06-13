package LinkList;



public class Kesisim {
    public static Object kesisim(SingleLinkList<Integer> s1,SingleLinkList<Integer> s2){
        SingleNode temp1=s1.head;
        SingleNode temp2=s2.head;
        int i=1,j=1;
        while (temp1 != null && temp2 != null) {
            if (temp1.data.equals(temp2.data)) {
                System.out.println(i+" "+j+" "+temp1.data);
                return temp1.data;
            }
            temp2 = temp2.next;

            if (temp2 == null) {
                temp2 = s2.head;
                temp1 = temp1.next;
                j=1;
                i++;
            }
           j++;

        }

        return null;
    }
    public static void main(String[] args){
        SingleLinkList<Integer> singleLinkList=new SingleLinkList<>();
        SingleLinkList<Integer> singleLinkList2=new SingleLinkList<>();
        //1 Link List 1 2 3 4 5
        singleLinkList.LastAdd(1);
        singleLinkList.LastAdd(2);
        singleLinkList.LastAdd(3);
        singleLinkList.LastAdd(4);
        singleLinkList.LastAdd(5);
        //2 Link List 4 5 6 7 8
        singleLinkList2.LastAdd(3);
        singleLinkList2.LastAdd(4);
        singleLinkList2.LastAdd(6);
        singleLinkList2.LastAdd(7);
        singleLinkList2.LastAdd(8);
        singleLinkList.show();
        singleLinkList2.show();
        //1 linklist i 4 2 limk list j 0 elemanda kesisir ortak eleman 4
        System.out.println(singleLinkList.head.data);
        if(kesisim(singleLinkList,singleLinkList2)==null){
            System.out.println("Elemanlar Kesismez");
        }

    }
}
