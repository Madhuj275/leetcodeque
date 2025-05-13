class Solution {
public:
    unordered_map<string, bool> memo;

    bool solve(string s1, string s2) {
        string key = s1 + " " + s2;
        if (s1 == s2) return memo[key] = true;
        if (s1.size() <= 1 || s2.size() <= 1) return false;
        if (memo.find(key) != memo.end()) return memo[key];

        int n = s2.size();
        bool isScrambled = false;
        for (int i = 1; i < s1.size(); i++) {
            bool cond1 = solve(s1.substr(0, i), s2.substr(n - i)) && solve(s1.substr(i), s2.substr(0, n - i));
            bool cond2 = solve(s1.substr(0, i), s2.substr(0, i)) && solve(s1.substr(i), s2.substr(i));
            if (cond1 || cond2) {
                isScrambled = true;
                break;
            }
        }
        return memo[key] = isScrambled;
    }

    bool isScramble(string s1, string s2) {
        vector<int> freq(26, 0);
        for (int i = 0; i < s1.size(); i++) {
            freq[s1[i] - 'a']++;
            freq[s2[i] - 'a']--;
        }
        for (int count : freq) {
            if (count != 0) return false;
        }
        return solve(s1, s2);
    }
};