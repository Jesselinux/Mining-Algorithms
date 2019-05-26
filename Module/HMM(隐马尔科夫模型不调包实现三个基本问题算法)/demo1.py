# --encoding:utf-8 --
"""课堂上实现一下这个前向的算法"""

import numpy as np


def calc_alpha(pi, A, B, Q, alpha):
    """
    计算前向概率alpha，最终结果保存alpha中
    pi: 初始状态选择概率
    A: 状态转移矩阵
    B：状态和观测值之间的转移矩阵
    Q：观测序列对应的下标组成的向量
    """
    # 状态数量
    n = len(A)
    n_range = range(n)

    #  1. 初始化t=1时候的前向概率值
    for i in n_range:
        alpha[0][i] = pi[i] * B[i][Q[0]]

    # 2. 更新其它时刻的前向概率值
    T = len(Q)
    tmp = np.zeros(n)
    for t in range(1, T):
        for i in n_range:
            # 当前状态为i
            # a. 计算上一个时刻t-1累积过来的概率值
            for j in n_range:
                # 上一个时刻的状态为j
                tmp[j] = alpha[t - 1][j] * A[j][i]

            # b. 更新时刻t的时候处于状态i的前向概率的值
            alpha[t][i] = np.sum(tmp) * B[i][Q[t]]


if __name__ == '__main__':
    # 测试
    pi = np.array([0.2, 0.5, 0.3])
    A = np.array([
        [0.5, 0.4, 0.1],
        [0.2, 0.2, 0.6],
        [0.2, 0.5, 0.3]
    ])
    B = np.array([
        [0.4, 0.6],
        [0.8, 0.2],
        [0.5, 0.5]
    ])
    Q = [0, 1, 0, 0, 1]
    alpha = np.zeros((len(Q), len(A)))
    # 开始计算
    calc_alpha(pi, A, B, Q, alpha)
    # 输出最终结果
    print(alpha)

    # 计算最终概率值：
    p = 0
    for i in alpha[-1]:
        p += i
    print(Q, end="->出现的概率为:")
    print(p)
