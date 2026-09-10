// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

struct Solution;

use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn ans_count_sum(node: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32, i32) {
        match node {
            Some(node_wrapped) => {
                let node_ref = node_wrapped.borrow();
                let (left_ans, left_count, left_sum) =
                    Solution::ans_count_sum(node_ref.left.clone());
                let (right_ans, right_count, right_sum) =
                    Solution::ans_count_sum(node_ref.right.clone());

                let mut new_ans = left_ans + right_ans;
                let new_count = left_count + right_count + 1;
                let new_sum = left_sum + right_sum + node_ref.val;
                if node_ref.val == new_sum / new_count {
                    new_ans += 1;
                }

                return (new_ans, new_count, new_sum);
            }
            None => (0, 0, 0),
        }
    }

    pub fn average_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Solution::ans_count_sum(root).0
    }
}
