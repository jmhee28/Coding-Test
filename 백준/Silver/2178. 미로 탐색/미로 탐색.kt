import kotlin.collections.ArrayDeque

val dx = arrayOf(-1,1, 0,0)
val dy = arrayOf(0, 0, -1, 1)
var N = 0
var M = 0
fun main() {
    val (n, m) = readLine()!!.split(" ").map { it.toInt() }
    N = n
    M = m
    val maze = Array(n) {
        readLine()!!.map { it - '0' }.toIntArray()
    }

    println(bfs(0,0, maze))
}
fun bfs(x:Int, y:Int, maze: Array<IntArray>): Int{
    var queue = ArrayDeque<Pair<Int, Int>>()
    queue.add(Pair(x, y))

    while(queue.isNotEmpty()){
        var (x, y) = queue.removeFirst()
        for(d in 0 until 4){
            val nx = x + dx[d]
            val ny = y + dy[d]
            if(nx in 0 until N && ny in 0 until M && maze[nx][ny] == 1){
                maze[nx][ny] = maze[x][y] + 1
                queue.add(Pair(nx, ny))
            }
        }
    }
    return maze[N-1][M-1]
}
