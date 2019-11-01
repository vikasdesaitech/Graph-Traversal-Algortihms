

class Bfs:
    def __init__(self, *args, **kwargs):
        self.adjacency_list = kwargs.get('adjacency_list', None)
        self.total_nodes = kwargs.get('total_nodes', 0)


    def shortestPath(self, start, end):
        queue = []
        print('total = ', self.total_nodes)
        visited = [-1] * (self.total_nodes + 1)
        queue.append(start)
        visited[start] = start
        while queue:
            front = queue.pop(0)
            for id in self.adjacency_list[front]:
                if visited[id] == -1:
                    queue.append(id)
                    visited[id] = front
                    if id == end:
                        queue = []
                        break

        path = []
        id = end
        while not id == start:
            path.insert(0, id)
            id = visited[id]
        path.insert(0, start)
        return path


