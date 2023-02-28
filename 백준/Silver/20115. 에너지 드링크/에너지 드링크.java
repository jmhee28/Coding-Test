import java.util.*;
public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double total = 0;
        double max_val = 0;
        for(int i= 0; i < n; i++){
            double x = sc.nextDouble();
            total += x;
            if(max_val < x) max_val = x;

        }
        // double result = (total - max_val) / 2 + max_val;
        double result = (total + max_val) / 2;
        System.out.println(result);
    }
}