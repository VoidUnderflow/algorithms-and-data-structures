from heapq import heappush, heappop
from collections import defaultdict


# Calculates the next server idx, based on the current idx.
# next_server_idx % k = original server idx
# This needs to be done before every heap insert, to maintain the invariant.
def next_server_idx(server_idx: int, curr_idx: int, k: int) -> int:
    return curr_idx + (server_idx - curr_idx) % k


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []
        idle = list(range(k))  # heapify(idle) = idle

        count = defaultdict(int)
        max_count = 0

        for event_idx in range(len(arrival)):
            curr_arrival, curr_load = arrival[event_idx], load[event_idx]

            # Pop servers that finish their current task before the curr_arrival.
            while len(busy) > 0 and busy[0][0] <= curr_arrival:
                _, server_idx = heappop(busy)
                wrapped_server_idx = next_server_idx(server_idx, event_idx, k)
                heappush(idle, wrapped_server_idx)

            # Assign a server to the current event.
            if len(idle) == 0:
                # No server => event is dropped.
                continue

            # Get the next wrapped server idx and unwrap it to its original value.
            server_idx = heappop(idle) % k

            # Move the server to idle with its finish time.
            heappush(busy, (curr_arrival + curr_load, server_idx))
            count[server_idx] += 1
            max_count = max(count[server_idx], max_count)

        return [key for key in count if count[key] == max_count]


sol = Solution()
print(sol.busiestServers(3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3]))
print(sol.busiestServers(3, [1, 2, 3, 4], [1, 2, 1, 2]))
print(sol.busiestServers(3, [1, 2, 3], [10, 12, 11]))
