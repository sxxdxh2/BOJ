import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if heap:
            print(hq.heappop(heap))
        else:
            print(0)
    else:
        hq.heappush(heap, x)
