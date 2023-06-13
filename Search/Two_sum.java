package Search;

import java.util.ArrayList;

public class Two_sum {
    public static ArrayList<Integer[]> twosum(int[] dizi,int target) {
        Hash hash = new Hash(dizi.length);
        System.out.println(hash.size);
        ArrayList<Integer[]>arrayList=new ArrayList<>();
        for(Integer a:dizi)
            hash.ekle(a);
        int deger;
        for(int i=0;i<dizi.length;i++){
            deger=hash.bul(target-dizi[i]);
            if(deger!=-1){
                Integer[] c={i,deger};
                arrayList.add(c);
            }
        }
        return arrayList;
    }
    public static void main(String[] args){
        int[] dizi={3,2,4};
        ArrayList<Integer[]>arrayList=twosum(dizi,6);
        if(arrayList.size()!=0)
        {
            for(Integer[] a:arrayList)
                System.out.print("["+a[0]+","+a[1]+"]"+" , ");
        }
        else
            System.out.println("Bulunamadı");
    }
}
