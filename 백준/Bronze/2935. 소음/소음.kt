fun main() {
    var arr = ArrayList<String>()
    for(i in 0 until 3){
        arr.add(readln())
    }
    var oper1 = arr[0].toBigInteger()
    var oper2 = arr[2].toBigInteger()
    if(arr[1] == "+"){
        println(oper1 + oper2)
    }else{
        println(oper1 * oper2)
    }
}