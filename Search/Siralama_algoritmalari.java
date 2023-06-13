package Search;

import java.util.Arrays;

public class Siralama_algoritmalari {
    public static void bubbleSort(int[] dizi){//Q(n^2)
        for(int i=0;i<dizi.length-1;i++){
            for(int j=0;j<dizi.length-i-1;j++){//ikiser saga dogru gezer sona ekler
                if(dizi[j]>dizi[j+1]){
                    int temp=dizi[j];
                    dizi[j]=dizi[j+1];
                    dizi[j+1]=temp;
                }
            }
        }
    }
    public static void selectionSort(int[] dizi){//q(n^2)
        for(int i=0;i<dizi.length-1;i++){
            int min=i;
            for(int j=i+1;j<dizi.length;j++){
                if(dizi[j]<dizi[min])//en kucuk elemanın indisini bulur
                    min=j;
            }
            int temp=dizi[i];//minumum değeri basa alır
            dizi[i]=dizi[min];
            dizi[min]=temp;
        }
    }
    public static void insetionSort(int[] dizi){//n^2
        for(int i=1;i<dizi.length;i++){
            int key=dizi[i];//elemanı gecici olarak key atanır
            int j=i-1;//bir onceki eleman j indisine alınır
            while (j>=0 && dizi[j]>key){//basa gelmeden ve solundaki eleman daha kucugunu buluna kadar sola kaydırır
                dizi[j+1]=dizi[j];//key elemanın oldugu yere saga kaydırarak kucuk bulana kadar yapılır
                j--;
            }
            dizi[j+1]=key;//kucugu buldugumu degistimez sag tarafına koyar
        }
    }
    public static void mergeSort(int[] dizi){//elemanaları çiftler halinde birleştirip ikise doger seklde aralarında karsılastırır
        //nlogn
        if(dizi.length>1){
            int orta=dizi.length/2;//orta nokta bulunur
            int[] left= Arrays.copyOfRange(dizi,0,orta);//ortanın sol kısmı ayrı dizi
            int[] right= Arrays.copyOfRange(dizi,orta,dizi.length);//ortanın sag kısmı ayrı dizi
            mergeSort(left);//recersive yaklasımla birlestirilr
            mergeSort(right);

            merge(dizi,left,right);//dizi ler karsilastirilir
        }
    }
    public static void merge(int[] dizi,int[] left,int[] right){
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                dizi[k] = left[i];
                i++;
            } else {
                dizi[k] = right[j];
                j++;
            }
            k++;
        }
        while (i < left.length) {
            dizi[k] = left[i];
            i++;
            k++;
        }
        while (j < right.length) {
            dizi[k] = right[j];
            j++;
            k++;
        }
    }
    public static void quickSort(int[] arr, int low, int high) {//q(n^2)
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);
        return i + 1;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }


}
