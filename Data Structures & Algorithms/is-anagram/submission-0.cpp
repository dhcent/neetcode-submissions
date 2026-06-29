#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> aCharFreq;
        unordered_map<char, int> bCharFreq;

        for(char c: s) {
            if(aCharFreq.contains(c)) {
                aCharFreq[c] += 1;
            }
            else {
                aCharFreq[c] = 0;
            }
        }
        for(char c: t) {
            if(bCharFreq.contains(c)) {
                bCharFreq[c] += 1;
            }
            else {
                bCharFreq[c] = 0;
            }
        }

        return aCharFreq == bCharFreq;
    }
};
