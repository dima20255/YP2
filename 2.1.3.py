def dup(nums):
    return len(nums) != len(set(nums))

print(dup([1,2,3,4]))
print(dup([1,1,1,3,3,4,3,2,4,2]))
print(dup([1,2,3,1]))
