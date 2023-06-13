package Diziler;

import java.util.*;

public class majorty_element {

    public static int majory(int[] dizi){
        int result=dizi[0],count=0;
        for (int i=0;i< dizi.length;i++){
            if(count==0){//eleman yoksa veya silinmisse degistirir baskın elemanı
                result=dizi[i];
            }
            if(result==dizi[i]){
                count++;
            }
            else{//farklı eleman buldumu
                count--;
            }
        }
        return result;
    }

    public static void main(String[] args){
        int[] dizi={1,4,5,4,8,4,4,5};
        //Baskın elemanı bulma
        System.out.println(majory(dizi));

    }
}
