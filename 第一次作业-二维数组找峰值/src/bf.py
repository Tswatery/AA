'''
Author: Tswatery
Date: 2024-10-03 18:36:52
'''
# 暴力解法 求所有峰值的坐标

nums = []
with open('data.txt', 'r+') as f:
    lines = f.readlines()

for line in lines:
    nums.append(list(map(int, line.split())))

n, m = len(nums), len(nums[0])

for i in range(n):
    nums[i] = [-1] + nums[i] + [-1]

padding = [-1 for _ in range(m + 2)]
nums.insert(0, padding)
nums.append(padding)

ans = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        t = nums[i][j]
        if t > nums[i - 1][j] and t > nums[i + 1][j] and t > nums[i][j + 1] and t > nums[i][j - 1]:
            # 峰值
            ans.append([i, j])
with open('outbf.txt', 'w+') as f:
    for x, y in ans:
        f.write(f"{x - 1} {y - 1}\n")

print(f"bf.py 完成")
