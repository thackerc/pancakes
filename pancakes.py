T = int(input())
for t in range(T):
    S = input() + "+"
    print(f"Case #{t+1}: {S.count('+-') + S.count('-+')}")
