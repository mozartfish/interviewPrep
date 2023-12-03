class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(len(nums))]

        # prefix pass
        prefix = 1
        for j in range(len(nums)):
            result[j] = prefix 
            prefix *= nums[j]
        # print(f"prefix array: {result}")
        # postfix pass 
        postfix = 1
        for k in range(len(nums)-1, -1, -1):
            result[k] *= postfix
            postfix *= nums[k]
        # print(f"postfix and final result: {result}")

        return result 