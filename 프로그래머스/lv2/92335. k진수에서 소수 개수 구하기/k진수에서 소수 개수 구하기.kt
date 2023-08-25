class Solution {
    fun solution(n: Int, k: Int): Int {
        var answer: Int = -1
        var kNum:String = getKnum(n, k)
        answer = getPrimeCnt(kNum)
        return answer
    }
    
    fun getPrimeCnt(knum: String):Int{
        var result = 0
        if(knum.length == 1){
            if(isPrime(knum.toLong())){
                return 1
            }else{
                return 0
            }
        }
        var knums = knum.split("0")
        println(knums)
        for(k in knums){
            if(k!!.length > 0 && isPrime(k.toLong())){
                result++
            }
        }
        return result
    }
    fun getKnum(n: Int, k: Int):String{
        if(k == 10){
            return n.toString()
        }
        var strList = mutableListOf<String>()
        var num = n
        while(num > 0){
            var res = num % k
            strList.add(res.toString())
            num = (num/k)
        }
        return strList.reversed().joinToString("")
    }
    fun isPrime(num: Long): Boolean{
        if(num == 1L){
            return false
        }
        return (2L..Math.sqrt(num.toDouble()).toLong()).none { num % it == 0L}
    }
}