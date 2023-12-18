

// FILEPATH: /home/biggy-admin/Documents/code/datastructures-algos/01-basic-dsa/6trees/binarytree/700_search_bst copy.js
// BEGIN: abpxx6d04wxr
// Definition for a binary tree node.
class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

const node1 = new TreeNode(1);
const node3 = new TreeNode(3);
const node5 = new TreeNode(5);
const node7 = new TreeNode(7);
const node2 = new TreeNode(2, node1, node3);
const node6 = new TreeNode(6, node5, node7);
const root = new TreeNode(4, node2, node6);

// You are given the root of a binary search tree (BST) and an integer val.

// Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
class Solution {
    searchBST(root, val) {
        // Helper method to find the node with the given value
        const findNode = (node, val) => {
            if (node === null || node.val === val) {
                return node;
            } else if (val < node.val) {
                return findNode(node.left, val);
            } else {
                return findNode(node.right, val);
            }
        };

        // Helper method to return the subtree rooted with the given node as an array
        const getSubtree = (node) => {
            if (node === null) {
                return [];
            }
            return [node.val, ...getSubtree(node.left), ...getSubtree(node.right)];
        };

        // Find the node with the given value
        const targetNode = findNode(root, val);

        // Return the subtree rooted with the target node as an array
        return getSubtree(targetNode);
    }
}

// Create an instance of the Solution class
const solution = new Solution();

// Define the value to search for
const targetValue = 2;

// Call the searchBST method and print the result
const result = solution.searchBST(root, targetValue);
console.log(result);
// END: abpxx6d04wxr
