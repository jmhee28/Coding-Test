#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>

using namespace std;

bool isBinaryTree(string binary);
bool isZeroTree(string binary);
string getFullBinary(string binary);

string getFullBinary(string binary) {
    int length = binary.length();
    int nodeCount = 1;
    int level = 1;
    while(length > nodeCount){
        level *= 2;
        nodeCount += level;
    }
    int offset = nodeCount - length;
    return string(offset, '0') + binary;
}

bool isBinaryTree(string binary){
    if(binary.empty()) return true;
    int len = binary.length();
    int root = len / 2;
    string leftSubTree = binary.substr(0, root);
    string rightSubTree = binary.substr(root+1);
    if (binary[root] == '0'){
        return isZeroTree(leftSubTree) && isZeroTree(rightSubTree);
    }
    return isBinaryTree(leftSubTree) && isBinaryTree(rightSubTree); 
}

bool isZeroTree(string binary){
    if(binary.empty()) return true;

    int len = binary.length();
    int root = len / 2;
    if (binary[root] == '1'){
        return false;
    }
    string leftSubTree = binary.substr(0, root);
    string rightSubTree = binary.substr(root+1);

    return isZeroTree(leftSubTree) && isZeroTree(rightSubTree);

}
vector<int> solution(vector<long long> numbers) {
    vector<int> answer;
    for(int i = 0; i < numbers.size(); i++){
        string binary = bitset<64>(numbers[i]).to_string();
        binary = binary.substr(binary.find('1'));
        string fullBinary = getFullBinary(binary);
        if(isBinaryTree(fullBinary)){
            answer.push_back(1);
        }else{
            answer.push_back(0);
        }
    }
    return answer;
}

// int main(){
//     solution({7, 42, 5});
//     return 0;
// }