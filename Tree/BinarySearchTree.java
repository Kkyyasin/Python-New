package Tree;

import Stack_QUEUE_DEQUE.QUEUE;

import java.util.ArrayList;

public class BinarySearchTree {
    Node kok;
    Node temp;
    public boolean insert(int data){
        if(kok==null){
            kok=new Node(data);
            return true;
        }
        else{
            temp=kok;
            Node newNode=new Node(data);
            while (true){
                if(temp.data==newNode.data)//koke deger esitse eklenmez
                    return false;
                if(temp.data > newNode.data){
                    if(temp.left==null){//sol taraf bossa ekler
                        temp.left=newNode;
                        return true;
                    }
                    else//degilse koku sol taraf yapar
                        temp=temp.left;
                }
                else{
                    if(temp.right==null){//sag taraf bossa ekler
                        temp.right=newNode;
                        return true;
                    }
                    else//degilse koku sol taraf yapar
                        temp=temp.right;
                }
            }
        }
    }
    public boolean contains(int x){//x varm yok mu kontrolu
        temp=kok;
        while (temp!=null){
            if(temp.data==x)
                return true;
            else{
                if(temp.data>x){
                    if(temp.left==null)
                        return false;
                    if(temp.left.data==x)
                        return true;
                    else
                        temp=temp.left;
                }
                else{
                    if(temp.right==null)
                        return false;
                    if(temp.right.data==x)
                        return true;
                    else
                        temp=temp.right;
                }
            }
        }
        return false;
    }
    public int minData(){
        temp=kok;
        while (temp.left!=null)
            temp=temp.left;
        return temp.data;
    }
    public int maxData(){
        temp=kok;
        while (temp.right!=null)
            temp=temp.right;
        return temp.data;
    }
    public void inorder(Node kok){//sol kok sag
        if(kok!=null){
            inorder(kok.left);//sol taraf gezilir
            System.out.print(kok.data+"  "); //kok yazilir
            inorder(kok.right);//sag taraf gezilir
        }
    }
    //DFS
    public void preorder(Node kok){
        if(kok!=null){
            System.out.print(kok.data+"  ");//kok
            preorder(kok.left);
            preorder(kok.right);
        }
    }
    public void postorder(Node kok){
        if(kok!=null){
            postorder(kok.left);
            postorder(kok.right);
            System.out.print(kok.data+"  ");
        }
    }
    public void invalidTree(Node kok){//Ters cevirme agaci
        if(kok!=null){
            Node temp=kok.right;
            kok.right=kok.left;
            kok.left=temp;
            invalidTree(kok.left);//sag taraf degisir
            invalidTree(kok.right);//sol taraf degisir
        }
    }
    public ArrayList<Integer> BFS(){//yatay olarak gezinmedir
        temp=kok;
        QUEUE<Node> queue=new QUEUE<>(100);//queue olusturlur
        queue.enqueu(temp);
        ArrayList<Integer> values=new ArrayList<>();//sıralı degerler eklenmek için eklenir
        while (queue.size()>0){//koyacak eleman kalmayana denk devam eder
            temp=queue.dequeu();
            values.add(temp.data);//sırasıyla ilk giren queue dan çıkararak kok - sag solu -sag solların sag solları...
            if(temp.left!=null)
                queue.enqueu(temp.left);
            if(temp.right!=null)
                queue.enqueu(temp.right);
        }
        return values;
    }
}
