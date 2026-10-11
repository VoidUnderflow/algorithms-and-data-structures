struct Solution;

impl Solution {
    pub fn sum_of_squares(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut ans = 0;

        for idx in 0..n {
            if n % (idx + 1) == 0 {
                ans += nums[idx as usize].pow(2);
            }
        }
        ans
    }
}

pub fn main() {
    assert_eq!(Solution::sum_of_squares(vec![1, 2, 3, 4]), 21);
    assert_eq!(Solution::sum_of_squares(vec![2, 7, 1, 19, 18, 3]), 63);
}
