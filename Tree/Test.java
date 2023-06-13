package Tree;

public class Test {
    public static String reverse_string(String s,int i){
        if(0<i)
            return s.charAt(i)+reverse_string(s,i-1);
        else
            return String.valueOf(s.charAt(0));
    }

    public static void main(String[] args){
        BinarySearchTree binarySearchTree=new BinarySearchTree();
        binarySearchTree.insert(8);//kok belirlenir
        binarySearchTree.insert(4);//sola yazılır
        binarySearchTree.insert(9);//saga yazılır
        binarySearchTree.insert(5);
        binarySearchTree.insert(3);
        binarySearchTree.insert(11);
    //Degerler varmı kontrol edilir
        System.out.println(binarySearchTree.contains(4));
        System.out.println(binarySearchTree.contains(7));
        System.out.println(binarySearchTree.contains(11));
        System.out.println(binarySearchTree.minData());
        System.out.println(binarySearchTree.maxData());
        String s="Merhaba";
        System.out.println(reverse_string(s,s.length()-1));
        binarySearchTree.inorder(binarySearchTree.kok);
        System.out.println();
        binarySearchTree.postorder(binarySearchTree.kok);
        System.out.println();
        binarySearchTree.preorder(binarySearchTree.kok);
        binarySearchTree.invalidTree(binarySearchTree.kok);
        System.out.println();
        binarySearchTree.inorder(binarySearchTree.kok);
    }
}
