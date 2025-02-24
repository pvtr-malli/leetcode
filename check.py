class Solution:
    def isBipartite(self, graph) -> bool:
        n = len(graph)
        visited = [-1] * (n)

        # We are going to color nodes are 0/1.
        # So in visited list, -1 --> not visited. 0/1 is colored.



        for i in range(n):
            if visited[i] == -1:
                q = []
                q.append((i, 0)) # # We will start with color one and have to color adj nodes other color. 0 is the starting color.
                while len(q) != 0:
                    ele = q.pop(0)
                    node, color = ele[0], ele[1]
                    opposite_color = 0 if color == 1 else 1
                    for adj in graph[node]:
                        # Traverse through all the adjecent nodes.
                        # So all the adjecent should have appocite color to the cur parent node color.
                        if visited[adj] == -1:
                            visited[adj] = opposite_color
                            q.append((adj, opposite_color))
                        else:
                            if visited[adj] != opposite_color:
                                return False
        return True

print(Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))