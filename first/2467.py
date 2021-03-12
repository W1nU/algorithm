N = int(input())
costs = list(map(int, input().split()))
min_cost = float('inf')
l_c = len(costs)
ans = ()

for i in range(l_c - 1):
    start = i + 1
    end = l_c - 1
    cost = costs[i]

    while start <= end:
        mid = (start + end) // 2 
        new_cost = costs[mid] + cost
        abs_new_cost = abs(new_cost)
        
        if abs_new_cost < min_cost:
            ans = (costs[i], costs[mid])
            min_cost = abs_new_cost
        
        if new_cost < 0:
            start = mid + 1
        
        else:
            end = mid - 1

print(" ".join(map(str, ans)))