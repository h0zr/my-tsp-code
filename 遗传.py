import random
from copy import deepcopy
from itertools import pairwise


graph = [
    [0, 85, 76, 94, 61, 60],
    [85, 0, 86, 51, 45, 33],
    [76, 86, 0, 43, 64, 47],
    [94, 51, 43, 0, 71, 93],
    [61, 45, 64, 71, 0, 94],
    [60, 33, 47, 93, 94, 0],
]
# GA相关参数
individual_num = 30  # 个体数量
gen_num = 200  # 迭代次数
cross_prob = 0.8  # 交叉概率
mutate_prob = 0.1  # 突变概率

individual_list = []  # 记录种群的个体


def init():  # 初始化族群
    for _ in range(individual_num):
        genes = list(range(cities_num))
        random.shuffle(genes)
        individual_list.append(genes)


def calc_fitness(genes):  # 计算适应度
    fitness = 0
    for i, j in pairwise(genes):
        fitness += graph[i][j]
    fitness += graph[genes[-1]][genes[0]]
    return fitness


def select():
    group_num = 6
    group_size = 10
    winners_num = individual_num // group_num
    winners = []
    for i in range(group_num):
        group = random.sample(individual_list, group_size)  # 随机抽样
        winners.extend(sorted(group, key=calc_fitness)[:winners_num])
    return winners


def cross(p1, p2):
    if random.random() >= cross_prob:  # 未发生
        return None, None
    idx1 = random.randint(0, cities_num - 2)  # 两个随机点
    idx2 = random.randint(idx1 + 1, cities_num - 1)

    def gen_child(g1, g2):
        child = [None] * cities_num
        selected = set()
        child[idx1:idx2] = g1[idx1:idx2]
        selected.update(child[idx1:idx2])
        unselected = [x for x in g2 if x not in selected]
        idx = 0
        for i in range(cities_num):
            if idx1 <= i < idx2:
                continue
            child[i] = unselected[idx]
            idx += 1
        return child

    return gen_child(p1, p2), gen_child(p2, p1)


def mutate(p):
    if random.random() >= mutate_prob:  # 使用翻转切片的方法产生变异
        return None
    idx1 = random.randint(0, cities_num - 2)  # 两个随机点
    idx2 = random.randint(idx1 + 1, cities_num - 1)
    p[idx1:idx2] = reversed(p[idx1:idx2])
    return p


def ga():
    global individual_list
    # 交叉
    new_genes = []
    random.shuffle(individual_list)  # 打乱个体排序
    for i in range(0, individual_num, 2):
        p1, p2 = deepcopy(individual_list[i]), deepcopy(individual_list[i + 1])
        c1, c2 = cross(p1, p2)
        if c1 is not None and c2 is not None:
            new_genes.extend([c1, c2])

    # 变异
    for g in new_genes:
        mut_gene = mutate(deepcopy(g))
        if mut_gene is not None:
            individual_list.append(mut_gene)

    # 选择
    individual_list += new_genes
    individual_list = select()


if __name__ == '__main__':
    cities_num = len(graph)
    init()
    best = individual_list[0]  # 每一代的最佳个体

    for _ in range(gen_num):
        ga()
        if calc_fitness(individual_list[0]) < calc_fitness(best):
            best = individual_list[0]
        best = max(best, individual_list[0], key=calc_fitness)

    best.append(best[0])
    print("基于遗传的最短路径：", " -> ".join(map(str, best)))
    print("基于遗传的最短距离：", calc_fitness(best))
