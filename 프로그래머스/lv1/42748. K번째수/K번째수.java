import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = {};
        int idx =0;
        int comlen = commands.length;
        answer = new int[comlen];
        for(int i = 0; i < comlen; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(temp);
            // answer.add(temp[commands[i][2]]);
            answer[idx++] = temp[commands[i][2]-1];
            
        }
        // System.out.println(commands.length);
        return answer;
    }
}