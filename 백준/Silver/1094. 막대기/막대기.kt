fun main() {
    val number = readln().toInt() // 출력할 정수 값
    val binaryString = Integer.toBinaryString(number) // 이진수 문자열로 변환
    println(binaryString.count{it == '1'})
}
