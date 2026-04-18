class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        edge_dict = defaultdict(list)

        for i,j in prerequisites:
            edge_dict[i].append(j)


    
        visited = set()
        def dfs(node, path= set()):
            if node in visited:
                # Cycle detected
                return False
            if edge_dict[node] == []:
                return True


            visited.add(node)
            for i in edge_dict[node]:
                if not dfs(i):
                    return False
                
            visited.remove(node)
            edge_dict[node] = []
            return True
                
            

        for i in list(edge_dict):
            if i not in visited and not dfs(i):
                return False 

        return True