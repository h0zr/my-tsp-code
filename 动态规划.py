graph = [
    [0, 85, 76, 94, 61, 60],
    [85, 0, 86, 51, 45, 33],
    [76, 86, 0, 43, 64, 47],
    [94, 51, 43, 0, 71, 93],
    [61, 45, 64, 71, 0, 94],
    [60, 33, 47, 93, 94, 0],
]


def tsp(graph):
    n = len(graph)
    # dp数组，dp[i][j]表示从城市0到城市i，经过已选择的城市集合j的最短路径长度
    dp = [[float('inf')] * (1 << n) for _ in range(n)]

    for i in range(n):  # 初始化dp数组
        dp[i][1 << i] = graph[0][i]

    # 动态规划转移方程
    for j in range(1, 1 << n):
        for i in range(n):
            if (j >> i) & 1:  # 如果城市i在集合j中
                continue
            for k in range(n):
                if (j >> k) & 1:  # 如果城市k在集合j中
                    dp[i][j | (1 << i)] = min(dp[i][j | (1 << i)], dp[k][j] + graph[k][i])
    min_path = min(dp[i][(1 << n) - 1] + graph[i][0] for i in range(1, n))

    # 构造最短路径
    last_city, state = min(enumerate(dp[i][(1 << n) - 1] + graph[i][0] for i in range(1, n)), key=lambda x: x[1])
    path = [0, last_city]
    mask = (1 << last_city) | 1
    while mask != (1 << n) - 1:
        current_city = min(i for i in range(1, n) if not (mask >> i) & 1)
        path.append(current_city)
        mask |= 1 << current_city
    path.append(0)  # 回到起点
    return min_path, path


if __name__ == '__main__':
    res_cost, res_path = tsp(graph)
    print("基于动态规划的最短路径：", " -> ".join(map(str, res_path)))
    print("基于动态规划的最短距离：", res_cost)
