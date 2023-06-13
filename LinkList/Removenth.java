package LinkList;

public class Removenth {//sonda x elemanı çıkar
    public static void main(String[] args){
        DoubleLinkList<Integer> doubleLinkList=new DoubleLinkList<>();
        doubleLinkList.add(1);
        doubleLinkList.add(2);
        doubleLinkList.add(3);
        doubleLinkList.add(4);
        doubleLinkList.add(5);
        doubleLinkList.display();
        doubleLinkList.removenth(3);
        doubleLinkList.display();


    }
}
