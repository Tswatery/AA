'''
Author: Tswatery
Date: 2024-10-03 19:03:18
'''
import subprocess

with open('check.info', 'w+') as f:
    pass

for i in range(1000):
    subprocess.run(["python3", "data.py"])
    subprocess.run(["python3", "main.py"])
    subprocess.run(["python3", "bf.py"])
    with open('outmain.txt', "r+") as f:
        lines = f.readlines()
    if len(lines) == 0:
        with open('check.info', 'a') as f:
            f.write(f"第{i}轮 没有峰值\n")
            continue
    x1, y1 = list(map(int, lines[0].split()))
    with open('outbf.txt', 'r+') as f:
        lines = f.readlines()
    flag = False
    for line in lines:
        x2, y2 = list(map(int, line.split()))
        if x1 == x2 and y1 == y2:
            with open('check.info', 'a') as f:
                f.write(f"第{i}轮 对比成功\n")
            flag = True
            continue
    if not flag:
        with open('check.info', 'a') as f:
            f.write(f"第{i}轮 对比失败\n")
        break
