package Stack_QUEUE_DEQUE;

public class QUEUE <E>{
    E[] dizi;
    int front,rear,size,kapasite;

    public QUEUE(int kapasite) {
        dizi=(E[]) new Object[kapasite];
        this.kapasite = kapasite;
        front=0;//ilk çıkacak eleman değişmez
        rear=-1;//konumu değişir
        size=0;//doluluk oranı
    }
    public void enqueu(E obj){//rear değişir
        if(size==kapasite){
            System.out.println("QUEUE dolu...");
            return;
        }
        rear=(rear+1)%kapasite;//asla kapasiteye aşmıcak sekilde konum belirlenir
        dizi[rear]=obj;
        size++;
    }
    public E dequeu(){//front degisir
        if(size==0){
            System.out.println("QEUEU bos...");
            return null;
        }
        E temp=(E) dizi[front];
        dizi[front]=null;
        front=(front+1)%kapasite;
        size--;
        return temp;
    }
    public E peek(){
        if(size==0){
            System.out.println("QEUEU bos...");
            return null;
        }
        return (E)dizi[front];
    }
    public boolean isEmpty(){
        if(size==0){
            return true;
        return false;
    }
    public int size(){
        return size();
    }
}
