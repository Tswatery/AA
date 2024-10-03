'''
Author: Tswatery
Date: 2024-10-03 18:37:00
'''
import random

n = random.randint(200, 500)
m = random.randint(200, 500)

with open('data.txt', 'w+') as f:
    for i in range(n):
        for j in range(m):
            f.write(str(random.randint(0, 10**5)) + " ")
        f.write('\n')
print(f"data.py 完成")