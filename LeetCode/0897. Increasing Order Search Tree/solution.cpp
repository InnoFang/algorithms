/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

/**
 * 37 / 37 test cases passed.
 * Runtime: 4 ms
 * Memory Usage: 7.7 MB 
 */
class Solution {
public:
    void inorder(TreeNode* root, vector<int>& ans) {
        if (!root) return;
        inorder(root->left, ans);
        ans.push_back(root->val);
        inorder(root->right, ans);
    }
    TreeNode* increasingBST(TreeNode* root) {
        vector<int> ans;
        inorder(root, ans);

        TreeNode* dummyNode = new TreeNode();
        TreeNode* dummy = dummyNode;
        for (auto& val: ans) {
            TreeNode* node = new TreeNode(val);
            dummy->right = node;
            dummy = dummy->right;
        }
        return dummyNode->right;
    }
};
