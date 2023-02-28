import java.util.*;

public class Main{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int one = 0;
        int zero = 0;
        String s = sc.next();
        if (s.charAt(0) == '1')
        {
            one += 1;
        }
        else{
            zero += 1;
        }
        for(int i  = 0; i < s.length()-1; i++ ){
            if(s.charAt(i) != s.charAt(i+1)){
                if (s.charAt(i+1) == '1'){
                    one +=1;
                }
                else{
                    zero += 1;
                }
            }
        }
        System.out.println(Math.min(one, zero));
    }
}