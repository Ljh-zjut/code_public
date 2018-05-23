#! usr/bin.env pytho3
#-*- coding: utf-8 -*-
def twoSum(nums, target):
    for i in range(len(nums)):
        j = target - nums[0]
        del nums[0]
        if j in nums:
            return(i, nums.index(j)+1+i)

a = [3,3]
b = 6
print(a.extend(a))