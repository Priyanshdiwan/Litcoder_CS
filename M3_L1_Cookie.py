import heapq
def total_steps(candies, target_sweetness):
    heapq.heapify(candies)
    
    steps = 0

    while candies[0] < target_sweetness:
        
        least_sweet = heapq.heappop(candies)
        second_least_sweet = heapq.heappop(candies)

        combined_sweetness = least_sweet + 2 * second_least_sweet


        heapq.heappush(candies, combined_sweetness)

        
        steps += 1

    return steps


target_sweetness = int(input().strip())
candies = list(map(int, input().strip().split()))


result = total_steps(candies, target_sweetness)
print(result)