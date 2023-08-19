class Solution {
    fun solution(food: IntArray): String {
        var answer: String = ""
        var a = mutableListOf<Int>()
        for(i in 1 until food.size){
            var cnt = food[i] / 2
            for(j in 0 until cnt.toInt()){
                a.add(i)
            }
        }
        var b = a.reversed()
        a.add(0)
        var com = a+b
        answer = com.joinToString(separator = "")
        
        return answer
    }
}