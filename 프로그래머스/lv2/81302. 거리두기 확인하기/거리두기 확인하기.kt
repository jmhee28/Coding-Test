import kotlin.collections.ArrayDeque

class Solution {
    var dx = arrayOf(1, -1, 0, 0)
    var dy = arrayOf(0, 0, 1, -1)
    var T = 5
    var rc = 5
    fun solution(places: Array<Array<String>>): IntArray {
        var answer = mutableListOf<Int>()
        var t = 0
        for(place in places){
            // println(t++)
            var pLocs = mutableListOf<Pair<Int, Int>>()

            for(i in 0 until rc){
                for(j in 0 until rc){
                    if(place[i][j] == 'P'){
                        pLocs.add(Pair(i, j))
                    }
                }
            }
            var flag = true
            for(pLoc in pLocs){
                var visited = MutableList(rc){ MutableList(rc){-1}}
                visited[pLoc.first][pLoc.second] = 0
                flag = bfs(pLoc, visited, place)
                if(!flag){
                    
                    // println(pLoc)
                    // for(v in visited){
                    //     println(v)
                    // }
                    //  println()
                    break
                }
            }
            if(flag){
                answer.add(1)
            }else{
                answer.add(0)
            }
        }
        
        
        return answer.toIntArray()
    }
    
    fun bfs(p:Pair<Int, Int>,  visited: MutableList<MutableList<Int>>, board: Array<String>):Boolean{
        var queue = ArrayDeque<Pair<Int, Int>>()
        queue.add(p)
        while(queue.isNotEmpty()){
            var (x, y) = queue.removeFirst()
            for(i in 0 until 4){
                var nx = x + dx[i]
                var ny = y + dy[i]
                if(nx < 0 || nx >= rc || ny < 0 || ny >= rc || visited[nx][ny] >= 0 || board[nx][ny] == 'X'){
                    continue
                }
                
                visited[nx][ny] = visited[x][y] + 1
                if( board[nx][ny] == 'P' && visited[nx][ny] <= 2){
                    // println("$nx , $ny")
                    // println(visited[nx][ny])
                      return false
                    }
                queue.add(Pair(nx, ny))
            }
        }
        
        return true
    }
}