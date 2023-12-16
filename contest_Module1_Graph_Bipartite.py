from collections import deque
def bipartite_or_not(graph):
    n = len(graph)
    color = [-1] * n 
    def bfs(start):
        queue = deque([start])
        color[start] = 0  
        while queue:
            current = queue.popleft()

            for neighbor in graph[current]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[current] 
                    queue.append(neighbor)
                elif color[neighbor] == color[current]:
                    return False
        return True
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                return False
    return True
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    neighbors = list(map(int, input().split()))
    graph[i] = neighbors
output = bipartite_or_not(graph)
print(output)