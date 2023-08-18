fun main(){
    var (h,m) = readln().split(' ').map{ it.toInt()}
    if(h == 0){
        h = 24
    }
    var absT = h * 60 + m
    var retT = absT - 45
    var retH: Int = retT / 60
    if (retH == 24) {
        retH = 0
    }
    var retM = retT % 60
    println("${retH} ${retM}")
}