nums = [int(s) for s in open('./17_17558.txt')]  # шаг 1

cnt32 = 0  # шаг 2
for num in nums:
    if abs(num)%32 == 0:
        cnt32 += 1

pairs = []  # шаг 3
for i in range(len(nums)-1):
    if ((nums[i]<0) or (nums[i+1]<0)) and (nums[i]+nums[i+1] < cnt32):
        pairs.append(nums[i] + nums[i+1])

print(len(pairs), max(pairs))
