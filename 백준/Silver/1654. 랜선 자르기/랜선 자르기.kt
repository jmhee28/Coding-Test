class Lan{
    var N = 0L
    var K = 0L
    lateinit var lans: MutableList<Long>

    fun solution(){
        var (k, n) = readln().split(" ").map{ it.toLong() }
        N = n
        K = k
        lans = mutableListOf()
        var maxLan = 0L
        for(i in 0 until K) {
            var num = readln().toLong()
            maxLan = maxOf(maxLan, num)
            lans.add(num)
        }

        var start = 1L
        var end = maxLan + 1
        var answer = 0L

        while(start <= end){
            var mid = ((start + end) / 2)
            var slicedLan = lanSlice(mid)
            if (slicedLan >= N){
                answer = maxOf(mid, answer)
                start = mid + 1
            } else {
                end = mid - 1
            }
        }
        println(answer)
    }

    fun lanSlice(div: Long): Long {
        var result = 0L

        lans.forEach{it->
            result += (it/div)
        }
        return result
    }
}

fun main(){
    var S = Lan()
    S.solution()
}