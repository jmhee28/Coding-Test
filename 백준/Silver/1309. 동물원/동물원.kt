class Zoo{
    fun solution(){
        var N = readln().toInt()
        var dp = MutableList(N+1){0L}
        dp[0] = 3L
        dp[1] = 7L
        if(N <= 2){
            println(dp[N-1])
            return
        }

        for(i in 2 until N) {
            dp[i] = (dp[i-2] + 2 * dp[i-1]) % 9901L
        }

        var answer = dp[N-1]
        println(answer)
    }
}

fun main() {
 var zoo = Zoo()
    zoo.solution()
}