import java.util.*;
import java.util.stream.IntStream;

class Solution {
   public String solution(int[] numbers, String hand) {
        String answer = "";
        int rightThumb = 10;
        int leftThumb = 12;
        int [] leftButtons = {1, 4, 7};

        int [] rightButtons = {3, 6, 9};
        String handChar = hand.equals("left")?"L":"R";

        for(int i = 0; i < numbers.length; i++) {
            int curNum = numbers[i];
            String handMoved = "";
            if(IntStream.of(leftButtons).anyMatch(x -> x == curNum)) {
                handMoved = "L";
            } else if (IntStream.of(rightButtons).anyMatch(x -> x == curNum)) {
                handMoved = "R";
            } else {
                int[] rightThumbRC = getRC(rightThumb);
                int[] leftThumbRC = getRC(leftThumb);
                int[] curThumbRC = getRC(curNum);
                int rightToCur = distance(rightThumbRC, curThumbRC);
                int leftToCur = distance(leftThumbRC, curThumbRC);
                if (rightToCur < leftToCur){
                    handMoved = "R";
                    rightThumb = curNum;
                } else if (rightToCur > leftToCur) {
                    handMoved = "L"   ;
                } else {
                    handMoved = handChar;
                }
            }

            if(handMoved.equals("L")){
                answer += "L";
                leftThumb = curNum;
            } else {
                answer += "R";
                rightThumb = curNum;
            }

        }

        return answer;
    }

    public int[] getRC(int target) {
        if (target == 0) {
            return new int[]{3, 1};
        }
        target -= 1;
        int r = target  / 3;
        int c = (target % 3);
        return new int[]{r, c};
    }

    public int distance(int[] a, int[] b){
        return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    }
}