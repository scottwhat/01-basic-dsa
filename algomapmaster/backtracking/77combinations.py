def combine(n, k):
    res = []

    def backtrack(start, path):
        # If combination is full
        if len(path) == k:
            res.append(path[:])
            return
        
        # Explore numbers from 'start' to n
        for num in range(start, n + 1):
            path.append(num)             # Choose
            backtrack(num + 1, path)     # Move to the next number
            path.pop()                   # Undo (backtrack)

    backtrack(1, [])
    return res


if __name__ == "__main__":
    n = 4
    k = 2
    combinations = combine(n, k)
    print(combinations)