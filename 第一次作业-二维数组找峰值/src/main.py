'''
Author: Tswatery
Date: 2024-10-03 18:36:52
'''
# 二分解决任意峰值问题
nums = []
with open('data.txt', 'r+') as f:
    lines = f.readlines()

for line in lines:
    nums.append(list(map(int, line.split())))

l, r = 0, len(nums) - 1

while l < r:
    mid = (l + r) // 2
    mx = max(nums[mid])
    if mx < nums[mid + 1][nums[mid].index(mx)]:
        # 下面一行比上面的大
        l = mid + 1
    else:
        r = mid

with open('outmain.txt', 'w+') as f:
    f.write(f"{l} {nums[l].index(max(nums[l]))}")

print("main.py 完成")