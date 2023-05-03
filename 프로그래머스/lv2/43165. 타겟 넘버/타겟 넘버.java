
import java.util.*;
public class Solution {
    int len = 0;
    int cnt = 0;
    public int getSum(ArrayList<Integer> arr){
        int sum = 0;
        for(int i = 0; i < arr.size(); i++){
            sum += arr.get(i);
        }
        return sum;
    }
    public void dfs(ArrayList<Integer> arr, int idx, int target, int[] numbers){
        if(arr.size() == len ){
            if(getSum(arr) == target)
                cnt += 1;
            return;
        }
        if(idx < len){
            ArrayList<Integer> temp = (ArrayList<Integer>)arr.clone();
            temp.add(numbers[idx]);
            dfs(temp, idx+1, target, numbers);
            temp.remove(temp.size()-1);
            temp.add(numbers[idx]*(-1));
            dfs(temp, idx+1, target, numbers);
        }
    }
    public int solution(int[] numbers, int target) {
        int answer = 0;
        len = numbers.length;
        ArrayList<Integer> arr = new ArrayList<>();
        dfs(arr, 0, target, numbers);
        answer = cnt;
        return answer;
    }
}