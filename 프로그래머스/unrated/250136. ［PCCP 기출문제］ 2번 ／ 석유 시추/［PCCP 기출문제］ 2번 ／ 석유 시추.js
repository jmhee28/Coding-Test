let idxSize = {}
let N = 0
let M = 0
function solution(land) {
    var answer = 0;
    N = land.length
    M = land[0].length
    let visited = Array.from({length: N}, () => Array(M).fill(0))
    let idx = 1
    
    for(let i = 0; i < N; i++){
        for(let j = 0; j < M; j++){
            if(visited[i][j] == 0 && land[i][j] == 1){
                bfs(idx, i, j, visited, land)
                idx++
            }
        }
    }
    
    for(let col = 0; col < M; col++){
        let oilIdxSet = new Set()
        let oilSum = 0
        for(let row = 0; row < N; row++){
            let oilIdx = visited[row][col]
            if(oilIdx>0)
                {
                   oilIdxSet.add(oilIdx) 
                }
            
        }
        // console.log(oilIdxSet)
        oilIdxSet.forEach((idx)=> {
            oilSum += idxSize[idx]
        })
        answer = Math.max(answer, oilSum)
    }
    return answer;
}
const dx = [0, 0, 1, -1]
const dy = [1, -1, 0, 0]

const bfs = (idx, x, y, visited, land) => {
    let q = []
    q.push([x, y]) 
    let oilSize = 1
    visited[x][y] = idx
    
    while(q.length > 0){
        [x, y] = q.shift() 
        for(let i = 0; i < 4; i++){
            const nx = x + dx[i]
            const ny = y + dy[i]
            if(validPos(nx, ny) && visited[nx][ny] == 0 && land[nx][ny] == 1){
                visited[nx][ny] = idx
                oilSize++
                q.push([nx, ny]) 
            }
        }
    }
    idxSize[idx] = oilSize
    
}

const validPos = (x, y) => {
    return (x >= 0 && x < N && y >= 0 && y < M)
}
const print = (param) => {
    console.log(param)
}
