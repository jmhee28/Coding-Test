
import java.util.*;

public class Main {
    static int[][] board;
    int cnt;
    static int[] bw = new int[2];
    static int n;
    static void solution(int x, int y, int len){
        if(x >= n || y >= n ){return;}
        int num = board[x][y];
        int flag = 0;
        for(int i = x; i< (x + len); i++ ){
            for(int j = y; j < (y+len); j++){
                if(board[i][j] != num){
                    flag = 1;
                    solution(x,y, len/2);
                    solution(x, (y + len/2), len/2);
                    solution((x + len/2), y, len/2);
                    solution((x + len/2), (y + len/2), len/2);
                    break;
                }
            }
            if(flag == 1){
                break;
            }
        }
        if(flag == 0){
            bw[num] += 1;
        }
    }
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            for(int j =0; j < n; j++){
                board[i][j] = sc.nextInt();
            }
        }
        solution(0,0, n);
        System.out.println(bw[0]);
        System.out.println(bw[1]);
    }
}
