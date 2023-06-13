package Search;

public class Search {
    public static int SirasizArama(int[] dizi, int a) {
        for(int i = 0; i < dizi.length; ++i) {
            if (dizi[i] == a) {
                return i;
            }
        }

        return -1;
    }
    public static double interpolate(double[] x, double[] y, double targetX) {
        // İnterpolasyon yöntemi olarak lineer interpolasyon kullanalım
        int n = x.length;
        int i = 0;

        // İnterpolasyon aralığını bulalım
        while (i < n && x[i] < targetX) {
            i++;
        }

        // Hedef değeri tahmin etmek için lineer interpolasyon yapalım
        if (i == 0) {
            return y[0]; // İlk noktada hedef değerini tahmin etmek için sadece ilk değeri kullanalım
        } else if (i == n) {
            return y[n - 1]; // Son noktada hedef değerini tahmin etmek için sadece son değeri kullanalım
        } else {
            // İki veri noktası arasında lineer interpolasyon yapalım
            double x0 = x[i - 1];
            double x1 = x[i];
            double y0 = y[i - 1];
            double y1 = y[i];
            return y0 + (targetX - x0) * (y1 - y0) / (x1 - x0);
        }
    }

public static int Sirali(int[] dizi, int a) {
        for(int i = 0; i < dizi.length; ++i) {
            if (dizi[i] == a) {
                return i;
            }

            if (dizi[i] > a) {
                return -1;
            }
        }

        return -1;
    }

    public static int binary(int[] dizi, int a) {
        int son = dizi.length;
        int bas = 0;

        while(bas < son) {
            int mid = (bas + son) / 2;
            if (dizi[mid] == a) {
                return mid;
            }

            if (dizi[mid] > a) {
                son = mid - 1;
            } else {
                bas = mid + 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] sirasizdizi = new int[]{1, 4, 1, 5, 80, 20, 2};
        int[] sirarli = new int[]{1, 2, 3, 5, 11, 24};
        System.out.println(SirasizArama(sirasizdizi, 80));
        System.out.println(Sirali(sirarli, 5));
        System.out.println(binary(sirarli, 5));
    }
}
