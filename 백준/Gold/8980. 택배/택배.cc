#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);
    int ans=0;
    int n, capacity;
    cin >> n >> capacity;
    int m;
    cin >> m;
    vector<tuple<int, int, int>> infos; //sender, reciever, box
    vector<int> truck(n);
    for(int i = 0; i < m; i++){
        int sender, reciever, box;
        cin >> sender >> reciever >> box;
        infos.emplace_back(sender, reciever, box);
    }
    
    sort(infos.begin(), infos.end(), [](const auto& a, const auto& b)
    {
        return get<1>(a) < get<1>(b);
    });
    int size = infos.size();
    for(int i = 0; i < size; i++){
        int sender = get<0>(infos[i]);
        int reciever = get<1>(infos[i]);
        int box = get<2>(infos[i]);
        int temp = 0;
        int cnt = 0;
        for(int j = sender; j < reciever; j++){
            temp = max(temp, truck[j]);
        }
        if(temp + box <= capacity) cnt = box;
        else cnt = capacity - temp;

        for(int j = sender; j < reciever; j++){
            truck[j] += cnt;
        }
        ans += cnt;
    }
    cout << ans;
    // for(auto t : infos){
    //     cout << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << '\n';
    // }
    
    

}