class RGB{
    var N = 0
    lateinit var Costs:MutableList<MutableList<Int>>
    val colors = List(3) {
        when (it) {
            0 -> listOf(1, 2)
            1 -> listOf(0, 2)
            2 -> listOf(0, 1)
            else -> throw IllegalArgumentException("Invalid index")
        }
    }
    fun solution(){
        N = readln().toInt()
        Costs = MutableList(N){ mutableListOf() }
        for(i in 0 until N){
            var rgb = readln().split(" ").map{ it.toInt() }
            Costs[i].addAll(rgb)
        }

        var dp = MutableList(N){ MutableList(3) {0} }
        dp[N-1] = Costs[N-1]

        for(i in N-2 downTo 0){
            for(j in 0 until 3){
                // 0 1 2
                // 1 0 2
                // 2 0 1
                dp[i][j] = minOf(dp[i+1][colors[j][0]], dp[i+1][colors[j][1]]) + Costs[i][j]
            }
        }
        var answer = minOf(dp[0][0], dp[0][1], dp[0][2])
        println(answer)
//        for(r in Costs){
//            println(r.joinToString(" "))
//        }

    }

}

fun main(){
    var S = RGB()
    S.solution()
}
