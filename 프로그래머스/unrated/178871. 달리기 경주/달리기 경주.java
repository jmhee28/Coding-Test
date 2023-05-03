import java.util.*;

class Solution {

    public String[] solution(String[] players, String[] callings) {
        int plen = players.length;
        int clen = callings.length;
        String[] answer = new String[plen];
        HashMap <String, Integer> nameMap = new HashMap();
        HashMap <Integer, String> idxMap = new HashMap();
        
        for(int i = 0; i < plen; i++){
            nameMap.put(players[i], i);
            idxMap.put(i, players[i]);
        }
        int iniIdx;
        String changeName;
        for(int i = 0; i< clen; i++){
            iniIdx = nameMap.remove(callings[i]);
            changeName = idxMap.remove(iniIdx-1);
            nameMap.remove(changeName);
            idxMap.remove(iniIdx);
            nameMap.put(changeName, iniIdx);
            nameMap.put(callings[i], iniIdx-1);
            idxMap.put(iniIdx, changeName);
            idxMap.put(iniIdx-1,callings[i]);            
        }
        for(int i = 0; i < plen; i++ ){
            answer[i] = idxMap.get(i);
        }
        return answer;
    }
}