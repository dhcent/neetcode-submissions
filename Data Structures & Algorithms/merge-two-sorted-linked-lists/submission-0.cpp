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
/* 
    Intuition is to iterate between each list node via while loops. 
    Start at the smaller of the two. Compare the .next with the current of 
    other list. If ptr2 value is less than ptr1.next, replace ptr1 .next with ptr2
     and then set the new L2 ptr to the previous (via temp references)
*/
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode* ptr1 = list1;
        ListNode* ptr2 = list2;
        ListNode* temp;
        ListNode dummy;
        // sets head via address
        ListNode* head = &dummy;
        // -> eq to dereferencing then accessing. (*var).member
        while(ptr1 != nullptr && ptr2 != nullptr) {
            // add ptrs to head accordingly
            if(ptr1->val < ptr2->val) {
                head->next = ptr1;
                ptr1 = ptr1->next;
            }
            else {
                head->next = ptr2;
                ptr2 = ptr2->next;
            }
            head = head->next;
        }
        head->next = (ptr1 != nullptr) ? ptr1 : ptr2;
        return dummy.next;
    }
};
