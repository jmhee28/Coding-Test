fun main(){
    var t = readln().toInt()
    for(i in 0 until t ) {
        println(String.format("%.3f",classScore()).plus("%"))
    }
}

fun classScore(): Float{
    var arr = ArrayList<Float>()
    var cnt = 0
    readLine()?.split(' ')?.mapIndexed { index, element ->
        if(index ==0){
            cnt = element.toInt()
        } else{
            arr.add(element.toFloat())
        }
    }
    var mean = arr.sum() / cnt.toFloat()
    var exceed = 0
    for(e in arr){
        if(e > mean){
            exceed++
        }
    }
    return (exceed / cnt.toFloat()) * 100
}