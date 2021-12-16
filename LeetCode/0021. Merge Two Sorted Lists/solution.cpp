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

/**
 * 208 / 208 test cases passed.
 * Runtime: 12 ms
 * Memory Usage: 14.6 MB 
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
       ListNode *head = new ListNode(INT_MIN);
       ListNode *curr = head, *l1 = list1, *l2 = list2;
       int next;
       while (l1 && l2) {
            if (l1->val > l2->val) {
                next = l2->val;
                l2 = l2->next;
            }  else {
                next = l1->val;
                l1 = l1->next;
            }
           curr->next = new ListNode(next);
           curr = curr->next;
        } 
        if (!l1 && l2) curr->next = l2;
        if (l1 && !l2) curr->next = l1;
        return head->next;
    }
};
