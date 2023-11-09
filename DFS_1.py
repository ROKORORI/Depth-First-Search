import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(now_node):
    global cnt
    visit[now_node] = 0
    out[now_node] = cnt
    for node in nodes[now_node]:
        if visit[node] == 1:
            cnt += 1
            dfs(node)


n, m, r = map(int, input().rstrip().split())
visit, out = [1] * (n + 1), [0] * (n + 1)
nodes, cnt = [[] for i in range(n + 1)], 1

for i in range(m):
    a, b = map(int, input().rstrip().split())
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(n):
    nodes[i].sort()

dfs(r)
print(*out[1:], sep="\n")
