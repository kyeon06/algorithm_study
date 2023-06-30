# DFS : 깊이 우선 탐색
- 스택 or 재귀를 사용해서 구현

```python
adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
# ...


def dfs(now):
    for nxt in range(13):
        if adj[now][nxt]:
            dfs(nxt)

dfs(0)
```