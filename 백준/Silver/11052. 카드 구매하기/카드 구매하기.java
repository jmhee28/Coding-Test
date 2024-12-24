import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] pays = new int[n+1];
        int[] dp = new int[n+1];

        for (int i = 1; i < n + 1; i++) {
            pays[i] = sc.nextInt();
            dp[i] = pays[i];
        }
        
        for (int i = 1; i < n + 1; i++) {
            dp[i] = Math.max(dp[i], dp[1] * i);
            for (int j = 1; j < i; j++) {
                dp[i] = Math.max(dp[j] + dp[i-j], dp[i]);
            }
        }

        System.out.println(dp[n]);
    }
}