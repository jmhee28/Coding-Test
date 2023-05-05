import java.util.*;
class Node{
    private String str;
    private int cnt;
    
    public Node(String str, int cnt){
        this.str = str;
        this.cnt = cnt;
    }
    public int getCnt(){
        return this.cnt;
    }
    public String getStr(){
        return this.str;
    }
}
class Solution {
    int charLen;
    public int checkStr(String curStr, String comStr){
        int c = 0;
        for(int i = 0; i < charLen; i++){
            char a = curStr.charAt(i);
            char b = comStr.charAt(i);
            if(a != b){
                c += 1;
                if(c >= 2){ return 0;}
            }
        }
        return 1;
        
    }
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        charLen = begin.length();
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(begin,0));
        int wlen = words.length;
        int[] visited = new int[wlen];
        
        while(!q.isEmpty()){
            Node node = q.poll();
            String str = node.getStr();
            int cnt = node.getCnt();
            
            if (str.equals(target)){
                answer = cnt;
                break;
            }
            for(int i = 0; i < wlen; i++ ){
                if(visited[i] == 0 && checkStr(str, words[i]) == 1){
                    visited[i] = 1;
                    q.offer(new Node(words[i], cnt+1));
                }
            }
        }
        return answer;
    }
}