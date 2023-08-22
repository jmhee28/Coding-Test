class Jingum{
    lateinit var rocks : MutableList<Long>
    var N = 0
    fun solution() {
        N = readln().toInt()
        rocks = readln().split(" ").map{it.toLong()}.toMutableList()
        var dp = MutableList(N){ Long.MAX_VALUE }
        dp[0] = 0
        for(i in 1 until N){
            for(j in 0 until i){
                var p = maxOf(dp[j], power(j, i))
                dp[i] = minOf(dp[i], p)
            }
        }
        println(dp[N-1])
    }

    fun power(from:Int, to: Int): Long {
        return (to - from) * (1 + Math.abs(rocks[from] - rocks[to]))
    }
}
fun main(){
    var S = Jingum()
    S.solution()
}