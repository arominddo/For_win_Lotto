!pip install pandas random numpy

# 라이브러리 불러오기
import random as rd
import pandas as pd
import numpy as np


# 이전 당첨번호 불러오기
bf_win_num = pd.read_csv("last_win_num.csv", index_col="#")
win_num_arr = np.array(bf_win_num)

# 가장 최근 당첨 번호
last_win = list(win_num_arr[0])

# 당첨 번호 시뮬레이션 함수 제작
def get_win():
    win = []
    while len(win) <= 5 :
        while True:
            result = rd.randint(1,45)
            print(result)
            if (result not in last_win) & (result not in win):
                break
        win.append(result)
    win.sort()
    return win

# 당첨 번호 시뮬레이션
while True:
    win = get_win()
    t = 0
    for w in range(len(win_num_arr)) :
        if list(win_num_arr[w]) == win :
            break
        t += 1
    if t == len(win_num_arr):
        break

# 당첨 예상 번호 확인
print(win)