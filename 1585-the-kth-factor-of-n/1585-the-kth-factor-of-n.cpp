class Solution {
public:
    int kthFactor(int n, int k) {
        vector<int>a;
        for(int i=1;i<=n;i++){
            if(n%i==0) a.push_back(i);
        }
        if(k>a.size()) return -1;
        else return a[k-1];
    }
};