# Patient 1
# FIXED: range(1, 10) stops before 10, so it was changed to range(1, 11).

for i in range(1, 11):
    print(i)


# Patient 2
# FIXED: n was never decreased, causing an infinite loop. We subtract 1 each time.

n = 3

while n > 0:
    print(n)
    n -= 1


# Patient 3
# FIXED: total was reset to 0 inside the loop. It must be initialized before the loop.

total = 0

for i in range(1, 6):
    total = total + i

print(total)