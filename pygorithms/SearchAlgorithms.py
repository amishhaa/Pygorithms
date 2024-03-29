import heapq

def linearSearch(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i  
    return -1

def binarySearch(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid  
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def depthFirstSearch(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])
    return visited

def breathFirstSearch(graph, start):
    visited = []  
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex])
    return visited

def aSearch(graph, start, goal, heuristic):
    open_set = [(0, start)] 
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None

def uniformCostSearch(graph, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor, edge_weight in graph[current].items():
            tentative_g_score = g_score[current] + edge_weight
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (g_score[neighbor], neighbor)) 
    return None

def exponentialSearch(arr, item):
    arr.sort()
    n = len(arr)
    i = 1
    while i < n and arr[i] <= item:
        i *= 2
    if i > n:
        return binarySearch(arr, item, i // 2, n - 1)
    else:
        return binarySearch(arr, item, i // 2, min(i, n - 1))

def fibonacciSearch(arr, item):
    arr.sort()
    n = len(arr)
    fib_nums = [0, 1]
    while fib_nums[-1] < n:
        fib_nums.append(fib_nums[-2] + fib_nums[-1])
    fib_m = len(fib_nums) - 1
    while fib_m > 0 and fib_nums[fib_m - 1] >= n:
        fib_m -= 1
    offset = 0
    while fib_m > 0:
        i = min(offset + fib_nums[fib_m - 1] - 1, n - 1)
        if arr[i] == item:
            return i
        elif arr[i] < item:
            fib_m -= 1
            offset = i + 1
        else:
            fib_m -= 2
    return -1

def jumpSearch(arr, item):
    arr.sort()
    n = len(arr)
    jump = int(n**0.5)
    curr = 0
    while curr < n and arr[curr] <= item:
        next = min(curr + jump, n - 1)
        if arr[next] == item:
            return next
        elif arr[next] < item:
            curr = next
        else:
            break
    for i in range(curr + 1, min(curr + jump, n)):
        if arr[i] == item:
            return 
    return -1  