#include <set>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        std::set<ListNode*> visited;
        while(head != nullptr) {
            if(visited.contains(head)) {
                return true;
            }
            visited.insert(head);
            head = head->next;
        }
        return false;
    }
};
