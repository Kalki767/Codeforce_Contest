from bisect import bisect_left, bisect_right


def solve():
    n, m = map(int,input().split())
    ratings = list(map(int,input().split()))
    problems = list(map(int,input().split()))
    problems.sort()
    kevin = ratings[0]
    ratings.sort()
    problem_solved = [0 for _ in range(m+1)]
    visited = set()
    solved_problems = []
    for rating in ratings:
        solved = bisect_right(problems,rating)
        problem_solved[solved] += 1
        if solved not in visited:
            visited.add(solved)
            solved_problems.append(solved)
    
    prefix_sum = [0]
    # problem_solved.reverse()
    solved_problems.reverse()
    for index in range(len(solved_problems)):
        solved = solved_problems[index]
        prefix_sum.append((index + 1)*problem_solved[solved] + prefix_sum[-1])
    
    print(prefix_sum)

t = int(input())
for _ in range(t):
    solve()
    