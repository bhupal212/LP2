g = {
    0:[1,2],
    1:[0,3,4],
    2:[0,3],
    3:[1,2,4],
    4:[3,1]
}

def dfs(g,s):
    vis[s] = 1
    print(s)
    for c in g[s]:
        if not vis[c]:
            dfs(g,c)


vis = [0]*5

dfs(g,0)