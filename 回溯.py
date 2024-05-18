from math import inf
from itertools import pairwise

graph = [
    [0, 85, 76, 94, 61, 60],
    [85, 0, 86, 51, 45, 33],
    [76, 86, 0, 43, 64, 47],
    [94, 51, 43, 0, 71, 93],
    [61, 45, 64, 71, 0, 94],
    [60, 33, 47, 93, 94, 0],
]


def calc_cost(p):
    # 计算某条路径的代价
    cost = 0
    for x, y in pairwise(p):
        cost += graph[x][y]
    cost += graph[p[0]][p[-1]]
    return cost


def tsp():
    path = [0] * cities_num
    res = []
    min_cost = inf

    def backtrace(start: int, unvisited: set):
        if start == cities_num:
            cost = calc_cost(path)
            nonlocal min_cost, res
            if cost < min_cost:  # 更新最短路径
                min_cost = cost
                res = path.copy()
            return

        for city in unvisited:
            path[start] = city
            backtrace(start + 1, unvisited - {city})

    backtrace(0, set(list(range(cities_num))))
    return res, min_cost


if __name__ == '__main__':
    cities_num = len(graph)
    res_path, res_cost = tsp()

    res_path.append(res_path[0])
    print("基于回溯的最短路径：", " -> ".join(map(str, res_path)))
    print("基于回溯的最短距离：", res_cost)
