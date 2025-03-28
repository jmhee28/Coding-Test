
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int[] dp = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        dp[0] = arr[0];
        if(n > 1){
            dp[1] = arr[0] + arr[1];
        }
        if (n > 2){
            dp[2] = Math.max(arr[2] + arr[0], arr[2] + arr[1]);
            dp[2] = Math.max(dp[2], dp[1]);
        }

        for (int i = 3; i < n; i++) {
            dp[i] = Math.max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2]);
            dp[i] = Math.max(dp[i], dp[i-1]);
        }

        System.out.println(dp[n-1]);
    }
}