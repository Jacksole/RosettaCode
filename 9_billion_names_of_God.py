cache = [[1]]


def cumu(n):
    for l in range(len(cache), n+1):
        r = [0]
        for x in range(1, l+1):
            r.append(r[-1] + cache[l-x][min(x, l-x)])
        cache.append(r)
    return cache[n]


def row(n):
    r = cumu(n)
    return [r[i+1] - r[i] for i in range(n)]


print("rows:")
for x in range(1, 11):
    print("%2d:" % x, row(x))

print("\nsums:")
for x in [23, 123, 1234, 12345]:
    print(x, cumu(x)[-1])


def partitions(n):
    partitions.p.append(0)
    
    for k in range(1, n + 1):
        d = n - k * (3 * k - 1) // 2
        if d < 0:
            break
        if k & 1:
            partitions.p[n] += partitions.p[d]
        else:
            partitions.p[n] -= partitions.p[d]
        
        d -= k
        if d < 0:
            break
        if k & 1:
            partitions.p[n] += partitions.p[d]
        else:
            partitions.p[n] -= partitions.p[d]
    return partitions.p[-1]


partitions.p = [1]


def main():
    ns = set([23, 123, 1234, 12345])
    max_ns = max(ns)
    
    for i in range(1, max_ns + 1):
        if i > max_ns:
            break
        p = partitions(i)
        if i in ns:
            print ("%6d: %s" % (i, p))

if __name__ == "__main__":
    main()
