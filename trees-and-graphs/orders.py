from collections import defaultdict,deque

def find_build_order(projects, dependencies):
    graph = defaultdict(list)
    indegree = {project: 0 for project in projects}
    print(type(graph))
    print(type(indegree))

    # Build the graph and in-degree table
    for first,second in dependencies:
        graph[first].append(second)
        indegree[second] +=1 
    
    
    # Add all projects with no dependencies
    queue = deque()
    for project in projects:
        if indegree[project] == 0:
            queue.append(project)
    
    build_order = []

    while queue:
        project = queue.popleft()
        build_order.append(project)

        # Reduce dependencies count for children
        for neighbour in graph[project]:
            indegree[neighbour] -=1

            if indegree[neighbour] ==0:
                queue.append(neighbour)

    # If build_order does not contain all projects, there is a cycle
    if len(build_order) != len(projects):
        raise Exception("No valid build order exists")
    
    return build_order

projects = ["a", "b", "c", "d", "e", "f"]

dependencies = [
    ("a", "d"),
    ("f", "b"),
    ("b", "d"),
    ("f", "a"),
    ("d", "c")
]

print(find_build_order(projects, dependencies))