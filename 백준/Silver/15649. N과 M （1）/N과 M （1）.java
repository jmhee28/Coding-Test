import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        int[] arr = new int[m];
        boolean[] visited = new boolean[n];
        dfs(arr, visited, n, m, 0);
    }

    static void dfs(int[] arr, boolean[] visited, int n, int m, int depth ) {
        if(depth == m){
            for(int i = 0; i < m; i++){
                System.out.print(arr[i] + " ");
            }
            System.out.println();
            return;
        }
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                visited[i] = true;
                arr[depth] = i + 1;
                dfs(arr, visited, n, m, depth + 1);
                visited[i] = false;
            }
        }

    }
}