package Tree;

public class AVLNode {
    AVLNode left,right;
    int value,yukseklik;

    public AVLNode(int value) {
        this.value = value;
        yukseklik=1;//agacin yuksekligi 1 baslatilir
    }
}
