import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static String str1 = "\"재귀함수가 뭔가요?\"";
    static String str2 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.";

    static String str3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.";
    static String str4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"";
    static String str5 = "\"재귀함수는 자기 자신을 호출하는 함수라네\"";
    static String str6 = "라고 답변하였지.";
    static String underBar = "____";
    static int N;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        System.out.println("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
        recursive(0);
    }

    public static void recursive(int n) {
        if(n == N) {
            return;
        }

        String nstr1 = underBar.repeat(n) + str1;
        String nstr2 = underBar.repeat(n) + str2;
        String nstr3 = underBar.repeat(n) + str3;
        String nstr4 = underBar.repeat(n) + str4;
        System.out.println(nstr1);
        System.out.println(nstr2);
        System.out.println(nstr3);
        System.out.println(nstr4);

        recursive(n+1);
        if(n == N-1) {
            System.out.println(underBar.repeat(n+1) + str1);
            System.out.println(underBar.repeat(n+1) + str5);
            System.out.println(underBar.repeat(n+1) + str6);
        }

//        String nstr5 = underBar.repeat(n) + str5;
        String nstr6 = underBar.repeat(n) + str6;
//        System.out.println(nstr5);
        System.out.println(nstr6);

    }
}
