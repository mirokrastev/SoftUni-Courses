n = int(input())
garbage_collector = 0
collector = 0

for i in range(n):
    inp = int(input())
    garbage_collector += inp
    if collector + inp <= 255:
        collector += inp
        continue
    if garbage_collector > 255:
        print('Insufficient capacity!')
print(collector)