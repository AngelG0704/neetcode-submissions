class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */

    getConcatenation(nums) {

        let j = 0;
        const ans = new Array(nums.length * 2);

        for (let i = 0; i < ans.length; i++) {
            if (j > nums.length - 1) {
                j = 0;
            }
            ans[i] = nums[j];
            j++;
        }

        return ans;

    }
}