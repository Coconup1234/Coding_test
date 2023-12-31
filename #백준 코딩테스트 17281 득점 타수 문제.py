import itertools

N = int(input())

innis = []

for _ in range(N):
    innis.append(list(map(int, input().split())))

ans = 0

def func(case):
    tmp_ans = 0
    inning = 0
    num = 0
    while inning < len(innis):
        out = 0
        b0 = b1 = b2 = 0
        while out < 3:
            if num == 3:
                cur = innis[inning][0]
            elif num < 3:
                cur = innis[inning][case[num]+1]
            else:
                cur = innis[inning][case[num-1]+1]
            if cur == 4:
                tmp_ans += (b0 + b1 + b2 + 1)
                b0 = b1 = b2 = 0
            elif cur == 0:
                out += 1
            elif cur == 1:
                tmp_ans += b2
                b0, b1, b2 = 1, b0, b1
            elif cur == 2:
                tmp_ans += (b1 + b2)
                b0, b1, b2 = 0, 1, b0
            elif cur == 3:
                tmp_ans += (b0 + b1 + b2)
                b0, b1, b2 = 0, 0, 1
            num = (num+1) % 9
        inning += 1
    return tmp_ans

cases = list(itertools.permutations(range(len(innis[0])-1), len(innis[0])-1))
out = 0
for case in cases:
    ans = max(ans, func(case))

print(ans)