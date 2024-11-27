import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        int[] clothCount = new int[n+1];
        Arrays.fill(clothCount, 1);

        for(int i = 0; i < lost.length; i++){
            clothCount[lost[i]] -= 1;
        }

        for(int i = 0; i < reserve.length; i++){
            clothCount[reserve[i]] += 1;
        }

        Deque<Integer> stack = new ArrayDeque<Integer>();
        for(int i = 1; i <= n; i++){
            if(clothCount[i] >= 2){
                stack.offer(i);
            }
        }

        while(!stack.isEmpty()){
            int ridx = stack.poll();
            int leftIdx = ridx - 1;
            int rightIdx = ridx + 1;
            if (leftIdx > 0 && clothCount[leftIdx] == 0){
                clothCount[leftIdx] += 1;
                clothCount[ridx] -= 1;
            }
            if (rightIdx <= n && clothCount[rightIdx] == 0 && clothCount[ridx] > 1){
                clothCount[rightIdx] += 1;
                clothCount[ridx] -= 1;
            }
        }

         for (int i = 1; i <= n; i++) {
             if (clothCount[i] > 0){
                 answer += 1;
             }
         }
         System.out.println(answer);
        return answer;
    }
}