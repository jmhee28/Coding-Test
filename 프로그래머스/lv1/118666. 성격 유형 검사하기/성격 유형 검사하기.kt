class Solution {
    fun solution(survey: Array<String>, choices: IntArray): String {
        var answer: String = ""
        var types = arrayOf("R", "T", "F", "C", "M", "J", "A", "N")
        var charMap = mutableMapOf<String, Int>()
        for(t in types){
            charMap[t] = 0
        }
        var N = choices.size
        for(i in 0 until N){
            var surs = survey[i].replace("\"", "")
            var score = choices[i]
            if(score <= 3){
                charMap[surs[0].toString()] = charMap[surs[0].toString()]!! + (4-score)
            }else if(score > 4){
                score -= 4
                charMap[surs[1].toString()] = charMap[surs[1].toString()]!! + (score)
            }            
        }
        for(i in 0 until 8 step 2){
            var ta = types[i]
            var tb = types[i+1]
            if(charMap[ta]!! > charMap[tb]!!){
                answer+= ta
            }else if(charMap[ta]!! < charMap[tb]!!){
                answer+= tb
            }else{
                answer += minOf(ta, tb)
            }
        }
        
        // for(m in charMap){
        //     println(m)
        // }
        return answer
    }
}