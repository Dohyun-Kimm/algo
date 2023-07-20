def solution(park, routes):
    answer = []
    # Park string to list
    graph = []
    height = len(park)
    width = len(park[0])
    for p in park:
        graph.append(list(p))

    # Start Point
    start = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start = [i, j]
    # Move
    for route in routes:
        way, distance = route.split(' ')
        distance = int(distance)
        if way == 'E':
            if start[1] + distance < width and 'X' not in graph[start[0]][start[1]:start[1] + distance + 1]:
                start[1] = start[1] + distance
        elif way == 'W':
            if start[1] - distance >= 0 and 'X' not in graph[start[0]][start[1] - distance:start[1] + 1]:
                start[1] = start[1] - distance
        elif way == 'S':
            if start[0] + distance < height:
                for r in range(start[0], start[0] + distance + 1):
                    if graph[r][start[1]] == 'X':
                        break
                else:
                    start[0] = start[0] + distance
        elif way == 'N':
            if start[0] - distance >= 0:
                for r in range(start[0] - distance, start[0] + 1):
                    if graph[r][start[1]] == 'X':
                        break
                else:
                    start[0] = start[0] - distance

    return start