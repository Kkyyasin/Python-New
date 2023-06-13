package Tree;

public class AVLTree {
    AVLNode kok;
    //Avl Tree agacin sol ve sag tarafi esit durmasi icin koklerde kaydirma yapmasidir
    public int height(AVLNode node){
        if(node==null)//yukseklik 1 den baslar
            return 0;
        return node.yukseklik;//agacin yuksekligini dondurur
    }
    // İki değer arasındaki maksimum değeri döndüren yardımcı bir yöntem
    public int max(int a, int b) {
        return (a > b) ? a : b;
    }
    // Bir düğümün denge faktörünü hesaplayan yardımcı bir yöntem
    public int getBalance(AVLNode node){
        if(node==null)
            return 0;
        return height(node.left)-height(node.right);//agacin sol ve sag taraftaki farkı dondurur farkın kapanması saglanır

    }
    public AVLNode rotaterigh(AVLNode y){//agacin sag tarafa kaydırmaya yarar
        AVLNode x = y.left;
        AVLNode T2 = x.right;
        //y ninci elemana kaydırılır
        // Döndürme işlemi
        x.right = y;
        y.left = T2;

        // Yükseklikleri güncelleme
        y.yukseklik = max(height(y.left), height(y.right)) + 1;
        x.yukseklik = max(height(x.left), height(x.right)) + 1;

        return x;
    }
    // Ağacı sola döndürmek için yardımcı bir yöntem
    AVLNode rotateLeft(AVLNode x) {
        AVLNode y = x.right;
        AVLNode T2 = y.left;

        // Döndürme işlemi
        y.left = x;
        x.right = T2;

        // Yükseklikleri güncelleme
        x.yukseklik = max(height(x.left), height(x.right)) + 1;
        y.yukseklik = max(height(y.left), height(y.right)) + 1;

        return y;
    }
    AVLNode insertNode(AVLNode node, int key) {
        // Standart BST ekleme işlemi
        if (node == null)
            return (new AVLNode(key));

        if (key < node.value)
            node.left = insertNode(node.left, key);
        else if (key > node.value)
            node.right = insertNode(node.right, key);
        else // Aynı anahtara sahip düğüm zaten var
            return node;

        // Düğümün yüksekliğini güncelleme
        node.yukseklik = 1 + max(height(node.left),height(node.right));
        // Denge faktörünü kontrol etme ve ağacı yeniden düzenleme
        int balance = getBalance(node);

        // Sol-sol durumu: Denge faktörü 2 veya daha fazlaysa ve yeni düğüm sol alt ağaçta yer alıyorsa
        if (balance > 1 && key < node.left.value)
            return rotaterigh(node);

        // Sağ-sağ durumu: Denge faktörü -2 veya daha azsa ve yeni düğüm sağ alt ağaçta yer alıyorsa
        if (balance < -1 && key > node.right.value)
            return rotateLeft(node);

        // Sol-sağ durumu: Denge faktörü 2 veya daha fazlaysa ve yeni düğüm sol alt ağaçta yer almıyorsa
        if (balance > 1 && key > node.left.value) {
            node.left = rotateLeft(node.left);
            return rotaterigh(node);
        }

        // Sağ-sol durumu: Denge faktörü -2 veya daha azsa ve yeni düğüm sağ alt ağaçta yer almıyorsa
        if (balance < -1 && key < node.right.value) {
            node.right = rotaterigh(node.right);
            return rotateLeft(node);
        }

        // Yeni düğüm eklenmiş olmasına rağmen ağaç dengeli durumda ise düğümü geri döndürme
        return node;
    }

    // Ağacı gezerek düğümü silen yardımcı bir yöntem
    AVLNode deleteNode(AVLNode root, int key) {
        // Standart BST silme işlemi
        if (root == null)
            return root;

        if (key < root.value)
            root.left = deleteNode(root.left, key);
        else if (key > root.value)
            root.right = deleteNode(root.right, key);
        else {
            // Silinecek düğümü bulduk

            // Yalnızca bir veya hiç çocuğu olan düğüm durumu
            if ((root.left == null) || (root.right == null)) {
                AVLNode temp = null;
                if (temp == root.left)
                    temp = root.right;
                else
                    temp = root.left;

                // Çocuk düğüm yoksa
                if (temp == null) {
                    temp = root;
                    root = null;
                } else // Tek bir çocuğu olan düğüm durumu
                    root = temp;
            } else {
                // İki çocuğu olan düğüm durumu
                AVLNode temp = minValueNode(root.right);

                // En küçük değere sahip düğümü kopyalama
                root.value = temp.value;

                // En küçük değere sahip düğümü silme
                root.right = deleteNode(root.right, temp.value);
            }
        }

        // Yalnızca bir düğüm varsa (veya hiç düğüm yoksa) durumu
        if (root == null)
            return root;

        // Düğümün yüksekliğini güncelleme
        root.yukseklik = 1 + max(height(root.left), height(root.right));

        // Denge faktörünü kontrol etme ve ağacı yeniden düzenleme
        int balance = getBalance(root);

        //
// Sol-sol durumu: Denge faktörü 2 veya daha fazlaysa ve sol alt ağaçtaki düğüm yüksek ise
        if (balance > 1 && getBalance(root.left) >= 0)
            return rotaterigh(root);

// Sağ-sağ durumu: Denge faktörü -2 veya daha azsa ve sağ alt ağaçtaki düğüm yüksek ise
        if (balance < -1 && getBalance(root.right) <= 0)
            return rotateLeft(root);

// Sol-sağ durumu: Denge faktörü 2 veya daha fazlaysa ve sol alt ağaçtaki düğüm düşük ise
        if (balance > 1 && getBalance(root.left) < 0) {
            root.left = rotateLeft(root.left);
            return rotaterigh(root);
        }

// Sağ-sol durumu: Denge faktörü -2 veya daha azsa ve sağ alt ağaçtaki düğüm düşük ise
        if (balance < -1 && getBalance(root.right) > 0) {
            root.right = rotaterigh(root.right);
            return rotateLeft(root);
        }

// Ağaç dengede ise düğümü geri döndürme
        return root;
    }

    // Minimum değere sahip düğümü bulan yardımcı bir yöntem
    AVLNode minValueNode(AVLNode node) {
        AVLNode current = node;

// Sol alt ağaca kadar en küçük değere sahip düğümü bulma
        while (current.left != null)
            current = current.left;

        return current;
    }

    // AVL ağacını inorder olarak gezerek düğümleri yazdıran yardımcı bir yöntem
    void inorder(AVLNode node) {
        if (node != null) {
            inorder(node.left);
            System.out.print(node.value + " ");
            inorder(node.right);
        }
    }
}
