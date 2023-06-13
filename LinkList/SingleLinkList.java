package LinkList;

import javax.swing.text.TabExpander;

public class SingleLinkList <E>{
    SingleNode head;
    SingleNode temp;
    public void LastAdd(E obj){
        if(head==null)
            head=new SingleNode(obj);
        else{
            temp=head;
            while (temp.next!=null){
                temp=temp.next;
            }
            temp.next=new SingleNode(obj);
        }
    }
    public void BasEkle(E obj){
        if(head==null)
            head=new SingleNode(obj);
        else{
            temp=new SingleNode(obj);
            temp.next=head;
            head=temp;
        }
    }
    public void show(){
        temp=head;
        while (temp!=null){
            System.out.print(temp.data+"  ");
            temp=temp.next;
        }
    }
    public E lastdelete(){
        if(isEmpty())
            return null;
        temp=head;
        if (temp.next == null) {
            E s = (E) temp.data;
            head = null;
            return s;
        }
        while (temp!=null)
            temp=temp.next;
        E s= (E) temp.data;
        temp=null;
        return s;
    }
    public void delete(E obj){
        if(isEmpty())
            return;
        temp=head;
        while (temp.next!=null){
            if(temp.next.data.equals(obj)){
                E s= (E) temp.next.data;
                System.out.println(s+" silindi...");
                temp.next=temp.next.next;
                return;
            }
            temp=temp.next;
        }
    }
    public E basdelete(){
        if(isEmpty())
            return null;
        E s=(E) head.data;
        head=head.next;
        return s;
    }
    public boolean isEmpty(){
        if(head==null) {
            System.out.println("LinkList bos...");
            return true;
        }
        return false;
    }

}
