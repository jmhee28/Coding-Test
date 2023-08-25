import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        long[][] board = new long[n][m];
        long[][] cnt = new long[n][m];

        for (int[] puddle : puddles) {
            board[puddle[1] - 1][puddle[0] - 1] = -1L;
        }
        for (int i = 1; i < m; i++) {
            if(board[0][i] == -1L){
                break;
            }
            cnt[0][i] = 1L;
        }
        for (int i = 1; i < n; i++) {
            if(board[i][0] == -1L){
                break;
            }
            cnt[i][0] = 1L;
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (board[i][j] != -1L) {
                    cnt[i][j] =  (cnt[i-1][j] + cnt[i][j-1]) % 1000000007L;
                }
            }
        }

        return Long.valueOf(cnt[n-1][m-1]).intValue();
    }
}
// public class Main {
//     public static void main(String[] args) {
//         School school = new School();

//         int m = 4;
//         int n = 3;
//         int[][] puddles = {{1, 2}, {2, 1}};

//         int result = school.solution(m, n, puddles);
//         System.out.println("Result: " + result);
//     }
// }
