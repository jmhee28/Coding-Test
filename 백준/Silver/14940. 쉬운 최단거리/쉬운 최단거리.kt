import kotlin.collections.ArrayDeque

fun main(){
    var (n, m) = readln().split(" ").map{it.toInt()}
    lateinit var target:Pair<Int, Int>
    var dist = List(n){ MutableList(m){ -1 } }

    var board = List(n){rowIndex->
        readLine()!!.split(" ").mapIndexed{ colIndex, it->
            var num = it.toInt()
            if(num == 2 ){
                target = Pair(rowIndex, colIndex)
            }else if(num == 0){
                dist[rowIndex][colIndex] = -2
            }
            num
        }.toMutableList()
    }

    val dx = arrayOf(1, -1, 0, 0)
    val dy = arrayOf(0, 0, 1, -1)

    var q = ArrayDeque<Pair<Int,Int>>()
    q.add(target)
    var (x, y) = target
    dist[x][y] = 0

    while(q.isNotEmpty()){
       var ( x, y ) = q.removeFirst()
        for(i in 0 until 4){
            var nx = x + dx[i]
            var ny = y + dy[i]
            if(nx in 0 until n && ny in 0 until m && dist[nx][ny] == -1) {
                if(board[nx][ny] == 1 ){
                    dist[nx][ny] = dist[x][y] + 1
                    q.add(Pair(nx, ny))
                }
            }
        }
    }

    dist.forEachIndexed{rindex, row ->
        row.mapIndexed{cindex, c->
            if(c == -2){
                dist[rindex][cindex] = 0
            }
        }
        println(row.joinToString(" "))
    }
}