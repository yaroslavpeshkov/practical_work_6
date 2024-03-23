children_n, children_k, minutes_m = map(int, input().split())
if children_k > children_n:
    children_k = children_n
times = (2*children_n // children_k)
if 2*children_n % children_k != 0:
    times += 1
time = times * minutes_m
print(time)
