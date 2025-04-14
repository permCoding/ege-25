nums = [int(s) for s in open('./17_17558.txt')]  # шаг 1

cnt32 = len([num for num in nums if abs(num)%32 == 0])  # шаг 2

pairs = []  # шаг 3
for i in range(len(nums)-1):
    u1 = (nums[i]<0) or (nums[i+1]<0)
    u2 = nums[i]+nums[i+1] < cnt32
    if u1 and u2:
        pairs += [nums[i] + nums[i+1]]

print(len(pairs), max(pairs))
