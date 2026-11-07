from heapq import heappop, heapify, heappush


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        busy_servers = []

        free_servers = [(weight, idx) for (idx, weight) in enumerate(servers)]
        heapify(free_servers)

        curr_time = 0

        def pop_finished():
            while len(busy_servers) > 0 and busy_servers[0][0] <= curr_time:
                _, server_idx = heappop(busy_servers)
                heappush(free_servers, (servers[server_idx], server_idx))

        ans = []
        for task_idx, task_time in enumerate(tasks):
            curr_time = max(curr_time, task_idx)
            pop_finished()

            if len(free_servers) == 0:
                curr_time = busy_servers[0][0]
                pop_finished()

            _, server_idx = heappop(free_servers)
            ans.append(server_idx)
            heappush(busy_servers, (curr_time + task_time, server_idx))
        return ans


sol = Solution()
print(sol.assignTasks([3, 3, 2], [1, 2, 3, 2, 1, 2]))
print(sol.assignTasks([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1]))
