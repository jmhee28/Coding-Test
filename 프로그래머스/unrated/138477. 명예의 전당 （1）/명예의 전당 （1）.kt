class Solution {
    fun solution(k: Int, score: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        var arr = mutableListOf<Int>()
        for(i in 0 until score.size){
            arr.add(score[i])
            arr = arr.sortedDescending().toMutableList()
            if(arr.size > k){
                arr = arr.take(k).toMutableList()
            }
            answer.add(arr[arr.size-1])
        }
        return answer.toIntArray()
    }
}
