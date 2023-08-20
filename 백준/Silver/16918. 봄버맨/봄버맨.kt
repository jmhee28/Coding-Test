var R = 0
var C = 0
var Ns = 0
var curSec = 0
var dx = arrayOf(1, -1, 0, 0)
var dy = arrayOf(0, 0, 1, -1)

lateinit var board:List<MutableList<Int>>

fun main(){
    var (r, c, n) = readln().split(" ").map{it-> it.toInt()}
    R = r
    C = c
    Ns = n
    if(Ns < 2){
        var xboard = List(r){
            readln()
        }
        for(row in xboard){
            println(row)
        }
        return
    }

    board = List(r){
        readLine()!!.map { if (it == 'O') 1 else -1 }.toMutableList()
    }
    Ns -= 1
    for(i in 0 until Ns){
        if(i % 2 == 0){
            installBomb()
        }else{
            explodeBomb()
        }
    }
    print2D(board)
}
fun installBomb() {
    board.forEach { row ->
        row.forEachIndexed { index, _ ->
            row[index]++
        }
    }
}
fun explodeBomb(){
    for(i in 0 until R){
        for(j in 0 until C){
            if(board[i][j]  == 2){
                for(d in 0 until 4){
                    var nx = i + dx[d]
                    var ny = j + dy[d]
                    if(nx in 0 until R && ny in 0 until C ){
                        when {
                            board[nx][ny] < 2 -> board[nx][ny] = -1
                        }
                    }
                    board[i][j] = -1
                }
            } else if (board[i][j] > -1){
                board[i][j]++
            }
        }
    }
}
fun print2D(arr: List<MutableList<Int>>){
    for(row in arr){
        var rowString = row.joinToString("") {if(it > -1) "O" else "."}
        println(rowString)
    }
}