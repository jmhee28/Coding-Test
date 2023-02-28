import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int m = 0;
        String min_val = "";
        String max_val = "";
        for(int i = 0; i < s.length(); i++){
            if (s.charAt(i) == 'M'){
                m += 1;
            }
            else{
                if(m > 0){
                    max_val += "5";
                    for(int j = 0; j < m; j++){
                        max_val += "0";
                    }
                    min_val += "1";
                    for(int j = 0; j < m-1; j++){
                        min_val += "0";
                    }
                    min_val += "5";
                }
                else{
                    max_val += "5";
                    min_val += "5";
                }
                m = 0;
            } 
        }   
        if( m > 0){
            min_val += "1";
            for(int i = 0; i <m-1; i++)
                {
                max_val += "1";
                min_val += "0";
            }
            max_val += "1";
        }
        System.out.println(max_val);
        System.out.println(min_val);

    }
}
