package Search;

public class Hash {
    int size;
    Object[] dizi;

    public Hash(int size) {
        this.size = size;
        dizi=new Object[size];
    }
    public int hash(String s){
        int value = 0;
        for(int i=0;i<s.length();i++){
            value+=s.charAt(i);
        }
        value%=size;
        return value;
    }public int hash(int s){

        return s%size;
    }
    public void ekle(String  obj){
        int hashvalue=hash(obj);
        int i=0;
        while (i<size){
            if(dizi[hashvalue]==null){
                dizi[hashvalue]=obj;
                return;
            }
            else
                hashvalue=(hashvalue+i)%size;
            i++;
        }
        System.out.println("Dolu hash");
    }


    public int bul(String obj){
        int hashvalue=hash(obj);
        int i=0;
        while (i<size){
            if(dizi[hashvalue].equals(obj)){;
                return hashvalue;
            }
            else
                hashvalue=(hashvalue+i)%size;
            i++;
        }
        return -1;
    }
    public void ekle(int obj) {
        int hashvalue = hash(obj);
        int i = 0;
        while (i < size) {
            if (dizi[hashvalue] == null) {
                dizi[hashvalue] = obj;
                return;
            } else if (dizi[hashvalue].equals(obj)) {
                return; // Aynı obje zaten tabloda var, ekleme yapma
            } else {
                hashvalue = (hashvalue + i) % size;
                i++;
            }
        }
        // Tablo dolu, ekleme yapılamıyor
    }

    public int bul(int obj) {
        int hashvalue = hash(obj);
        int i = 0;
        while (i < size && dizi[hashvalue] != null) {
            if (dizi[hashvalue].equals(obj)) {
                return hashvalue;
            } else {
                hashvalue = (hashvalue + i) % size;
                i++;
            }
        }
        return -1; // Eleman bulunamadı
    }

    public void show(){
        for(Object a:dizi){
            if(a!=null)
                System.out.println(a);
        }
    }
    public static void main(String args[]){
        Hash hash=new Hash(100);
        hash.ekle("Merhaba");
        hash.ekle("Yasin");
        hash.ekle("Özdemir");
        hash.show();
        System.out.println(hash.bul("Yasin"));
    }
}
