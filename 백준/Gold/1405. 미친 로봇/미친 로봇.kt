// 오 왼 아래 위 순
class Robot{
    var dx = arrayOf(0, 0, 1, -1)
    var dy = arrayOf(1, -1, 0, 0)
    lateinit var pDir: DoubleArray
    lateinit var board: MutableList<MutableList<Int>>
    var rc = 31
    var maxN =0
    var answer = 0.0
    fun solution(){
        var (N, e, w, s, n) = readln().split(" ").map{it.toInt()}
        maxN = N
        pDir = arrayOf(e, w, s, n).map{
            it.toDouble() * 0.01
        }.toDoubleArray()
        board = MutableList(rc){ MutableList(rc){0}}
        var x = 15
        var y = 15
        board[x][y] = 1
        bfs(x, y, board, 0, 1.0)
        println(answer)
    }

    fun bfs(x: Int, y: Int, board: MutableList<MutableList<Int>>, cnt:Int, pos: Double) {
        if(cnt >= maxN){
            answer += pos
            return
        }
        for(i in 0 until 4 ){
            var nx = x + dx[i]
            var ny = y + dy[i]
            if(nx in 0 until rc && ny in 0 until rc && pDir[i] > 0.0){
                if(board[nx][ny] == 0){
                    board[nx][ny] = 1
                    bfs(nx, ny, board, cnt+1, pos * pDir[i])
                    board[nx][ny] = 0
                }
            }
        }
    }
}

fun main() {
    var S = Robot()
    S.solution()
}