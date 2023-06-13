package Diziler;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class find_single {
    public static int find(int dizi[]){
        int c;
        for(int i=0;i<dizi.length;i++){
            c=0;
            for(int j=0;j<dizi.length;j++){
                if(i!=j && dizi[i]==dizi[j])
                    c=1;
            }
            if(c==0)
                return dizi[i];
        }
        return -1;
    }
    public static int find2(int dizi[]){
        int result =0;
        for(int i=0;i<dizi.length;i++){
            result=result^i;//aynıysa yok tek kalanı verir ^xor isareti
        }
        return result;
    }
    public static void main(String[] args){
        int[] dizi={1,1,2,3,3,4,4},dizi2={1,2,3,4};
        System.out.println(find(dizi));//kaba kuvvet
        System.out.println(find2(dizi));//xor sokarak aynı sonuçların 0 etme sonucu
    }
}
