
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main{
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};
    public static final int INF  = (int) 1e9;
    public static int[][] rooms;
    public static int[][] distance;
    public static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        rooms = new int[n][n];
        distance = new int[n][n];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                rooms[i][j] = (line.charAt(j) - '0') ^ 1;
                distance[i][j] = INF;
            }
        }
        dijkstra(0, 0);
        System.out.println(distance[n - 1][n - 1]);
    }

    static void dijkstra(int startX, int startY){
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(startX, startY, 0));
        distance[startX][startY] = 0;

        while(!pq.isEmpty()){
            Node current = pq.poll();
            int x = current.x;
            int y = current.y;
            int dist = current.dist;

            if(distance[x][y] < dist){
                continue;

            }
            for (int i = 0; i < 4; i++) {
             int nx = x + dx[i];
             int ny = y + dy[i];
             if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                int cost = dist + rooms[nx][ny];

                if (cost < distance[nx][ny]) {
                    distance[nx][ny] = cost;
                    pq.offer(new Node(nx, ny, cost));
                }
            }
            }
        }
    }

    static class Node implements Comparable<Node>{
        int x, y, dist;
        public Node(int x, int y, int dist){
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        @Override
        public int compareTo(Node other){
            return Integer.compare(this.dist, other.dist);
        }
    }
}