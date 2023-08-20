import kotlin.system.exitProcess

lateinit var inifriends: MutableList<MutableList<Int>>
lateinit var visited: MutableList<Boolean>
var result = 0
var N = 0
fun main(){
    var (n, m) = readln().split(" ").map {it.toInt()}
    N = n
    var arr = List(n){ it }
    inifriends = MutableList(n){ mutableListOf<Int>() }
    visited = MutableList(n){false}
    for(i in 0 until m){
        var (a, b) = readln().split(" ").map{it.toInt()}
        inifriends[a].add(b)
        inifriends[b].add(a)
    }
    for(i in 0 until n){
        visited[i] = true
        dfs(i, 0)
        visited[i] = false
        if(result == 1){
            break
        }
    }
    println(result)
}

fun dfs(x: Int, count: Int){
    if(count >= 4){
        result = 1
        return
    }
    for(i in inifriends[x]){
        if(!visited[i]){
            visited[i] = true
            dfs(i, count + 1)
            visited[i] = false
        }
    }
}

