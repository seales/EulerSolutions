def initialize(file_p):
    arr = []
    for line in file_p:
        line = line.split()
        for num in range(len(line)):
            line[num] = int(line[num])
        arr.append(line)
    return arr

f = open("bigtriangle.txt")
triangle_numbers = initialize(f)


def max_route(triangle):

    # NOTE: paths are stored in a [sum of path, current position, path_id] format

    i, path_id, paths = 0, 0, []
    while i < len(triangle[-1])-1:
        if triangle[-1][i] > triangle[-1][i+1]:
            paths.append([triangle[-1][i], i, path_id])
        else:
            paths.append([triangle[-1][i+1], i+1, path_id])
        path_id += 1
        i += 2

    i = len(triangle) - 2  # -1 for row already analyzed, -1 for 0-index
    while i > -1:
        for j in range(len(paths)):
            if paths[j][1] - 1 >= 0 and paths[j][1] <= len(triangle[i]) - 1:
                # initially, brute force; try both paths
                
                # take same position
                paths.append([triangle[i][paths[j][1]]+paths[j][0], paths[j][1], path_id])
                path_id += 1
                
                # take position-1
                paths[j][0] += triangle[i][paths[j][1]-1]
                paths[j][1] -= 1
            elif paths[j][1] - 1 < 0:
                # left-end case: can only go right
                paths[j][0] += triangle[i][0]
                paths[j][1] = 0
            elif paths[j][1] >= len(triangle[i]):
                # right-end case: can only go left
                paths[j][0] += triangle[i][len(triangle[i])-1]
                paths[j][1] = len(triangle[i]) - 1

        for path2 in paths:
            for path1 in paths:
                # delete paths that have converged on one another
                if path1[1] == path2[1] and path1[2] != path2[2]:
                    if path1[0] > path2[0]:
                        path2[0] = path1[0]  # share largest sum
                    paths.remove(path1)
        i -= 1

    return paths[0][0]


print max_route(triangle_numbers)
