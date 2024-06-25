import sys
input = lambda: sys.stdin.readline().strip()
mod = 10 ** 9 + 7 # 998244353

k, a, b = map(int, input().split())
alice, bob, cnt = 0, 0, 0
aa = [list(map(int, input().split())) for _ in range(3)]
bb = [list(map(int, input().split())) for _ in range(3)]
memo = [[-1] * 4 for _ in range(4)]
while memo[a][b] == -1 and cnt < k:
    memo[a][b] = cnt
    if (a == 3 and b == 2) or (a == 2 and b == 1) or (a == 1 and b == 3):
        alice += 1
    elif a != b:
        bob += 1
    # print(f"1a: {a}, b: {b}, alice: {alice}, bob: {bob}")
    a, b = aa[a - 1][b - 1], bb[a - 1][b - 1]
    cnt += 1
if cnt == k:
    exit(print(alice, bob))
memo = [[-1] * 4 for _ in range(4)]
Alice, Bob, cnt, k = 0, 0, 0, k - cnt
# print(f"alice: {alice}, bob: {bob}, k: {k}")
while memo[a][b] == -1 and cnt < k:
    memo[a][b] = cnt
    if (a == 3 and b == 2) or (a == 2 and b == 1) or (a == 1 and b == 3):
        Alice += 1
    elif a != b:
        Bob += 1
    # print(f"2a: {a}, b: {b}, Alice: {Alice}, Bob: {Bob}")
    a, b = aa[a - 1][b - 1], bb[a - 1][b - 1]
    cnt += 1
if cnt == k:
    exit(print(alice + Alice, bob + Bob))
circle = k // cnt
alice, bob = alice + Alice * circle, bob + Bob * circle
k %= cnt
while k:
    if (a == 3 and b == 2) or (a == 2 and b == 1) or (a == 1 and b == 3):
        alice += 1
    elif a != b:
        bob += 1
    # print(f"3a: {a}, b: {b}, alice: {alice}, bob: {bob}")
    a, b = aa[a - 1][b - 1], bb[a - 1][b - 1]
    k -= 1
print(alice, bob)
