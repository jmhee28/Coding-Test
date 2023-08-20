lateinit var computers:List<MutableList<Int>>

fun main(){
    var n = readln().toInt()
    var t = readln().toInt()
    computers = List(n+1){ mutableListOf<Int>() }
    for(i in 0 until t){
        var (a, b) = readln().split(" ").map{it.toInt()}
        computers[a].add(b)
        computers[b].add(a)
    }
    var visited = MutableList(n+1){false}
    var answer = 0
    dfs(1, visited)
    visited.forEach{it->
        if(it){
            answer++
        }
    }
    println(answer-1)
}

fun dfs(v:Int, visited:MutableList<Boolean>) {
    visited[v] = true
    for(i in computers[v]){
        if(!visited[i]){
            dfs(i, visited)
        }
    }
}