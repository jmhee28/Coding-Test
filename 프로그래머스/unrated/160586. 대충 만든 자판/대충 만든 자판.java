import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = {};
        answer = new int[targets.length];
        int idx = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        
        for(int i = 0; i < keymap.length; i++){
            for(int j = 0; j < keymap[i].length(); j++){
                char x = keymap[i].charAt(j);
                
                if(map.containsKey(x))
                {
                    if( map.get(x) > j+1)
                    {
                        map.remove(x);
                        map.put(x, j+1);
                    }
                }
                else{
                    map.put(x, j+1);
                }
            }
        }
        
        for (int i = 0; i < targets.length; i++){
            String target = targets[i];
            int cnt = 0;
            for(int j = 0; j< target.length(); j++){
                char t = target.charAt(j);
                if (!map.containsKey(t)){
                    cnt = -1;
                    break;
                }
                else{
                    cnt += map.get(t);
                }
            }
            answer[idx++] = cnt;
        }
        return answer;
    }
}