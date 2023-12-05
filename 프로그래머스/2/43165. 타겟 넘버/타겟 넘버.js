let N = 0
let answer = 0;
let T = 0
function solution(numbers, target) {
    N = numbers.length
    T = target
    dfs(numbers,0)
    return answer;
}

const arrSum = (arr) => {
    return arr.reduce((sum, cur)=>{
        return sum + cur
    }, 0)
}

const dfs = (arr, depth) => {
    if (depth == N) {
        if(arrSum(arr) == T){
            answer++
        }
        return
    }
    
   
    dfs(arr, depth + 1)
    newArr = JSON.parse(JSON.stringify(arr))
    newArr[depth] *= -1
    dfs(newArr, depth + 1)    
    
}