target = 36000000
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

i = 0
while True:
    i += 1
    s = 10 * sum(factors(i))
    if s >= target:
        print 'part 1:', i
        break

i = 0
while True:
    i += 1
    s = sum(11 * f for f in factors(i) if i / f <= 50)
    if s >= target:
        print 'part 2:', i
        break
