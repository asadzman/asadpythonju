# Implement a priority queue that sorts items by a given priority and always
# returns the item with the highest priority on each pop operation.
import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        # store negative priority to simulate max-heap
        heapq.heappush(self.heap, (-priority, item))

    def pop(self):
        if not self.heap:
            return None
        priority, item = heapq.heappop(self.heap)
        return item

    def is_empty(self):
        return len(self.heap) == 0


# Example usage
pq = PriorityQueue()

n = int(input("Enter number of items: "))

for _ in range(n):
    item = input("Enter item: ")
    priority = int(input("Enter priority: "))
    pq.push(item, priority)

print("\nItems popped in priority order:")

while not pq.is_empty():
    print(pq.pop())
