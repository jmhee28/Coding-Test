class Solution {
    fun solution(number: Int, limit: Int, power: Int): Int {
        var answer: Int = 0
        for(i in 1 until number+1){
            var divisor = countDivisor(i)
            if(divisor > limit){
                divisor = power
            }
            answer += divisor
        }
        return answer
    }
    
    fun countDivisor(n: Int):Int{
        var count = 0
        var i = 1
        while (i * i <= n) {
            if (n % i == 0) {
                count++
                if (i != n / i) {
                    count++ // 중복 제거를 위해 제곱근이 아닌 약수도 세기
                }
            }
            i++
        }
        return count
    }
}