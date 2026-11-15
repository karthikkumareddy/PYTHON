nums = [1,0,2,0,12]
left = 0
for right in range(0,len(nums)):
    if nums[right] != 0:
        nums[left],nums[right] = nums[right],nums[left]
        left = left +1
print(nums)
        