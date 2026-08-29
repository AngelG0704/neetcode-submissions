class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let map = {};

        for(let s in nums){
            const val = nums[s];
            if (val in map){
                return true;
            }
            map[val] = true;
        }
        return false;

    }
}
