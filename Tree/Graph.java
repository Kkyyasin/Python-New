package Tree;

import Stack_QUEUE_DEQUE.QUEUE;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class Graph {
    HashMap<String, ArrayList<String>> adjDic;

    public Graph() {
        adjDic=new HashMap<>();
    }
    public void addVertex(String vertex){//Dugum ekleme
        if(!adjDic.keySet().contains(vertex)){//vertex yani dugum yoksa ekleme işlemi yapılır
            ArrayList<String> edges=new ArrayList<>();//baglantı listesi olusturlur
            adjDic.put(vertex,edges);//dugum ve baglanti listesi eklenir
        }
    }
    public void addEdge(String vertex1,String vertex2){//Baglantı ekleme
        if(adjDic.keySet().contains(vertex1) && adjDic.keySet().contains(vertex2)){//iki dugumde varmı kontrol edilir
            adjDic.get(vertex1).add(vertex2);//birbirlerine baglanti eklenir
            adjDic.get(vertex2).add(vertex1);
        }
    }
    public void deleteEdge(String vertex1,String vertex2){
        if(adjDic.keySet().contains(vertex1) && adjDic.keySet().contains(vertex2)){//iki dugumde varmı kontrol edilir
        try{//baglantı yoksa catch atlar bir sey yapmaz
            adjDic.get(vertex1).remove(vertex2);
        }
        catch (Exception e){

        }
            try{
                adjDic.get(vertex2).remove(vertex1);
            }
            catch (Exception e){

            }
        }
    }
    public void DFS(String startVertex) {
        HashSet<String> visited = new HashSet<>(); // Ziyaret edilen düğümleri takip etmek için
        DFSUtil(startVertex, visited);
    }

    private void DFSUtil(String currentVertex, HashSet<String> visited) {
        visited.add(currentVertex);//ziyaret edilenlere ilk bata baslangıc belirlediimiz konulur
        System.out.print(currentVertex + " ");

        ArrayList<String> neighbors = adjDic.get(currentVertex);//baslangic elemanın baglantıları aarrayliste atanır
        for (String neighbor : neighbors) {//bağlantılar gezilir
            if (!visited.contains(neighbor)) {//egreki baslangic noktasinin baglantısı olmadıkları için girilir
                DFSUtil(neighbor, visited);//hasset te ziyaret edilir bir kere ziyaret olur
            }
        }
    }
    // BFS (Genişlik Öncelikli Arama) algoritması
    public void BFS(String startVertex) {
        HashSet<String> visited = new HashSet<>(); // Ziyaret edilen düğümleri takip etmek için bir HashSet oluşturulur
        QUEUE queue=new QUEUE(100); // BFS sırasında ziyaret edilecek düğümleri tutmak için bir kuyruk (Queue) oluşturulur

        visited.add(startVertex); // Başlangıç düğümü ziyaret edildi olarak işaretlenir
        queue.enqueu(startVertex); // Başlangıç düğümü kuyruğa eklenir

        while (!queue.isEmpty()) { // Kuyruk boş olmadığı sürece döngü devam eder
            String currentVertex = (String) queue.dequeu(); // Kuyruğun başındaki düğüm çıkarılır ve currentVertex'e atanır
            System.out.print(currentVertex + " "); // Çıkarılan düğüm ekrana yazdırılır

            ArrayList<String> neighbors = adjDic.get(currentVertex); // Çıkarılan düğümün komşuları alınır
            for (String neighbor : neighbors) { // Komşular üzerinde döngü ile gezinilir
                if (!visited.contains(neighbor)) { // Eğer komşu daha önce ziyaret edilmemişse
                    visited.add(neighbor); // Komşu ziyaret edildi olarak işaretlenir
                    queue.enqueu(neighbor); // Komşu kuyruğa eklenir
                }
            }
        }
    }

    public void removeVertex(String vertex){
        if(adjDic.keySet().contains(vertex)){
            for(String a:adjDic.get(vertex))
                adjDic.get(a).remove(vertex);//vertex her baglantıdan siler
            adjDic.remove(vertex);//vertex silinir
        }
    }
    public void show(){
        for(String a:adjDic.keySet())
            System.out.println(a+" --> "+adjDic.get(a));
    }
    public static void main(String[] args){
        Graph graph=new Graph();
        graph.addVertex("A");
        graph.addVertex("B");
        graph.addVertex("C");
        graph.addEdge("A","C");
        graph.addEdge("B","C");
        graph.show();
        graph.removeVertex("C");
        graph.show();


    }
}
