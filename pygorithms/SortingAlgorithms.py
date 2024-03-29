import heapq

def bubbleSort(nums):
    while any(nums[i] > nums[i+1] for i in range(len(nums)-1)):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

def selectionSort(nums):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

def insertionSort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current
    return nums

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [x for x in nums[1:] if x <= pivot]
    right = [x for x in nums[1:] if x > pivot]
    return left + [pivot] + right

def heapSort(nums):
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]

def radixSort(nums):
    RADIX = 10
    max_digit = max(nums)
    placement = 1
    while placement < max_digit:
        buckets = [[] for _ in range(RADIX)]
        for num in nums:
            digit = (num // placement) % RADIX
            buckets[digit].append(num)
        nums = [item for bucket in buckets for item in bucket]
        placement *= RADIX
    return nums

def countingSort(nums):
    count, min_val, max_val = {}, min(nums), max(nums)
    for num in nums:
        count[num] = count.get(num, 0) + 1
    return [num for num in range(min_val, max_val + 1) for _ in range(count.get(num, 0))]

def shellSort(nums):
    gaps = [7, 2, 1]
    for gap in gaps:
        for i in range(gap, len(nums)):
            temp, j = nums[i], i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
    return nums

def timSort(nums):
    return nums.sort()

def topologicalSort():
    visited = set()
    stack = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            if node in graph:  # If the node has dependencies
                for neighbour in graph[node]:  # Iterate through its dependencies
                    dfs(neighbour)
            stack.append(node)  # Append the node to the stack after visiting its neighbours

    for node in graph:
        dfs(node)

    return stack[::-1] 