package Diziler;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Containis_Duplicate {
    public static boolean contais(Integer[] dizi){//Q(n^2) zaman q(1) yer
        for(int i=0;i< dizi.length;i++){
            for(int j=i+1;j<dizi.length;j++)
                if (dizi[i]==dizi[j]){
                    return true;}
        }
        return false;
    }
    public static boolean contais2(Integer[] dizi){
        Set<Integer> set = new HashSet<>();
        for (int num : dizi) {//
            if (set.contains(num)) {
                return true;
            }
            set.add(num);//aynı elemandan varsa eklemez Q(n) zaman Q(n) yer
        }
        return false;
    }
    public static boolean contais3(Integer[] dizi){
        Arrays.sort(dizi);
        for(int i=1;i<dizi.length;i++){
            if(dizi[i]==dizi[i-1])
                return true;
        }
        return false;
    }
    public static void main(String[] args){
        Integer[] dizi={1,2,3,4,1},dizi2={1,2,3,4};
        System.out.println(contais(dizi));//kaba kuvvet
        System.out.println(contais(dizi2));
        System.out.println(contais2(dizi));//setleme
        System.out.println(contais2(dizi2));
        System.out.println(contais3(dizi));//sırlayarak çözüm
        System.out.println(contais3(dizi2));
    }
}
