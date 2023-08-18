var hmap = HashMap<String, Float>()
fun makeGrade() {
    var pm = arrayOf('+', '0', '-')
    var sc = 4.3F
    for (i in 0 until 3){
        var str = 'A'.plus(pm[i].toString())
        hmap.put(str, sc)
        sc -= 0.3F
    }
    sc = 3.3F
    for (i in 0 until 3){
        var str = 'B'.plus(pm[i].toString())
        hmap.put(str, sc)
        sc -= 0.3F
    }
    sc = 2.3F
    for (i in 0 until 3){
        var str = 'C'.plus(pm[i].toString())
        hmap.put(str, sc)
        sc -= 0.3F
    }
    sc = 1.3F
    for (i in 0 until 3){
        var str = 'D'.plus(pm[i].toString())
        hmap.put(str, sc)
        sc -= 0.3F
    }
    hmap.put("F", 0.0F)
}
fun main() {
    var score = readln()
    makeGrade()
    println(String.format("%.1f", hmap.get(score)))
}
