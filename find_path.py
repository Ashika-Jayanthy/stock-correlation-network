def find_path(graph, start, end, path=[]):
        path.append(start)

        if start == end:
            return path
        if start not in graph.keys():
            return path


        if graph[start] not in path:
            new_start = graph[start]
            path_update = find_path(graph, new_start, end, path)

        return path
