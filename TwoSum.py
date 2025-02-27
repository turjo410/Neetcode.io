def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in len(nums):
        for j in len(nums):
            if(nums[i] + nums[j] == target and i != j):
                return [i,j]


nums = [3,4,5,6], target = 7
twoSum(nums,target)


        