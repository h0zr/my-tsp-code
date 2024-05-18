from math import inf

graph = [
    [0, 85, 76, 94, 61, 60],
    [85, 0, 86, 51, 45, 33],
    [76, 86, 0, 43, 64, 47],
    [94, 51, 43, 0, 71, 93],
    [61, 45, 64, 71, 0, 94],
    [60, 33, 47, 93, 94, 0],
]


def tsp(start_city: int):
    # 最近邻居法，start表示起始城市
    unvisited = set([i for i in range(cities_num) if i != start_city])  # 未访问的
    cost = 0
    path = [start_city]
    cur_city = start_city

    while unvisited:  # 找到最近的且未被访问的城市，并访问之
        nearest_city = min(unvisited, key=lambda x: graph[cur_city][x])
        path.append(nearest_city)
        unvisited.remove(nearest_city)
        cost += graph[cur_city][nearest_city]
        cur_city = nearest_city

    path.append(start_city)  # 返回起始点
    cost += graph[cur_city][start_city]

    return path, cost


if __name__ == '__main__':
    cities_num = len(graph)
    res_cost = inf
    res_path = []  # 结果
    for start in range(cities_num):
        best_path, best_cost = tsp(start)
        if res_cost > best_cost:
            res_cost = best_cost
            res_path = best_path

    print("基于贪心的最短路径：", " -> ".join(map(str, res_path)))
    print("基于贪心的最短距离：", res_cost)
