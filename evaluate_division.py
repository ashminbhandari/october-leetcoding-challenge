class Solution(object):
    def calcEquation(self, equations, values, queries):
        #check if already exist, if not create and insert
        def putInAdjList(adjList, key, value):
            if key in adjList:
                adjList[key].append(value)
            else: adjList[key] = [value]

        #create adjList
        adjList = {}
        for i in range(len(equations)):
            putInAdjList(adjList, equations[i][0], (equations[i][1], values[i]))
            putInAdjList(adjList, equations[i][1], (equations[i][0], 1/float(values[i])))

        #dfs
        visited = set()
        def dfs(adjList, src, dest):
            if (src not in adjList or dest not in adjList): return -1.0
            visited.add(src)
            if (src == dest):
                return 1.0
            if (src in adjList):
                adjs = adjList[src]
                for i in range(len(adjs)):
                    nxtNode = adjs[i][0]
                    weight = adjs[i][1]
                    if nxtNode not in visited:
                        pthAns = dfs(adjList, nxtNode, dest)
                        if pthAns != -1.0: return weight * pthAns
            return -1.0

        divs = []

        for i in range(len(queries)):
            divs.append(dfs(adjList, queries[i][0], queries[i][1]))
            visited = set()

        return divs

