class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_fix = 1
        post_fix = 1
        #pre_product = [1] * len(nums)
        #post_product = [1] * len(nums)
        result = [1] * len(nums)#[1 , 1 , 1 , 1]
        for i in range(len(nums)):
            result[i] = pre_fix
            pre_fix *= nums[i] 
        #result = [1,1,2,6]

        for i in range(len(nums)-1 , -1 , -1):# this one will start from 3
            result[i] *= post_fix # result[0] = 24 * 1 = 24
            post_fix *= nums[i]# post = 4 * nums[2] = 4 * 3 = 24

        return result
            
            