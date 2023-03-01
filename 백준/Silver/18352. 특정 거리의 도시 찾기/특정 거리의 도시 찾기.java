import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        int x = sc.nextInt();
        int[] d = new int[300001];
        ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
        
        for(int i = 0; i <= n; i++){
            graph.add(new ArrayList<Integer>());
            d[i] = -1;
        }
        for(int i = 0; i < m; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph.get(a).add(b);
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.add(x);

        d[x] = 0;

        while(queue.size() > 0){
            int now = queue.poll();
            
            for(int i = 0; i< graph.get(now).size(); i++){
                int next = graph.get(now).get(i);
                if(d[next] == -1){
                    d[next] = d[now] + 1;
                    queue.add(next);
                }
            }
        }
        int flag = 0;
        for(int i = 1; i < n+1; i++ ){
            if(d[i] == k){
                System.out.println(i);
                flag = 1;
            }
        }
        if(flag == 0){
            System.out.println(-1);
        }
    }
}
