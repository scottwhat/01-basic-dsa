# from collections import deque

# def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
#     q: deque[int] = deque()  # stores *indices*
#     res = []
#     for i, cur in enumerate(nums):
#         while q and nums[q[-1]] <= cur:
#             q.pop()
#         q.append(i)
#         # remove first element if it's outside the window
#         if q[0] == i - k:
#             q.popleft()
#         # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
#         if i >= k - 1:
#             res.append(nums[q[0]])

#     return res


from collections import deque

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    q = deque()
    output = []
    l = r = 0

    while r < len(nums):
        # while smaller vals exist in the que, pop them. then add new val to queue
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # remove left value if its out of bounds
        if q and l > q[0]:
            q.popleft()

        # edge case, because left and right start at 0, make sure you start at window size k
        if (r + 1) >= k:
            output.append(nums[q[0]])
            # left only incremented once size k
            l += 1

        r += 1

    return output
                
            