def damageCalc(arr):
    damageRate = 1
    totalDamage = 0
    for i in arr:
        if i == 'S':
            totalDamage += damageRate
        else:
            damageRate *= 2
    return totalDamage


def main():
    for test in range(1, int(input()) + 1):
        D, P = input().strip().split()
        D, P = int(D), list(P)
        count, totalSwaps = 0, 0
        while True:
            prevDamage = damageCalc(P)
            if prevDamage <= D:
                break
            else:
                found_S = False
            for i in range(len(P)):
                loc = len(P) - i - 1
                if P[loc] == 'S':
                    found_S = True
                elif found_S:
                    P[loc] = 'S'
                    P[loc + 1] = 'C'
                    totalSwaps += 1
                    break
            if prevDamage == damageCalc(P):
                break
            count += 1

        print('Case #{0}: {1}'.format(test, totalSwaps if damageCalc(P) <= D else 'IMPOSSIBLE'))

main()
