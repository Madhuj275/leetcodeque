# Problem:   Count Symmetric Integers
# Difficulty: Unknown
# Solution:

class Solution {
public:
    int countSymmetricIntegers(int low, int high) {
        int count = 0;
        for (int i = low; i <= high; i++) {
            string num = to_string(i);
            if (num.size() % 2 == 0) {
                int half = num.size() / 2;
                int leftSum = 0;
                int rightSum = 0;

                for (int i = 0; i < half; i++) {
                    leftSum += num[i] - '0';
                }

                for (int i = half; i < num.size(); i++) {
                    rightSum += num[i] - '0';
                }

                if (leftSum == rightSum)
                    count++;
            }
        }
        return count;
    }
};