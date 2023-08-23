class IpAddress{

    fun solution(){
        var N = readln().toInt()
        var ipAddresses = mutableListOf<Int>()
        for(i in 0 until N){
            var ipAdd = readln()
            ipAddresses.add(ipStrToInt(ipAdd))
        }
        var netMask = getNetMask(ipAddresses, N)
        printIp((ipAddresses[0] and netMask))
        printIp((netMask))

    }

    fun ipStrToInt(ipAdd:String): Int {
        var parsed = ipAdd.split(".")
        var temp = 0
        temp = temp or (parsed[0].toInt() shl 24)
        temp = temp or (parsed[1].toInt() shl 16)
        temp = temp or (parsed[2].toInt() shl 8)
        temp = temp or (parsed[3].toInt())
        return temp
    }

    fun getNetMask(ipAddresses:MutableList<Int>, n: Int): Int {
        var subnet = 0
        for(i in 31 downTo 0){
            var bit = 1 shl i
            var isContinue = true
            for(r in 1 until n){
                if((ipAddresses[0] and bit) != (ipAddresses[r] and bit)){
                    isContinue = false
                    break
                }
            }
            if(!isContinue){
                break
            } else{
                subnet = subnet or bit
            }

        }
        return subnet
    }
    fun printIp(ipAdd: Int){
        var ipStr = Integer.toBinaryString(ipAdd).padStart(32, '0')
        var chunks = ipStr.chunked(8)
        var result = mutableListOf<Int>()
        for(i in 0 until 4){
            var n =Integer.parseInt(chunks[i], 2)
            result.add(n)
        }
        println(result.joinToString("."))
    }
}

fun main(){
    var S = IpAddress()
    S.solution()
}